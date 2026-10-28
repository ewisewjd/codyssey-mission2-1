# 01. 설치와 첫 실행

## 요구 환경

- Python 3.10 이상
- Git
- 외부 Python 패키지 설치 불필요(표준 라이브러리 사용)

## 최신 코드 받기

프로젝트 폴더에서 로컬 변경 사항을 먼저 확인한다.

```bash
git status
git pull
```

변경 중인 파일이 있다면 내용을 확인하고 보존한 다음 업데이트한다.

## 도움말과 첫 실행

```bash
python3 --version
python3 -m budget_app --help
python3 -m budget_app category list
python3 -m budget_app list --limit 10
```

처음 실행하면 기본 `data/` 폴더와 세 개의 JSONL 파일이 만들어진다. 거래가 없으면 목록에 거래 내역이 없다고 표시된다.

## 별도 데이터 폴더 사용

전역 옵션 `--data-dir`은 명령어보다 앞에 둔다.

```bash
python3 -m budget_app --data-dir ./sample_data list
python3 -m budget_app --data-dir ./sample_data add
```

이렇게 하면 기본 `data/`와 분리된 시험용 데이터를 사용할 수 있다.

## 실행 위치

명령은 저장소 루트에서 실행한다. 루트가 아닌 위치에서 실행하면 Python이 `budget_app` 패키지를 찾지 못할 수 있다.
