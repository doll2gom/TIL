# Git/ GitHub

## 개요

    깃은 소프트웨어
    깃헙은 온라인에서
    신입도 경력을 깃헙에서 쌓아나갈 수 있다.
    깃헙은 내 개발의 흔적을 말하는 것이다. 포트폴리오가 된다/ 더 투명해진 개발환경
    주호민 작가님은 포폴보다 그 자리에서 그려보게 한다.
    개발도 마찬가지 깃헙에서 120일가까이 지속적으로 커밋한 사람

1. 얼마나 개발했는지 프로잭트 경험
2. 꾸준함 인증
3. 이름, 블로그, sns

## 학습목표

    버전관리/ 마크다운 기반 문서 작성 (Git으로 관리)/ Git/ GitHub

# 마크다운 Markdown

    [markdown](TIL/markdown.md)

# CLI

- CLI (커맨드 라인 인터페이스) 또는 명령어 인터페이스는 가상 터미널 또는 텍스트 터 미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식을 뜻한다.
- 작업 명령은 사용자가 툴바 키보드 등을 통해 문자열의 형태로 입력하며, 컴퓨터로부터 의 출력 역시 문자열의 형태로 주어진다.
- 이 같은 인터페이스를 제공하는 프로그램을 명령 줄 해석기 또는 셀이라고 부른다. 이 를테면, 유닉스 셀(sh, ksh, csh, tcsh, bash 등)과 CP/M, 도스의 command.com("명령 프롬프트") 등이 있다.

### 내가 무엇인가를 알고 싶으면, 명령을 하고 그 결과를 읽어야한다.

### 불편한 것이 아니라 '전혀 다르게' 생각하고 조작하자.

- ls : 목록(list)
- mkdir : 디렉토리 생성(make directory)
- cd : 디렉토리 이동(change directory)
- . : 현재 디렉토리/ .. : 상위 디렉토리
- touch 파일명 : 새로운 파일을 생성
- rm 파일명 : 파일 삭제(remove)

### 실습

CL 명령어를 활용하여 아래에 해당하는 이름을 확인한다.

- 1반 13번 : 최지혜
- 5반 11번 : 서승민
- 3반 15번 : 김영지

CL 명령어를 활용하여 새로운 폴더와 파일을 만든다.

- 6반 1번 본인 이름.txt
- 6반 2번 친구 이름.txt

### 버전관리

- git \_ 분산 버전 관리 시스템
- 버전 : 컴퓨터 소프트웨어의 특정 상태
  git은 버전 기록을 도와주는 강력한 기능이다. 여러 버전관리 시스템에서 가장 많이 쓰이는 것이 git이다. 2005년에 리눅스 만든 아저씨가 버전관리 시스템에 화나서 만들었다.

- Git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구
- 2005년 리눅스 커널을 위한 도구로 리누스 토르발스가 개발
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 파일들의 작업을 조율
- 분산버전관리시스템(DVCS)

저장소를 만들어보자!

터미널에서 git init 입력

## 버전관리 기초

1. 작성(워킹디렉토리)
2. 저장할 내용 모음(add)
3. 버전 기록(commit)
   -m : 커밋메시지 작성을 의미(messag)

## 기본 명령어 ~ 로그(커밋 기록 조회

    $ git log

- 현재 저장소에 기록된 커밋을 조회
- 다양한 옵션을 통해 로그를 조회할 수 있음

  $ git log
  $ git log --oneline 한글로
  $ git log -2 --oneline

- commit할게 없는 상태
- 작업한 내용이 없어 왜 저장하려고해~?
- 버전이 기록되고 있는지 보고 싶
- nothing to commit, working tree clean => 1통, 2통 비어 있음!
