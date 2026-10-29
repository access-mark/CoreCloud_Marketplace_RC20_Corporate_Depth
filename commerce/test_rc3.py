import subprocess,os,tempfile,time,urllib.request,json,urllib.error
root='/mnt/data/rc3_build/corecloud-marketplace.com-main';db=tempfile.mktemp(suffix='.sqlite3');env={**os.environ,'MARKETPLACE_DB':db,'MARKETPLACE_ADMIN_KEY':'test-secret','PORT':'18878'}
p=subprocess.Popen(['python',root+'/commerce/server.py'],env=env,stdout=subprocess.DEVNULL)
def call(path,data=None,admin=False):
 req=urllib.request.Request('http://127.0.0.1:18878'+path,data=json.dumps(data).encode() if data is not None else None,headers={'Content-Type':'application/json',**({'X-Admin-Key':'test-secret'} if admin else {})})
 try:
  with urllib.request.urlopen(req,timeout=3) as r:return r.status,json.load(r)
 except urllib.error.HTTPError as e:return e.code,json.load(e)
try:
 time.sleep(1.5)
 assert call('/api/health')[0]==200
 assert call('/api/products')[1]['products']==[]
 assert call('/api/admin/orders')[0]==403
 product={'id':'t14-test','name':'ThinkPad T14 test','category':'Professional','description':'Verified test device','price_cents':750000,'stock':2,'active':True}
 assert call('/api/admin/product',product,True)[0]==200
 assert len(call('/api/products')[1]['products'])==1
 order={'customer':'Test Buyer','email':'buyer@example.com','phone':'0123456789','province':'Gauteng','consent':True,'items':[{'id':'t14-test','quantity':1}]}
 status,r=call('/api/orders',order);assert status==201,(status,r)
 assert r['total_cents']==750000
 assert call('/api/order/status',{'order_id':r['order_id'],'lookup_token':'wrong'})[0]==404
 assert call('/api/order/status',{'order_id':r['order_id'],'lookup_token':r['lookup_token']})[0]==200
 assert call('/api/orders',{'items':[{'id':'t14-test','quantity':99}],**{k:v for k,v in order.items() if k!='items'}})[0]==400
 assert call('/api/orders',{'items':[{'id':'t14-test','quantity':2}],**{k:v for k,v in order.items() if k!='items'}})[0]==409
 assert call('/api/admin/status',{'order_id':r['order_id'],'status':'cancelled'},True)[0]==200
 assert call('/api/admin/status',{'order_id':r['order_id'],'status':'cancelled'},True)[0]==409
 assert call('/api/products')[1]['products'][0]['stock']==2
 print('PASS: health, unpublished catalogue, admin auth, inventory, order, totals, private lookup, validation, oversell protection, cancellation/restock, terminal state')
finally:
 p.terminate();p.wait(timeout=3)
 for suffix in ('','-wal','-shm'):
  try:os.remove(db+suffix)
  except FileNotFoundError:pass
