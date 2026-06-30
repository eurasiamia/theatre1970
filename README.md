# theatre1970

1970년대 서울 소극장(small theatre) 연구를 위한 데이터 저장소입니다. ARKO(한국문화예술위원회) 오픈데이터, 구술채록 자료, 인물/공연 관계망, 온톨로지 정의 파일 등을 정리합니다.

## 폴더 구성

### 원자료 / 오픈데이터
- `arko_opendata_1970s.xlsx` — ARKO 오픈데이터에서 추출한 1970년대 공연 기록
- `arko-open_daarts_중복표기.xlsx` — ARKO/DAARTS 데이터 간 중복 표기 정리
- `공연예술컬렉션_정리_2.xlsx` — 공연예술 컬렉션 정리본

### 소극장 대상자원
- `1970년대 소극장_대상자원.xlsx` — 전체 대상자원 원본 (대용량, 78MB)
- `1970년대 소극장_대상자원_ver.1.xlsx` — 정리본 v1
- `small theatre.xlsx` — 소극장 기초 목록

### 인물 관계망 (Person Network)
- `arko_person_network.xlsx` / `arko_person_network_filtered.xlsx` — 인물 관계망 원본 및 필터링본
- `arko_person_network_관계세부추가.xlsx` — 관계 세부 정보 추가본
- `arko_person_network_채록문번호수정.xlsx` — 채록문 번호 수정본
- `동명이인.xlsx` — 동명이인 식별 및 구분 작업
- `아르코_소극장_중복인물_관계목록.xlsx` / `아르코-소극장_중복인물_관계목록_OT추가.xlsx` — 중복 인물 관계 목록 (OT: oral history 추가)
- `구술채록_관계정리.xlsx` — 구술채록 기반 관계 정리

### 온톨로지 / 시맨틱 데이터
- `theater_v2.owl` — 소극장 도메인 온톨로지(OWL)
- `small_theatre_ontology_2026.xlsx`, `small_theatre_ontology_ver.1~3.xlsx` — 온톨로지 정의 작업본(버전별)
- `small_theatre_semanticdate_2026*.xlsx` — 시맨틱 데이터 변환 작업본(버전별, 수정본 포함)
- `small_theatre_2026_nodes.xlsx` / `small_theatre_2026_links.xlsx` — 네트워크 그래프용 노드/링크 데이터

### 아카이브 / 시각자료
- `small_theatre_archive_13.html` — 소극장 아카이브 페이지 스냅샷
- `1970s_seoul_theatre_map_v3.png` — 1970년대 서울 소극장 지도 시각화

### 제외된 파일 (`.gitignore`)
- `oral_history_변환용.txt` — 구술채록 원문 변환용 텍스트 (195MB, GitHub 100MB 제한 초과로 저장소에서 제외)
- `.claude/settings.local.json` — 로컬 개발 환경 설정 (개인 설정이라 제외)

## 데이터 관리 메모

- 파일명에 버전(`ver.1`, `v2`, `v3`) 또는 수정 표시(`_수정`)가 있는 경우, 가장 최근 버전이 최신 작업본입니다.
- `oral_history_변환용.txt`는 용량이 커서 저장소에 포함되지 않으므로, 필요 시 로컬 또는 별도 저장소(Git LFS 등)에서 관리하세요.
- 대용량 xlsx 파일(`1970년대 소극장_대상자원.xlsx`, 78MB)은 GitHub 권장 용량(50MB)을 초과하므로, 향후 더 커질 경우 Git LFS 도입을 검토하세요.

## 원격 저장소

https://github.com/eurasiamia/theatre1970
