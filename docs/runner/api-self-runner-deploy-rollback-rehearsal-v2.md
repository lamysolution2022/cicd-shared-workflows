# API Self-Runner Deploy/Rollback Rehearsal v2

- SubmissionId: `0c3f2c5689a94ba1b7f9ce6650a53b28`
- PlanId: `a74a37ef-c39c-40b5-bb7d-7f1cad2cdf28`

## 리허설 시나리오
1. 성공: `rehearsal_mode=success`, `self_runner_available=false`
2. 차단: `rehearsal_mode=block`, `self_runner_available=false`
3. 복구: `rehearsal_mode=recover`, `self_runner_available=false`

## 기대 동작
- 성공: 게이트 통과 후 fallback 배포 성공
- 차단: 게이트 단계에서 정책 차단(exit 97)
- 복구: 강제 실패(simulate_fail_code=19) 후 recovery deploy 성공

## 증적
- 워크플로: `.github/workflows/api-self-runner-deploy-governance.yml`
- fallback artifact: `artifacts/runner/api-self-runner-fallback-rehearsal-2026-02-19.json`
- run URL:
  - success: `TBD`
  - block: `TBD`
  - recover: `TBD`
