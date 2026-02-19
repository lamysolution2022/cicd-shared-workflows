# CI/CD 공용 워크플로우 원격 실행 증적 v1

- PlanId: `24cc616d-c05e-476b-863d-b18c79d083da`
- SubmissionId: `7268e615cec1408ab121db5a3306ef9a`
- 요청 ID: `04e5d338-8a8f-454b-bf73-59f7d786cdb5`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 소비 리포 @v1 연동 적용
- 소비 리포: `https://github.com/lamysolution2022/cicd-consumer-sample-7268`
- 연동 파일: `.github/workflows/consumer-cicd-remote-validation.yml`
- 연동 방식: `uses: lamysolution2022/cicd-shared-workflows/.github/workflows/<template>.yml@v1`

## 2) 원격 실행 증적 (GitHub Actions)
| 구분 | Run URL | 결과 | 비고 |
|---|---|---|---|
| 성공 시나리오 | `https://github.com/lamysolution2022/cicd-consumer-sample-7268/actions/runs/22169587786` | success | deploy 성공, rollback skipped |
| 실패-롤백 시나리오 | `https://github.com/lamysolution2022/cicd-consumer-sample-7268/actions/runs/22169590188` | failure | deploy 실패 후 rollback 실행 성공 |

### 실패-롤백 상세 증적
- deploy job URL: `https://github.com/lamysolution2022/cicd-consumer-sample-7268/actions/runs/22169590188/job/64104463321` (failure)
- rollback job URL: `https://github.com/lamysolution2022/cicd-consumer-sample-7268/actions/runs/22169590188/job/64104470519` (success)

## 3) 릴리즈 태그/포인터 확정
- 공용 리포: `https://github.com/lamysolution2022/cicd-shared-workflows`
- 릴리즈 태그: `v1.0.0`
- 릴리즈 URL: `https://github.com/lamysolution2022/cicd-shared-workflows/releases/tag/v1.0.0`
- 메이저 포인터: `v1` (tag push 완료)

## 4) 산출물 경로
- `docs/cicd-shared-repo-architecture-v1.md`
- `.github/workflows/shared-build.yml`
- `.github/workflows/shared-test.yml`
- `.github/workflows/shared-security-scan.yml`
- `.github/workflows/shared-deploy.yml`
- `docs/cicd-shared-workflow-validation-report-v1.md`
- `docs/cicd-shared-operations-transition-guide-v1.md`
- `docs/cicd-shared-remote-run-evidence-v1.md`

## 5) 운영 원칙
- Coordination 단일 채널
- Owner 직접 소통 금지
