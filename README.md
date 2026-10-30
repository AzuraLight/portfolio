# 이현도 · Frontend Engineer

Vue 3 · TypeScript 기반 웹 프론트엔드 개발자입니다. 교육 서비스의 관리자 화면, 교재 저작 도구,
수업 플레이어, 공공 추천 시스템 포털을 만들고 운영했습니다. 업무 중에 반복되는 일은 VS Code
확장과 개발 도구로 직접 만들어 오픈소스로 공개하고 있습니다.

- GitHub: [@AzuraLight](https://github.com/AzuraLight)
- 소속: 코드넛 (2026)

> 이 저장소는 포트폴리오 문서만 담고 있습니다. 회사 프로젝트의 소스 코드는 포함하지 않으며,
> 고객사 내부 정보(주소 · 인프라 · 계정)는 적지 않았습니다.

---

## 기술 스택

| 분야 | 사용 기술 |
| --- | --- |
| 언어 | TypeScript, JavaScript, Python, SQL |
| 프레임워크 | Vue 3 (Composition API · `<script setup>`), React 19 |
| 상태 · 데이터 | Pinia, TanStack Query, vue-i18n, Axios |
| 빌드 · 모노레포 | Vite, pnpm workspace, Turborepo |
| 스타일 | Tailwind CSS v4, 디자인 토큰(Figma 변수 → CSS 시맨틱 토큰) |
| 시각화 | D3 (force · radial), Chart.js, SVG |
| 에디터 | TipTap, CodeMirror 6 |
| API 계약 | OpenAPI, openapi-typescript, swagger-typescript-api |
| 품질 | Vitest, Playwright, Storybook, oxlint · ESLint, commitlint, husky |
| 배포 | Docker, Kubernetes(NKS), Bitbucket Pipelines, GitLab CI, 온프렘 httpd 패키징 |
| 도구 개발 | VS Code Extension API, Webview, MCP(Model Context Protocol) |

---

## 회사 프로젝트

| 프로젝트 | 무엇 | 역할 | 기간 |
| --- | --- | --- | --- |
| [티처스 클래스](projects/company/teachers-class.md) | 교재 에디터 · 관리자 · 강사용 수업 서비스 모노레포 | 프론트엔드 단독 개발 (설계 · 구현 · 배포) | 2026.09 – 2026.10 |
| [HRD-Net 훈련추천시스템 포털](projects/company/hrd-net-portal.md) | 한국산업인력공단 훈련 추천 백오피스 + 학습자 진단·추천 화면 | 프론트엔드 단독 개발 | 2026.06 – 2026.10 |
| [매쓰캔버스](projects/company/mathcanvas.md) | 비상교육 수학 수업 플랫폼의 관리자 · 사용자 화면 | 관리자 프론트엔드 주 개발, 사용자 화면 기능 개발 | 2026.04 – 2026.09 |
| [해봄 AI 플랫폼](projects/company/haebom.md) | 지역 문제 ↔ 해결 기업 카드 매칭 플랫폼의 공개 화면 · 관리자 화면 | 프론트엔드 저장소 개발 | 2026.08 – 2026.09 |

## 개인 오픈소스

| 프로젝트 | 무엇 | 링크 |
| --- | --- | --- |
| **Gitline** | VS Code 하단 패널용 Git 커밋 그래프 (v1.2.0) | [repo](https://github.com/AzuraLight/gitline) |
| **BindB** | VS Code 안의 Database IDE: PostgreSQL · MySQL · SQLite · H2 | [repo](https://github.com/AzuraLight/bindb) |
| **tourcast** | YAML 시나리오로 웹 앱 시연 영상을 자동 녹화하는 CLI (Demo-as-Code) | [repo](https://github.com/AzuraLight/tourcast) |
| **OpenAPI Explorer** | 에디터 안에서 Swagger/OpenAPI 를 탐색 · 검색 · 호출하는 확장 | [repo](https://github.com/AzuraLight/openapi-explorer) |
| **Midnight ERD** | SQL DDL 을 인터랙티브 ERD 로 그리는 VS Code 확장 | [repo](https://github.com/AzuraLight/midnight-erd) |
| **Terminal CD Click** | 터미널 출력의 디렉터리를 클릭해 `cd` 하는 확장 | [repo](https://github.com/AzuraLight/terminal-cd-click) |
| **vue-force-network-map** | D3 force 기반 Vue 3 네트워크 그래프 컴포넌트 | [repo](https://github.com/AzuraLight/vue-force-network-map) |
| **vue-bullseye-chart** | 값(0~1)을 동심원에 배치하는 Vue 3 불스아이 차트 | [repo](https://github.com/AzuraLight/vue-bullseye-chart) |
| **vue-safe-iframe** | sandbox · origin 검증 · 타임아웃을 갖춘 iframe 컴포넌트 | [repo](https://github.com/AzuraLight/vue-safe-iframe) |
| **recommend-embed** | 의존성 없는 스니펫으로 띄우는 임베드형 추천 위젯 | [repo](https://github.com/AzuraLight/recommend-embed) |

상세 설명과 그 밖의 도구(Cairn, swagger-mcp, Notion MD, Todo Kanban 등)는
[개인 프로젝트 문서](projects/personal/README.md)에 정리했습니다.

---

## 일하는 방식

- **계약 먼저.** 서버 OpenAPI 명세에서 타입을 생성하고, 화면은 생성 타입만 씁니다. 명세가
  바뀌면 타입 검사가 먼저 깨지게 만듭니다.
- **경계를 코드로 지킵니다.** 독립 모듈은 import 방향을 테스트와 린터로 검사합니다.
- **디자인은 토큰으로.** Figma 변수를 원시 → 시맨틱 토큰으로 옮겨 다크 모드와 테마를 같은 구조로 다룹니다.
- **반복 작업은 도구로.** 업무에서 반복되는 일(Swagger 조회, DB 조회, Git 이력, 시연 영상)은 확장 · CLI · MCP 서버로 만들어 공개합니다.
