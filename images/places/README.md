# Place photographs

## v26 additions — 2026-09-30

The app now uses 36 place photographs. The 17 v26 additions are `chebu`, `jalppajin`, `gippen`, `sujebi`, `london`, `osulloc`, `chatteul`, `fritz`, `teatherapy`, `park`, `daelim`, `hakgojae`, `boan`, `baekinje`, `sangchon`, `sajik`, and `donglim` (`.jpg`).

Exact source pages, original image URLs, providers and retrieval date are retained in [catalog_assets_v26.json](../../research/catalog_assets_v26.json); [the editorial report](../../research/CATEGORY_EXPANSION_V26.md) links each place's official tourism source. These are reference photos with **redistribution permission not established**. The report and manifest do not grant a reuse license. Across v23 and v26, 34 reference photos need permission or replacement before public release; the two Commons photos retain the licenses below.

`fritz` uses the article's Wonseo café photo rather than its general header. `park` shows the museum's exterior steps. `sangchon` is a source-provided collage of the hanok and its architectural details, not the article's promotional banner. `boan` includes an earlier exhibition, `chatteul` shows an evening entrance, and `sajik` depicts the altar rather than guaranteeing public access inside it. Captions distinguish these limits. Full source compositions and visible markings are retained. No image was generated or retouched. See [photo contact sheet](../../research/catalog-photos-v26.jpg).

`scripts/fetch_catalog_assets_v26.py` downloads these reference originals from the official pages collected by `scripts/collect_catalog_v26.py`. `scripts/build_preview_assets.py` creates the app derivatives. The `osulloc.jpg` download contains a PNG source; Pillow decodes its actual format for the WebP derivatives while preserving the original bytes as the fallback.

## Original and v23 sources

Source review: 2026-09-29. The app now displays actual place photographs, preserving their proportions and source watermarks. Each detail screen links to the source and identifies the provider. Unknown dates are explicitly labeled. Images are not retouched.

| File | Subject | Author | License | Original |
| --- | --- | --- | --- | --- |
| jeongdok.jpg | Jeongdok Library, 2025 | EllalineSeoul | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | [Original](https://commons.wikimedia.org/wiki/File:Jeongdok_Library.jpg) |
| suseongdong.jpg | Giringyo in Suseongdong Valley, 2020 | 오모군 | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) | [Original](https://commons.wikimedia.org/wiki/File:Giringyo.jpg) |

## Official reference photographs used in the local preview

| File | Place | Provider / source page |
| --- | --- | --- |
| onion.jpg | 어니언 안국 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=191156) |
| staffpicks.jpg | 스태픽스 | [한국관광공사](https://access.visitkorea.or.kr/food/detail.do?cotId=5fcd1c8c-4d80-443e-a5ed-3bad2e9ebbaf) |
| craft.jpg | 서울공예박물관 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=186458) |
| baeryeom.jpg | 계동 배렴 가옥 | [국가유산포털](https://www.heritage.go.kr/heri/cul/culSelectDetail.do?ccbaCpno=4411100850000&pageNo=1_1_1_1) |
| daeo.jpg | 대오서점 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=198592) |
| yisang.jpg | 이상의 집 | [문화유산국민신탁](https://nationaltrustkorea.org/) |
| tongin.jpg | 통인시장 입구 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=79811) |
| tosokchon.jpg | 토속촌 삼계탕 메뉴 | [한국관광공사 게시, 원본 저작자 워터마크 유지](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=97919) |
| hwangsaengga.jpg | 황생가 칼국수 메뉴 | [네이버블로그 이용 · 한국관광공사 게시](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=86236) |
| changdeok.jpg | 창덕궁 후원 (별도 관람 구역) | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=94399) |
| unhyeon.jpg | 운현궁 가옥과 마당 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111253) |
| gogung.jpg | 고궁박물관 계단 있는 정면 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=106970) |
| gyeongbok.jpg | 경복궁 경회루 외부 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=87740) |
| folk.jpg | 민속박물관 외관과 앞마당 | [한국관광공사](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110875) |
| mmca.jpg | 국립현대미술관 서울 외관 | [서울관광재단 · 한국관광공사 게시](https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=76101) |
| workshop.jpg | 북촌전통공예체험관 마당 | [서울시 공공서비스예약](https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S240122144020674558) |
| bukchoncenter.jpg | 북촌문화센터 입구 (과거 행사 안내 포함) | [서울관광재단](https://english.visitseoul.net/PalaceArea/Bukchon-Traditional-Culture-Center-k/ENP018916) |

These 17 photos have verified subject identity but their redistribution permissions have not been established. Public availability and source attribution do not establish a reuse license. Before publishing, confirm permission for each exact image or replace it with a permitted photograph. Do not infer a license from other images of the same property. The downloader `scripts/fetch_reference_photos.py` records the original six image URLs. The 11 additions are recorded in `research/expansion_assets_v23.json` by `scripts/fetch_expansion_assets.py`.

The previous illustrative images under the parent `images/` directory are no longer referenced by the active app. Existing files are retained rather than erased.

## v20 delivery derivatives

`optimized/*-480.webp` and `*-960.webp` are resized and WebP-encoded derivatives
of the above files, generated by `scripts/build_preview_assets.py`. The full
composition, proportions, and source watermarks are retained; there is no crop,
retouch, or fabricated entrance/scene. Images smaller than a target size are not
upscaled. Credits and license links continue to refer to the original source;
the UI discloses resizing and format conversion. Original JPGs are retained as
fallbacks. Dimensions and file byte counts are in `optimized/manifest.json`.
