# 커스텀 액션 스펙 v1 (I/O/실패코드/권한)

- 액션 경로: `.github/actions/deploy-api-server/action.yml`
- 목적: Nexus NuGet 기반 API 서버 배포 표준화

## 1) Input 스펙
- `package_id` (필수): 배포 대상 NuGet 패키지 ID
- `package_version` (필수): 배포 대상 버전
- `nexus_source_name` (선택, 기본 `nexus-internal`): NuGet source 별칭
- `nexus_source_url` (필수): 사내 Nexus NuGet feed URL
- `nexus_username` (선택): Nexus 계정
- `nexus_password` (선택): Nexus 토큰/비밀번호
- `deploy_path` (필수): 배포 출력 경로
- `runner_mode` (선택): `self-hosted-windows` / `hosted-fallback`
- `simulate_fail_code` (선택, 기본 `0`): 실패 리허설 코드

## 2) Output 스펙
- `deploy_status`: `deployed` 또는 `blocked`
- `exit_code`: `0` 또는 실패 코드 문자열

## 3) 실패 코드 표준
- `10`: 필수 input 누락
- `11`: Nexus source 구성 실패
- `12`: 패키지 복원 실패(향후 확장)
- `13`: 배포 파일 반영 실패(향후 확장)
- `90`: 거버넌스 정책 위반 차단(워크플로 게이트)

## 4) 권한 스펙(최소권한)
- 워크플로 기본 권한: `contents: read`
- 금지: `contents: write`, `actions: write`, 광범위 토큰 권한
- 시크릿은 GitHub Secrets/Variables로만 주입

## 5) Nexus NuGet 준수
- 공용 패키지 피드는 사내 Nexus NuGet으로 고정
- 외부 public 피드 직접 사용 금지
- 자격증명은 런타임 주입, 저장소 하드코딩 금지
