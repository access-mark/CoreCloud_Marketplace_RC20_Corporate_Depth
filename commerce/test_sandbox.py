import unittest, tempfile, os, sys, importlib, hashlib
from unittest.mock import patch
os.environ['MARKETPLACE_DB']=tempfile.mktemp(suffix='.db')
sys.path.insert(0,os.path.dirname(__file__))
import sandbox_server as s
class Tests(unittest.TestCase):
 def test_signature_matches_documented_example(self):
  d={'merchant_id':'10000100','merchant_key':'46f0cd694581a','amount':'100.00','item_name':'Test Product'}
  expected=hashlib.md5(('merchant_id=10000100&merchant_key=46f0cd694581a&amount=100.00&item_name=Test+Product&passphrase=jt7NOE43FZPn').encode()).hexdigest()
  self.assertEqual(s.signature(d,'jt7NOE43FZPn'),expected)
 def test_tamper_changes_signature(self):
  d={'amount':'100.00'};a=s.signature(d,'secret');d['amount']='1000.00';self.assertNotEqual(a,s.signature(d,'secret'))
 def test_no_live_host(self):self.assertEqual(s.SANDBOX_HOST,'https://sandbox.payfast.co.za')
 def test_untrusted_ip(self):
  with patch.object(s.socket,'gethostbyname_ex',return_value=('sandbox.payfast.co.za',[],['192.0.2.1'])):
   self.assertFalse(s.trusted_ip('203.0.113.99'));self.assertTrue(s.trusted_ip('192.0.2.1'))
 def test_seeds_inactive(self):
  s.base.init()
  with s.base.conn() as c:self.assertEqual(c.execute('SELECT COUNT(*) FROM products WHERE active=1').fetchone()[0],0)
if __name__=='__main__':unittest.main()
