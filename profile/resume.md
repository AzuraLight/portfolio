# 이현도

> 웹 프론트엔드 개발자 · 경력 약 3년
>
> 저작 도구와 관리자 화면처럼 복잡한 업무 화면을 설계부터 배포까지 혼자 완성하는 Vue · TypeScript 개발자.

| 항목 | 내용 |
| --- | --- |
| 직무 | 웹 프론트엔드 (Vue · React · TypeScript) |
| 경력 | 약 3년 — ㈜코드넛 재직 중, 토피도㈜ 2년 4개월 |
| GitHub | [github.com/AzuraLight](https://github.com/AzuraLight) |
| 포트폴리오 | [azuralight.github.io/portfolio](https://azuralight.github.io/portfolio/) |

## 소개

- 교재 에디터, 수업 플레이어, 공공 추천 시스템 포털, 관리자 CMS 등 **업무용 웹 애플리케이션** 개발
- 최근 7개월간 고객사 프로젝트 4건 중 2건의 **프론트엔드 단독 개발** (설계 · 구현 · 테스트 · 배포)
- OpenAPI 타입 생성, 경계 테스트, ADR 로 **계약과 결정을 코드와 문서로 고정**하는 방식 선호
- Java · Spring 백엔드 경험을 바탕으로 백엔드 개발자와 API 설계부터 함께 논의
- 반복 업무를 VS Code 확장 · CLI · MCP 서버로 만들어 **오픈소스 공개** (Gitline, BindB, tourcast 등)

## 기술 스택

| 분류 | 기술 |
| --- | --- |
| Frontend | TypeScript, Vue 3, Pinia, TanStack Query, vue-i18n, React 19 |
| Styling | Tailwind CSS v4, 디자인 토큰, Figma 구현, 반응형 |
| Editor · Visualization | CodeMirror 6, TipTap, D3, Chart.js |
| Build · Test | Vite, pnpm, Turborepo, Vitest, Playwright, Storybook |
| API · DevOps | OpenAPI, openapi-typescript, Docker, Kubernetes, Bitbucket Pipelines, GitLab CI |
| Backend | Java, Spring Boot, Spring WebFlux, MyBatis, MySQL, Oracle, PostgreSQL |

## 경력

### ㈜코드넛 · 2026.04 ~ 재직 중

웹 개발 · 사원 — 교육 · 공공 고객사의 웹 프론트엔드 개발

#### 티처스 클래스 — 교재 에디터 · 관리자 · 수업 서비스 (2026.09 ~ 2026.10)

교사가 KIT(교구 + 차시 교재)로 수업하는 서비스의 관리자 · 에디터 · 강사용 앱 · 수업 Player 모노레포

| 항목 | 내용 |
| --- | --- |
| 역할 | 프론트엔드 단독 개발 (커밋 520여 건) |
| 기술 | Vue 3.5, TypeScript, pnpm + Turborepo, Pinia, TanStack Query, CodeMirror 6, Vitest, Playwright |

- 앱 2개 + 공통 · 렌더러 · API 패키지로 모노레포 설계, Feature-Sliced Design 적용, 설계 결정 17건 ADR 기록
- 교재 렌더러를 독립 패키지로 분리해 에디터 미리보기와 실제 수업 화면의 렌더링 불일치 제거
- 레이아웃 13개 묶음을 선언형으로 정의 — 폼 · 글자 수 한도 · 가이드 페이지를 선언에서 자동 생성
- 편집 잠금 · 저장 충돌 해결 · 판 기록 · 새로고침 복원으로 다중 편집 시 내용 유실 방지
- CodeMirror 6 기반 JSON 편집기 구현 (스키마 자동완성 · 인라인 오류 · 빠른 고침)
- 수업 Player 를 애드온 구조로 설계 (필기 · 타이머 · 퀴즈 · 참고자료 · 메모), Docker · Kubernetes 배포

#### HRD-Net 훈련추천시스템 포털 — 한국산업인력공단 (2026.06 ~ 2026.10)

AI 훈련 추천 시스템의 백오피스와 학습자 진단 · 추천 화면

| 항목 | 내용 |
| --- | --- |
| 역할 | 프론트엔드 단독 개발 (커밋 420여 건) |
| 기술 | Vue 3.5, TypeScript, Vite, Pinia, Tailwind v4, Chart.js, D3 |

- 사전역량진단 → 결과 → 추천 → 지식맵(force 그래프) 학습자 흐름 구현, 기관 사이트용 iframe 임베드 지원
- 학습자 모듈을 인터페이스 주입 구조로 분리하고 양방향 import 금지를 경계 테스트로 검사
- 대시보드(KPI · 도넛 · 시간대 히트맵), 기관 · 학습자 · 콘텐츠 관리, 엑셀 일괄 등록 구현
- 게이트웨이 로그 뷰어 구현 — 요청 단위 · 엔드포인트 집계, mtime 기준 캐시
- 내부망 HTTP 메서드 차단 대응, 온프렘(JWS/httpd) 배포 패키지 · 설치 가이드 제작
- 테스트 76 → 245개 확대, ESLint 도입

#### 매쓰캔버스 — 비상교육 수학 수업 플랫폼 (2026.04 ~ 2026.09)

| 항목 | 내용 |
| --- | --- |
| 역할 | 관리자 프론트엔드 주 개발 (커밋 220여 건), 사용자 화면 기능 개발 (커밋 120여 건) |
| 기술 | Vue 3, TypeScript, Pinia, TanStack Query, TipTap, openapi-typescript |

- 통합 SSO 연동, 통합회원 전환에 맞춘 사용자 관리 화면 개편과 개인정보 노출 최소화
- TipTap 리치텍스트 에디터를 워드형으로 개편, 초안 로컬 보존 · 이탈 경고로 편집 유실 방지
- 데이터 이관 화면 구현 (작업 실행 · 상태 폴링 · 재시작 · 파이프라인형 이력)
- 신규 백엔드 스펙으로 API 마이그레이션, openapi-typescript 생성 타입으로 전환
- 폐쇄망(신규 패키지 설치 불가) 환경에서 기존 의존성만으로 구현, 종료 시 인수인계 문서 작성

#### 해봄 AI 플랫폼 — 이티랩 지역 문제 매칭 플랫폼 (2026.08 ~ 2026.09)

| 항목 | 내용 |
| --- | --- |
| 역할 | 프론트엔드 저장소 개발 (커밋 230여 건) |
| 기술 | React 19, TypeScript, Vite, TanStack Query, react-router 7, Tailwind v4 |

- 모노레포의 사용자 화면을 독립 저장소로 분리, REST 계약만 공유하는 구조로 정리
- 공개 화면(무한 스크롤 목록 · 행정동 폴리곤 지도 · 등록 흐름)과 관리자 화면(검수 · 매칭 · 권한별 라우트) 구현
- 좌표 동 단위 표시 · 원문 비공개 등 개인정보 원칙을 화면 설계에 반영

### 토피도㈜ · 2023.06 ~ 2025.09 (2년 4개월)

사원 — 공공 · 금융 SI 프로젝트의 프론트엔드 개발과 백엔드 보조

- ESB 관리 콘솔 프론트엔드 전반 개발 (Vue 3 · Vuex · Chart.js)
- 농협 세금계산서 프로젝트 프론트엔드 개발, 백엔드 개발 보조
- 한국도로공사 데이터 안심구역 프로젝트 백엔드 소스 수정
- 경찰청 · 법무부 KICS 모니터링 에이전트 점검
- Spring WebFlux · MVC 비동기 처리 프로토타입, Vue 2 · CoreUI / Vuetify 관리자 템플릿 제작

## 개인 프로젝트

| 프로젝트 | 내용 | 링크 |
| --- | --- | --- |
| Gitline | VS Code 커밋 그래프 확장 (v1.2.0) — SVG 레인 그래프, 가상 스크롤, 멀티 저장소 | [repo](https://github.com/AzuraLight/gitline) |
| BindB | VS Code Database IDE — 4종 DB, 스키마 기반 자동완성, 스트리밍 결과 그리드 | [repo](https://github.com/AzuraLight/bindb) |
| tourcast | YAML 시나리오로 웹 앱 시연 영상을 자동 녹화하는 CLI (Python · Playwright) | [repo](https://github.com/AzuraLight/tourcast) |
| OpenAPI Explorer | 에디터 안에서 Swagger 탐색 · 호출, TS 타입 · 호출 코드 생성 | [repo](https://github.com/AzuraLight/openapi-explorer) |
| Vue 3 라이브러리 3종 | force 네트워크 맵 · 불스아이 차트 · 안전한 iframe — 실무 코드를 일반화 | [repo](https://github.com/AzuraLight/vue-force-network-map) |

## 교육

| 기간 | 내용 |
| --- | --- |
| 2022.10 ~ 2023.04 | 애드인에듀 — 리액트와 스프링부트를 활용한 자바 풀스택 개발자 양성과정 (Elasticsearch 로그 분석 · 시각화 포함) |

## 학력

| 기간 | 내용 |
| --- | --- |
| 2010.03 ~ 2020.02 | 충북대학교 경제학과 졸업 |

## 자격 · 어학

| 취득 | 내용 |
| --- | --- |
| 2024.02 | OPIc Intermediate Mid 1 |
| 2023.04 | 정보처리기사 필기 합격 |
| 2021.10 | TOEIC 800 |
| 2017.09 | 재경관리사 (국가공인) |
| 2014.06 | 회계관리 2급 (국가공인) |
| 2003.06 | 정보처리기능사 |

## 기타

| 항목 | 내용 |
| --- | --- |
| 병역 | 육군 병장 만기 전역 (2010.12 ~ 2012.09) |
| 운전면허 | 1종 보통 |
