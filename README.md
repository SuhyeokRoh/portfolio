# 노수혁 포트폴리오 — 배포용 정적 사이트

슬라이드 38장을 웹에서 바로 볼 수 있는 단일 페이지입니다. 빌드 과정 없이 폴더 그대로 올리면 됩니다.

## 폴더 구성

```
index.html          뷰어 (의존성 없음, 이 파일 하나가 전부)
portfolio.pdf       원본 PDF — 상단 PDF 버튼으로 다운로드됨
slides/             슬라이드 1920px WebP 38장
thumbs/             목차용 썸네일 38장
vercel.json         이미지 캐시 헤더 (Vercel 전용, 없어도 동작)
.nojekyll           GitHub Pages 전용 (없어도 동작)
```

## 배포

### Vercel — 가장 간단

1. [vercel.com](https://vercel.com) 로그인 → **Add New → Project**
2. **Deploy without Git** 쪽에서 이 폴더를 통째로 드래그
3. 바로 `https://<프로젝트이름>.vercel.app` 발급
4. Settings → Domains 에서 주소를 `suhyeok-roh.vercel.app` 같은 걸로 변경 가능

### Netlify — 계정 없이도 가능

[app.netlify.com/drop](https://app.netlify.com/drop) 에 이 폴더를 드래그하면 즉시 링크가 나옵니다. 계정을 만들면 주소를 바꿀 수 있습니다.

### GitHub Pages — 주소가 가장 깔끔

```bash
git init
git add .
git commit -m "portfolio"
git branch -M main
git remote add origin https://github.com/SuhyeokRoh/portfolio.git
git push -u origin main
```

저장소 **Settings → Pages → Source: Deploy from a branch → main / (root)** 설정 후 1~2분 기다리면
`https://suhyeokroh.github.io/portfolio` 로 열립니다.

## 조작

| 동작 | 방법 |
|---|---|
| 다음 / 이전 | `→` `←` `Space` / 화면 좌우 클릭 / 모바일 스와이프 |
| 처음 / 끝 | `Home` / `End` |
| 전체 목차 | `G` — 썸네일 클릭으로 해당 장 이동 |
| 확대 | 슬라이드 클릭 (모바일에선 탭) |
| 전체화면 | `F` |
| 닫기 | `Esc` |

진행 바를 클릭하면 그 지점으로 바로 이동합니다.

## 특정 슬라이드 링크

주소 뒤에 `#숫자`를 붙이면 그 장으로 바로 열립니다.
예) `https://.../#12` → 12번째 슬라이드

지원서에 "트러블슈팅은 12쪽부터" 같이 적을 때 쓰면 됩니다.

## 슬라이드를 수정했을 때

PPT를 고친 뒤 PDF로 내보내고, 아래를 다시 실행하면 이미지가 갱신됩니다.

```bash
# PDF → 1920px WebP
pdftoppm -png -r 144 portfolio.pdf slides/s
cd slides && for f in s-*.png; do mv "$f" "$(echo $f | sed 's/s-0*/slide-/')"; done
# PNG → WebP 변환과 썸네일 생성은 Pillow 사용 (convert.py 참고)
```

장수가 바뀌면 `index.html` 안의 `var TOTAL = 38;` 값도 함께 고쳐야 합니다.
