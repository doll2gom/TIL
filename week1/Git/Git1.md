# 버전관리 기초

> 1. 작업을 하고
> 2. 변경된 파일을 모아 (add)
> 3. 버전으로 남긴다. (commit)

# Git 기본 명령어

1. git init : 워킹디렉토리 생성
2. add : 저장할 내용 모음
3. commit : 버전 기록
   -m (message) : 커밋메시지 작성을 의미

```
  $ git init
  $ git add
  $ git commit -m (message)
```

# 커밋 기록 조회

$ git log : 현위치의 저장소에 기록된 커밋을 조회

아래 옵션을 통해 로그 조회할 수 있음

```
  $ git log
  $ git log --oneline 한글로
  $ git log -2 --oneline
```

> master/main의 차이\
> master가 글(로벌)룰이었는데, 노예제도를 연상시킨다는 이유로 main으로 바꾸자는 움직임들이 있다.\
> 하지만, 여전히 master가 보편적으로 많이 쓰이고 있음

## 발생 가능한 문제 상황들

- commit할게 없는 상태
- 작업한 내용이 없어 왜 저장하려고해~?
- 버전이 기록되고 있는지 보고 싶
- nothing to commit, working tree clean => 1통, 2통 비어 있음!

## 질문!

```
- 목표라는 이름의 폴더 이름 바꿔도 되나?
  => 된다!

- .git 폴더를 지워도 된다? 안된다?
  => x 버전이 모두 삭제됨

- 목표라는 폴더를 다른 곳으로 이동(예, 바탕화면 -> C/) 가능한가 아닌가?
  => △ 다른 git 저장소 폴더 하위 폴더면.. 안됨
  submodule 이라는 것을 통해 git 저장소로 관리하는 것
```
