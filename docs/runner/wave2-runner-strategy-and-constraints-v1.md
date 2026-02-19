# 커스텀 액션 + 러너 운영 전략 결정표 v1

- SubmissionId: `8729c454979a476893707d5ab5b11572`
- PlanId: `02716e20-3c29-4973-b8f3-889e1b3573f0`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 러너 전략 결정표

| 구분 | 기본 러너 | 대체 러너 | NuGet 소스 | 적용 조건 |
|---|---|---|---|---|
| API 서버 배포 | Windows self-runner(`self-hosted, windows, api-server`) | Windows hosted(`windows-latest`) | 사내 Nexus NuGet | self-runner 정상 시 기본 사용 |
| 리허설/복구 | Windows self-runner | Windows hosted fallback | 사내 Nexus NuGet | self-runner 장애/불가용 시 fallback |
| 정책 검증 게이트 | GitHub hosted(`ubuntu-latest`) | 없음 | 해당 없음 | 정책 위반 차단 전용 |

## 2) 금지 조건
- Linux/macOS 러너에서 API 서버 배포 실행 금지
- 공용 패키지 소스를 GitHub Packages/public NuGet로 우회 사용 금지
- self-runner 장애를 무시한 무조건 배포 강행 금지
- 승인 없는 권한 확장(`contents: write`, `actions: write`) 금지
- 시크릿 하드코딩 금지(토큰/계정/피드 자격증명 포함)

## 3) 운영 원칙
- 배포 구현은 GitHub 커스텀 액션으로 통일
- API 서버 배포 기본 러너는 Windows self-runner 유지
- fallback은 장애 리허설 및 비상 복구 시나리오에 한정
- Owner 직접 소통 금지, Coordination 단일 채널
