# CI/CD 공용 리포 아키텍처 정의서 v1

- PlanId: `24cc616d-c05e-476b-863d-b18c79d083da`
- SubmissionId: `7268e615cec1408ab121db5a3306ef9a`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 범위 정의
- 공용 리포 목적: 다수 소비 리포에서 공통으로 사용하는 CI/CD 재사용 워크플로우 표준 제공
- 포함 범위:
  - Build 템플릿 (`workflow_call`)
  - Test 템플릿 (`workflow_call`)
  - Deploy 템플릿 (`workflow_call`, 환경 승인 게이트 포함)
  - Security Scan 템플릿 (`workflow_call`, SAST/Dependency/Secret scan)
  - 소비 리포 연동 가이드/버전 고정 규칙
- 제외 범위:
  - 서비스별 애플리케이션 배포 스크립트 세부 구현
  - 비표준 런너 자체 프로비저닝

## 2) 버전 전략
- 버전 체계: SemVer (`MAJOR.MINOR.PATCH`)
- 참조 규칙:
  - 운영 기본: `vMAJOR` 태그 고정 사용 (예: `@v1`)
  - 안정성 검증 환경: `vMAJOR.MINOR` 또는 릴리즈 태그 사용 (예: `@v1.2.0`)
  - 긴급 핫픽스: `PATCH` 릴리즈 후 `vMAJOR` 재포인팅
- 호환성 원칙:
  - `MAJOR` 변경 시 브레이킹 체인지 허용, 마이그레이션 가이드 필수
  - `MINOR/PATCH`는 하위 호환 유지

## 3) 권한 모델
- Role 분리:
  - Maintainer: 워크플로우 수정/릴리즈 승인
  - Reviewer: 변경 검토 및 보안 정책 점검
  - Consumer: 템플릿 사용, 파라미터 설정만 수행
- 브랜치 보호:
  - `main`: 직접 push 금지, PR 필수
  - 최소 승인 2인 (CI/CD Owner 1 포함)
  - 필수 체크: workflow lint, security baseline, release note check
- 비밀정보 원칙:
  - 리포 내 하드코딩 금지
  - `secrets: inherit` 또는 환경별 조직 시크릿 사용

## 4) 브랜치/태그/릴리즈 규칙
- 브랜치 전략:
  - `main`: 릴리즈 준비 완료 코드만 병합
  - `release/vX.Y`: 릴리즈 안정화
  - `hotfix/*`: 긴급 수정
- 태그 규칙:
  - 릴리즈 태그: `vX.Y.Z`
  - 메이저 포인터: `vX`
- 릴리즈 게이트:
  1. 테스트/보안검사 통과
  2. 소비 리포 스모크 검증 통과
  3. 롤백 시나리오 리허설 통과
  4. Coordination 채널 승인 기록

## 5) SLA/보안 정책 정합성
- 배포 중 무단 다운타임 금지: Blue/Green 또는 canary 전환 절차 강제
- 취약점 정책: High 이상 검출 시 배포 차단
- 감사 추적: 모든 배포/승인/롤백 이벤트를 워크플로우 로그와 릴리즈 노트에 기록

## 6) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
