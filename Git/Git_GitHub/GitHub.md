# GitHub 기본 명령어

```
- push : 원격저장소로 저장하는 명령어
  git push
- pull : 원격저장소 버전을 로컬 저장소로 가져온다.
  git pull

지금은 push하지만 다른 사람과 협업할 때 pull하는 상황이 많이 발생한다.
```

## 초기 원격저장소 설정하는 법

```
1. New Repository 클릭
2. 저장소 설정
  : 이름, 설명, 공개여부,(다른거 별도 설정하지 않는다), 생성
3. URL 확인
4. 로컬에 원격저장소 정보 설정하기
  : URL을 잘 복붙한다
  (git아  원격저장소  추가해  origin으로  ... 나의 깃헙이름  저장소이름  .git)
5. 원격저장소 기본이름은 전 세계적으로 많이 쓰는 것이 origin이다.
```

# GitHub flow 기본 원칙

Github Flow는 Github에서 제안하는 브랜치 전략으로 다음과 같은 기본 원칙을 가지고 있다.

```
1. master branch는 반드시 배포 가능한 상태여야 한다.
2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
3. Commit message는 매우 중요하며, 명확하게 작성한다.
4. Pull Request를 통해 협업을 진행한다.
5. 변경사항을 반영하고 싶다면, master branch에 병합한다.
```

## GitHub 실제 사용과정 상세

```
1. 브랜치 만들고
2. 작업
3. 커밋
4.  로컬에서 master 이동/병합
    github으로 브랜치 push
5. Pull request (리뷰)
6. merge

 * A가 pull request를 하면
    > 가져가 주세요~!
 * origin에서 pull master하여
    > 가져와서
 * 두개의 파일을 merge한다
    > 합친다
```

## push 하기

```
기본 입력문
$ git push <원격저장소이름> <브랜치이름>

적용예시
$ git push origin master
```

> push 입력시 주의사항

- push할 때 인증정보 필수
- 맥은 토큰을 발급 받아 비밀번호로 활용(github비밀번호 아닌 토큰값이다!)
  Authentication이 뜨면 인증번호 다시 확인(토큰값)

> push 실패

1. 원격저장소의 커밋을 원격저장소로 가져와서(pull)
2. 로컬에서 두 커밋을 병합(추가 커밋 발생) 동시에 같은 파일이 수정된 경우 merge conflict가 발생하나 이 부분은 브랜치 학습
3. 다시 GitHub으로 push

---

# Git/GitHub 명령어 정리

```
- 저장소 처음 만들때
  § git init
- 비전을 기곡할 때
  S git add.
  Sgit commit m '커밋메시지'
- 상태 확인할 때
  Sgit status : 1동, 2통 S gt log : 커밋 확인
- 원격저장소 할용하기
  • 원격저장소 설정을 처음 할 때
  S git remote add origin URL
  • push / pull
  $ git push origin master
  S git pull origin master
```

## GitHub을 활용한 협업

```
다운로드.zip은 최신버전의 파일을 가져올 뿐
clone은 git 저장소를 받아오는 것으로 모든 버전을 받은 것일 뿐
init은 개인의 로컬에 저장하는 것일 뿐

clone에 저장한다는 것은 금일 github에서 앞서 생성한 'test'폴더의 위치를 가져오는 것이다.
pull은 하나의 저장소를 가져오는 것으로 여러사람이 하나의 원격저장소에 push/pull로 협업하는 것이다.
타인의 저장소에 접근하려면 접근 권한을 부여받아야 push가 가능하다.
```

```
- 로컬에서 프로젝트 시작?
  init
- 원격에 있는 프로젝트 시작?
  git clone
- 다른사람 작업내용 가져오기?
  git pull
- 내가 한 로컬작업 공유?
  git push
```

| 명령어                         | 내용                                |
| ------------------------------ | ----------------------------------- |
| git clone <url>                | 원격 저장소 복제                    |
| git remote - v                 | 원격저장소 정보 확인                |
| git remote add origin <url>    | 원격저장소 추가 (일반적으로 origin) |
| git remote rm <원격저장소>     | 원격저장소 삭제                     |
| git push <원격저장소> <브랜치> | 원격저장소에 push                   |
| git pull<원격저장소> <브랜치>  | 원격저장소로부터 pull               |

---

## .gitignore

```
git으로 관리되지 않는 문서, 파일, 폴더 등을 의미한다.

- 이미 커밋한 경우는?
  => 무시하지 않는다. 그래서 미리 .gitignre를 설정하자.

- 커밋된 정보를 삭제할 수는 있지만, 삭제한 기록이 남게 된다.
  => 그래서 .gitignore를 처음부터 잘 설정하자!!!

- 커밋역사 (commit history)
  잘 기록하되 바꾸려고 하지 말자/// 역사를 만들기만 하자///
```

## gitignore.io

```
개발환경에 따른 깃 이그노어 파일이 쭉 나온다.
복붙으로 개발환경 먼저 셋팅하면 편리함

메모장은 인코딩의 적... 무조건 vsc로 작성한다...!
```

---

## 질문

```
- github에 올리고 로컬에서 파일을 지우면 사라지나요?
  => △ 아니오 사라지지는 않는다. 버전을(커밋)하는 것 add,commit하면 그냥 최신 상태의 버전을 보여줄 뿐!
  ! 모든 것은 자동으로 되지 않는다. !

- 왜 push가 reject되었나? 어떻게 해결하나?
  => 하나의 프로젝트에 두번째 사람의 작업이 pus되면 문제 발생

  1. push 거절
  2. pull 권유, pull 진행
  3. merge commit 자동으로 됨
  4. push 진행

- 같은 파일을 수정했다면?
  => merge conflict(목요일 수업할 예정)
```

### 실습

```
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>
```
