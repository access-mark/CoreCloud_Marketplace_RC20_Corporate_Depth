import unittest,tempfile,os,time,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
import server
class HardeningTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();server.DB=Path(self.tmp.name)/'test.sqlite3';server.init()
 def tearDown(self):self.tmp.cleanup()
 def test_reservation_expiry_releases_stock_once(self):
  with server.conn() as c:
   c.execute("UPDATE products SET stock=2,active=1,price_cents=10000 WHERE id='thinkpad-t14'")
   c.execute("INSERT INTO orders(id,email,customer,phone,province,programme,status,total_cents,created,lookup_hash,consent) VALUES('A','a@b.co','A','123','Gauteng','General','awaiting_payment',10000,1,'hash',1)")
   c.execute("INSERT INTO order_items VALUES('A','thinkpad-t14','T14',1,10000)")
   c.execute("UPDATE products SET stock=1 WHERE id='thinkpad-t14'")
   c.execute("INSERT INTO reservations(order_id,expires) VALUES('A',1)")
  self.assertEqual(server.expire_reservations(),1)
  self.assertEqual(server.expire_reservations(),0)
  with server.conn() as c:
   self.assertEqual(c.execute("SELECT stock FROM products WHERE id='thinkpad-t14'").fetchone()[0],2)
   self.assertEqual(c.execute("SELECT status FROM orders WHERE id='A'").fetchone()[0],'expired')
 def test_delivery_columns_created(self):
  with server.conn() as c:
   cols={r[1] for r in c.execute('PRAGMA table_info(orders)')}
  self.assertTrue({'address_line1','city','postal_code'}.issubset(cols))
if __name__=='__main__':unittest.main()
