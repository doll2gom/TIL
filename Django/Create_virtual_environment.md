# Create virtual environment

가상환경 설정 가이드

## 1. 가상환경 생성

- `$ python3 -m venv venv`

마지막에 작성하는 `venv`는 가상환경 이름으로 수정이 가능하지만 모든 개발자들이 암묵적으로 통일한다.

---

## 2. 가상환경 활성화

VSCode 상에서 1번 절차인 가상환경을 생성 명령을 입력한 후 `cmd + shift + P`를 눌러 방금 생성된 인터프리터를 선택한다.

그리고 터미널을 껐다가 다시 열면 아래의 명령어가 자동으로 입력 및 실행된다.

- `$ source venv/Script/activate`<sup>탭키로 자동완성</sup>

---

## 3. Django 설치

- `$ pip install django==3.2.18`

[설치 버전 : 3.2.18](https://static.djangoproject.com/img/release-roadmap.4cf783b31fbe.png)
마지막 숫자 18은 틀려도 되지만
230320 현시점을 기준으로 최신버전이 아닌 [LTS(Long Term Support)](https://ko.wikipedia.org/wiki/%EC%9E%A5%EA%B8%B0_%EC%A7%80%EC%9B%90_%EB%B2%84%EC%A0%84)버전 3.2를 설치한다.

---

## 4. 의존성 파일 생성

- ` $ pip freeze > requirement.txt`

나의 가상환경에 설치된 내역을 txt 파일로 작성\
패키지 설치시 반복적으로 진행한다

`>` 기호는 cli명령어로 `a > b`는 a를 b에 작성함을 뜻한다.
`requirement`의존성 파일명은 암묵적으로 통일한다.

---

### `+` github 사용을 위한 설정

> github에 push해야하는 경우 필요한 절차(협업)

1. git init
2. `.gitignore` 파일 생성

   - [gitignore io 생성 사이트](https://www.toptal.com/developers/gitignore)
   - git에 commit할 때는 이런 환경설정<sub>설치된 프로그램 버전 등 잡다한 내용</sub>자체를 포함하지 않는다. &rArr; `.gitignore`에 담기는 내용

3. git add
4. git commit
5. git push

---

### `+` pair 사용자가 해야할 설정

> github를 통해 받아온 설치목록으로 가상환경 일치시키기

1. pull
2. 가상환경 생성 + 활성화
3. 의존성 파일 목록 설치

`$ pip install -r requirement.txt`

---

## 5. django 서버 실행

- `$ python3 manage.py renserver`

`manage.py`파일과 동일한 경로에서 다음의 명령어를 실행한다.

터미널 창에서 보이는 링크를 `cmd`를 누른 상태에서 클릭
로켓이 발사되는 화면을 확인한다.
