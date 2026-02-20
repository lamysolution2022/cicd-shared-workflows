# 운영 런북 (success/block/recover) v1

- SubmissionId: `6b70ea428f9248d28b92d97b77527ead`
- PlanId: `fdec7f53-2374-4857-806e-5408fe2548f0`
- 적용 대상 워크플로: `.github/workflows/api-self-runner-deploy-governance.yml`

## 1) 공통 사전 점검
1. `NEXUS_NUGET_USERNAME`, `NEXUS_NUGET_PASSWORD` 시크릿 존재 확인
2. `runs-on` 정책 확인
   - 기본: `[self-hosted, windows, api-server]`
   - 장애 리허설: `windows-latest`
3. Gate 선행 통과 확인
   - contract, performance, observability, release governance

## 2) success 모드 운영 절차
- 입력: `rehearsal_mode=success`, `self_runner_available=false/true`
- 기대 결과:
  - integrated-gates 성공
  - 배포 job 성공
  - fallback 증빙 JSON 생성
- 운영 확인 포인트:
  - run URL: `https://github.com/lamysolution2022/cicd-shared-workflows/actions/runs/22176929546`
  - fallback job URL: `https://github.com/lamysolution2022/cicd-shared-workflows/actions/runs/22176929546/job/64127913936`

## 3) block 모드 운영 절차
- 입력: `rehearsal_mode=block`
- 기대 결과:
  - `Block by quality profile rehearsal` 단계에서 즉시 차단(exit 97)
  - 배포 job 미실행(skipped)
- 운영 확인 포인트:
  - run URL: `https://github.com/lamysolution2022/cicd-shared-workflows/actions/runs/22176929577`
  - 차단 step URL: `https://github.com/lamysolution2022/cicd-shared-workflows/actions/runs/22176929577/job/64127890587`

## 4) recover 모드 운영 절차
- 입력: `rehearsal_mode=recover`
- 기대 결과:
  1. 첫 배포 단계 강제 실패(simulate_fail_code=19)
  2. `Recovery deploy after forced failure` 단계 자동 실행
  3. 최종 run 성공 및 복구 증빙 JSON 생성
- 운영 확인 포인트:
  - recover run URL: `https://github.com/lamysolution2022/cicd-shared-workflows/actions/runs/22207139912`
  - fallback/recovery job URL: `https://github.com/lamysolution2022/cicd-shared-workflows/actions/runs/22207139912/job/64233512531`

## 5) 장애 대응/에스컬레이션
1. Gate 실패 시 배포 즉시 중지, 실패 step URL 수집
2. 10분 이내 재현 불가 시 Platform On-call에 에스컬레이션
3. 30분 내 임시 우회 금지, 원인 분석 후 재실행
4. 모든 재시도는 Coordination 채널에 run URL/step 근거 첨부
