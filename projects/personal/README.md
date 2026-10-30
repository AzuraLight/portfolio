# 개인 프로젝트

업무에서 반복된 불편을 해결하려고 만든 도구들입니다. 대부분 MIT 라이선스이고, 계정이나
텔레메트리 없이 동작하도록 만들었습니다.

## VS Code 확장

### Gitline — [repo](https://github.com/AzuraLight/gitline)
GitLens 의 대안으로 만든 커밋 그래프 확장입니다. 하단 패널에 Git 그래프를 띄웁니다. 현재 v1.2.0 입니다.
- SVG 레인 그래프(브랜치별 색, 베지어 병합선)와 HEAD · 로컬 · 원격 · 태그 칩
- 가상 스크롤로 큰 저장소에서도 빠르게 동작합니다. `.git` 을 감시해서 자동으로 새로고침합니다.
- 작성자·메시지·SHA 검색, 파일 단위 이력(이름 변경 추적), 클릭 한 번으로 파일 diff
- 멀티 저장소 선택, Pull / Push / Fetch, ahead·behind 배지, force-with-lease
- 작업 중 변경과 stash 를 그래프 안에 함께 표시합니다. 영어·한국어 지원
- 기술: TypeScript · VS Code Webview · Git CLI

### BindB — [repo](https://github.com/AzuraLight/bindb)
VS Code 안에서 쓰는 Database IDE 입니다. PostgreSQL · MySQL/MariaDB · SQLite · H2 를 지원합니다.
- 연결 → 스키마 → 테이블 → 컬럼 탐색기
- 커서가 있는 문장 실행(⌘↵), 스크롤하면 페이지 단위로 결과를 받아 오는 결과 그리드(Glide Data Grid)
- 스키마를 아는 자동완성: FROM/JOIN 뒤 테이블, 별칭 컬럼, INSERT 컬럼 목록
- 파일별 연결 지정(`-- @conn:`), 읽기 전용 연결, 비밀번호는 OS 키체인에 저장
- H2 는 Node 드라이버가 없어서 내장 PostgreSQL 프로토콜 서버를 거쳐 연결합니다
- 기술: TypeScript · pg · mysql2 · sql.js · React(그리드 웹뷰) · esbuild

### OpenAPI Explorer — [repo](https://github.com/AzuraLight/openapi-explorer)
에디터를 떠나지 않고 Swagger/OpenAPI 게이트웨이를 탐색·검색·호출하는 확장입니다. 현재 v1.1.0 입니다.
- 사이드바 트리(게이트웨이 → 태그 → 엔드포인트 · 모델)와 내장 Swagger UI 딥링크
- Try it out 요청을 확장 호스트에서 보내서 CORS 없이 동작합니다. 사내 프록시 · 사설 CA · 토큰을 지원합니다
- 엔드포인트 퍼지 검색. 우클릭으로 TS 응답 타입 · fetch/axios 함수 · cURL 을 생성합니다
- Swagger UI 를 번들해서 오프라인·방화벽 환경에서도 씁니다

### Midnight ERD — [repo](https://github.com/AzuraLight/midnight-erd)
SQL DDL 을 인터랙티브 ERD 로 그리는 확장입니다(의존성 없는 SVG).
- CREATE/ALTER TABLE · 복합 키 · COMMENT 를 파싱합니다
- FK 깊이 기반 계층 자동 배치(교차 최소화)와 Crow's-foot 표기
- 검색과 포커스, 관계 하이라이트, 배치 저장
- PNG · SVG 내보내기, 마크다운 데이터 사전 내보내기

### Terminal CD Click — [repo](https://github.com/AzuraLight/terminal-cd-click)
터미널 출력의 디렉터리 이름을 클릭하면 그 디렉터리로 `cd` 합니다. 셸 통합 cwd 를 기준으로 경로를 풀고,
POSIX 와 Windows 따옴표 처리를 지원합니다. 4개 언어를 지원합니다.

### Cairn
AI 코딩 에이전트(Cursor · Claude Code · Codex)가 읽는 작업 세션 인수인계 문서를 자동으로 관리하는 확장입니다.
- 오늘 목표를 체크하면 LOG · HANDOFF 문서에 자동으로 기록합니다. 디스크를 감시하므로 CLI 에이전트가 고친 것도 잡힙니다
- 끝내지 못한 목표는 다음 세션으로 넘어갑니다. 사이드바에 진행 상황을 표시합니다

### 그 밖의 확장
- **Notion MD:** 마크다운 파일을 Notion 스타일 블록 에디터로 편집합니다(슬래시 메뉴 · 단축 서식 · 양방향 동기화)
- **Todo Kanban:** 형식 없이 쓴 `todo.md` 를 칸반 보드로 보여 줍니다
- **Claude Right Editor:** Cursor 에서 Claude Code 를 오른쪽 에디터 그룹에 도킹합니다

## Vue 3 라이브러리

### vue-force-network-map — [repo](https://github.com/AzuraLight/vue-force-network-map)
D3 force 기반 인터랙티브 네트워크 그래프입니다. 클러스터 배치와 방사형 트리 배치를 지원합니다.
드래그 · 줌 · 포커스 · 다중 강조 · 카메라 API(`lookAtNode` · `frameAll` · 인트로 애니메이션)가 들어 있습니다.
HRD-Net 추천 지식맵을 일반화해 라이브러리로 만들었습니다.

### vue-bullseye-chart — [repo](https://github.com/AzuraLight/vue-bullseye-chart)
`value(0~1)` 만 넘기면 동심원에 자동으로 배치하는 불스아이 차트입니다. 주요 차트 라이브러리에는 없는
차트 형태입니다. 키보드 접근성과 ARIA 를 기본 지원합니다.

### vue-safe-iframe — [repo](https://github.com/AzuraLight/vue-safe-iframe)
sandbox, origin 검증, 로드 타임아웃, 오류 fallback 을 표준대로 처리한 iframe 래퍼와 모달 셸입니다.

### playground — [repo](https://github.com/AzuraLight/vue-force-network-map-playground)
위 세 라이브러리를 실제로 조합하는 데모입니다: NCS 학습자 맵, 역량 로드맵, 적합도 차트, iframe 탐색기.

## 개발 도구

### tourcast — [repo](https://github.com/AzuraLight/tourcast)
웹 앱 시연 영상을 코드로 만드는 CLI 입니다(Demo-as-Code). 현재 v0.2.0 입니다.
- YAML 로 투어를 작성하면 Playwright 가 앱을 돌고, 합성 커서와 카메라 줌·딤으로 MP4 를 녹화합니다
- 제품이 바뀌면 다시 찍는 대신 다시 생성합니다
- `check`(브라우저 없이 검증) · `probe`(대상 앱 실측) · `init`(스캐폴드) 명령
- 기술: Python 3.11 · Playwright

### swagger-mcp
Swagger/OpenAPI 를 AI 에이전트가 직접 조회하게 하는 MCP 서버입니다. 엔드포인트·모델 목록과 상세,
키워드 검색 도구를 제공합니다. Swagger UI 주소를 넣으면 실제 스펙 주소를 자동으로 찾습니다.

### recommend-embed — [repo](https://github.com/AzuraLight/recommend-embed)
외부 스크립트 없이 붙이는 임베드형 위젯 패턴입니다. 호스트는 버튼 + iframe + 짧은 브릿지만
넣고, UI 는 모두 iframe 안의 Vue 앱이 그립니다. 둘은 네임스페이스가 붙은 postMessage 로 통신합니다.
JS 라이브러리를 넣을 수 없는 공공기관 페이지를 위해 설계했습니다.
