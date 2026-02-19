# API 배포 검증 리포트 v1

- SubmissionId: `0c3f2c5689a94ba1b7f9ce6650a53b28`
- PlanId: `a74a37ef-c39c-40b5-bb7d-7f1cad2cdf28`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 산출물 경로
- 워크플로: `.github/workflows/api-self-runner-deploy-governance.yml`
- 게이트 문서: `docs/runner/api-self-runner-gate-integration-v1.md`
- 리허설 로그: `artifacts/runner/api-self-runner-fallback-rehearsal-2026-02-19.json`

## 2) 검증 근거
- 성공 run URL: `TBD`
- 차단 run URL: `TBD`
- 차단 step 링크: `TBD`

## 3) 검증 요약
- 최소권한/비밀 마스킹 적용
- Nexus NuGet 강제 복원 정책 적용
- 계약·성능·관측성·릴리스 거버넌스 게이트 통합
- self-runner 장애 시 hosted fallback 리허설 로그 생성
