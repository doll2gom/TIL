# Git이란?

```bash
- 분산/ 버전/ 관리/ 시스템
- 로컬 버전 관리 → 작업을 (add, commit)
- 파일로 할 수 있는 일 CRUD
  C 생성
  R 읽기
  U 수정
  D 삭제

- 작업을 하게되면 다양한 파일이 동시다발적으로 변경되게 된다.
- 변경된 파일들을 모두 모으는 것이 add
- 그것을 저장하는 것이 commit
```

## 커밋해시값

```bash
고유한 값/ 내일 오전 branch 배움 내가 어디까지 왔는지 확인
```

## 질문!

```bash
- 목표라는 이름의 폴더 이름 바꿔도 되나?
  => 된다!/ .gidl git의 본체임

- .git 폴더를 지워도 된다? 안된다?
  => x 버전이 모두 삭제됨

- 목표라는 폴더를 다른 곳으로 이동(예, 바탕화면 -> C/) 가능한가 아닌가?
  => △ 다른 git 저장소 폴더 하위 폴더면.. 안됨
  submodule 이라는 것을 통해 git 저장소로 관리하는 것
```

# 분산버전관리시스템 (DVCS)

몇가지 종류중에 전세계적으로 github(원격저장소)을 가장 많이 사용함

# 깃헙 github

```bash
- push : 원격저장소로 저장하는 명령어
  git push
- pull : 원격저장소 버전을 로컬 저장소로 가져온다.
  git pull

지금은 push하지만 다른 사람과 협업할 때 pull하는 상황이 많이 발생한다.
```

## 실습

```bash
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>
```

### 초기 원격저장소 설정하는 법

```bash
1. New Repository 클릭
2. 저장소 설정
   이름, 설명, 공개여부,(다른거 별도 설정하지 않는다.), 생성
3. URL 확인
4. 로컬에 원격저장소 정보 설정하기
   복붙
   깃아\ 원격저장소\ 추가해\ origin으로\ ...\내 깃헙이름\저장소이름\ .git
5. 원격저장소 기본이름 많이 쓰는 것
   => origin
```

### push 하기

```bash
> git push <원격저장소이름> <브랜치이름>

- push할 때 인증정보 필수
- 맥은 토큰을 발급 받아 비밀번호로 활용(github비밀번호 아닌 토큰값이다!)
  Authentication이 뜨면 인증번호 다시 확인(토큰값)
```
