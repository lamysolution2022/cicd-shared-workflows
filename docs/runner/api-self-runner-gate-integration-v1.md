# API 배포 게이트 통합 문서 v1

- SubmissionId: `0c3f2c5689a94ba1b7f9ce6650a53b28`
- PlanId: `a74a37ef-c39c-40b5-bb7d-7f1cad2cdf28`
- 작성일: 2026-02-19
- 작성자: Platform Engineer (CI/CD Owner)

## 1) 워크플로 개요
- 파일: `.github/workflows/api-self-runner-deploy-governance.yml`
- 기본 배포 러너: `runs-on: [self-hosted, windows, api-server]`
- fallback 리허설 러너: `windows-latest`
- 권한: 모든 job `permissions: contents: read` 최소화

## 2) Nexus NuGet 강제 정책
- `nuget.config`를 런타임 생성하고 `<clear />`로 타 소스 제거
- `nexus-internal`만 허용 + `packageSourceMapping`으로 전체 패키지 Nexus 강제
- `dotnet nuget add source` 인증 주입(Secrets)
- 민감정보 마스킹: `::add-mask::${{ secrets.NEXUS_NUGET_USERNAME }}`, `::add-mask::${{ secrets.NEXUS_NUGET_PASSWORD }}`

## 3) 통합 게이트
1. 계약 게이트: `tests/architecture`, `tests/compatibility`
2. 성능 게이트: 워크플로 인라인 검증 로직(`messaging-load-test-results` vs `messaging-capacity-thresholds`)
3. 관측성 게이트: `tools/observability/retrycount_guard.py`
4. 릴리스 거버넌스 게이트: `tools/release/release_governance_gate.py`

## 4) 차단 정책
- `rehearsal_mode=block` 시 `Block by quality profile rehearsal` step에서 강제 차단
- 차단 코드: `97`

## 5) 운영 원칙
- API 서버 배포 기본 경로는 Windows self-runner
- self-runner 장애 시 hosted fallback 리허설 로그 필수
- Owner 직접 소통 금지, Coordination 단일 채널
