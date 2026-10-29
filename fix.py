from pathlib import Path
import re,zipfile
root=Path('/mnt/data/rc8_work'); img=root/'assets/images';img.mkdir(parents=True,exist_ok=True)
for name,brand,model,accent in [('lenovo-thinkpad','LENOVO','ThinkPad','25B5A6'),('dell-latitude','DELL','Latitude','3788C7'),('hp-elitebook','HP','EliteBook','6D84A7')]:
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 630" role="img" aria-label="Illustrative {brand} {model} business laptop, not an actual product photograph"><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#091d2a"/><stop offset="1" stop-color="#164451"/></linearGradient><linearGradient id="screen" x2="1" y2="1"><stop stop-color="#102e42"/><stop offset="1" stop-color="#{accent}"/></linearGradient></defs><rect width="1000" height="630" fill="url(#bg)"/><circle cx="780" cy="160" r="260" fill="none" stroke="#5fd1c5" opacity=".15"/><rect x="205" y="100" width="590" height="368" rx="18" fill="#101921" stroke="#697d87" stroke-width="8"/><rect x="228" y="123" width="544" height="318" rx="4" fill="url(#screen)"/><path d="M228 410 L500 123 L772 123 L772 441 L228 441Z" fill="#fff" opacity=".055"/><circle cx="500" cy="111" r="3" fill="#83959e"/><path d="M180 470 H820 L910 524 Q916 536 900 540 H100 Q84 536 90 524Z" fill="#9daab0"/><path d="M200 471 H800 L848 512 H152Z" fill="#263740"/><path d="M428 518 H572 L560 529 H440Z" fill="#72858f"/><text x="500" y="286" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="55" fill="#fff">{brand}</text><text x="500" y="333" text-anchor="middle" font-family="Arial,sans-serif" font-size="25" letter-spacing="5" fill="#e5f4f5">{model.upper()}</text><text x="500" y="588" text-anchor="middle" font-family="Arial,sans-serif" font-size="18" fill="#c6d8df">ILLUSTRATIVE DEVICE FAMILY · CONFIGURATION MAY VARY</text></svg>'''
 (img/f'{name}.svg').write_text(s)
# Replace the Apple/MacBook hero photo throughout the site with a neutral business laptop illustration.
for p in root.rglob('*'):
 if p.suffix not in ('.html','.js'):continue
 t=p.read_text()
 t=re.sub(r'https://images\.unsplash\.com/photo-1517336714731-489689fd1ca8\?[^"\'<> ]+', 'assets/images/dell-latitude.svg' if p.suffix=='.html' else 'assets/images/dell-latitude.svg',t)
 if p.name=='rc5.js':
  # Three repeating card photos -> corresponding brand illustration, based on product name.
  t=re.sub(r"\['https://images\.unsplash\.com/photo-1496181133206-80ce9b88a853\?[^']+','assets/images/dell-latitude.svg','https://images\.unsplash\.com/photo-1486312338219-ce68d2c6f44d\?[^']+'\]\[items\.indexOf\(p\)%3\]", "(/Lenovo/i.test(p.name)?'assets/images/lenovo-thinkpad.svg':/Dell/i.test(p.name)?'assets/images/dell-latitude.svg':'assets/images/hp-elitebook.svg')",t)
 p.write_text(t)
# add release notes
(root/'RC8_DEVICE_IMAGE_CORRECTION.md').write_text('''# RC8 device imagery correction\n\nRemoved the Apple/MacBook stock photo from the storefront and replaced product-card photographs with original, lightweight illustrative business-laptop SVGs. Lenovo ThinkPad and Dell Latitude/Precision cards are mapped by product name. HP asset is available for future verified HP stock. Illustrations are not exact model photographs. No Apple products are offered.\n\nCommerce status unchanged: online payments, stock sync, and production order fulfilment are not verified.\n''')
out=Path('/mnt/data/CoreCloud_Marketplace_RC8_No_Apple_Imagery.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p in root.rglob('*'):
  if p.is_file() and p.name!='fix.py':z.write(p,p.relative_to(root))
print(out)
