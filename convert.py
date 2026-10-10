"""PDF -> 뷰어용 WebP 슬라이드 + 썸네일 생성. 사용: python3 convert.py portfolio.pdf"""
import glob, os, subprocess, sys
from PIL import Image

pdf = sys.argv[1] if len(sys.argv) > 1 else 'portfolio.pdf'
os.makedirs('slides', exist_ok=True); os.makedirs('thumbs', exist_ok=True)
for f in glob.glob('slides/*') + glob.glob('thumbs/*'):
    os.remove(f)

subprocess.run(['pdftoppm', '-png', '-r', '144', pdf, 'slides/s'], check=True)

n = 0
for f in sorted(glob.glob('slides/s-*.png')):
    n = int(os.path.basename(f).split('-')[1].split('.')[0])
    im = Image.open(f).convert('RGB')
    im.save('slides/slide-%d.webp' % n, 'WEBP', quality=88, method=6)
    th = im.copy(); th.thumbnail((400, 400))
    th.save('thumbs/slide-%d.webp' % n, 'WEBP', quality=80, method=6)
    os.remove(f)

print('슬라이드 %d장 생성 완료 — index.html 의 TOTAL 값을 %d 로 맞추세요.' % (n, n))
