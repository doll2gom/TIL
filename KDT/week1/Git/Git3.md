## git 명령어 정리

```bash
- 저장소 처음 만들때
  $ git init
- 비전을 가공할 때
  $ git add.
  $ git commit m '커밋메시지'
- 상태 확인할 때
  $ git status : 1동, 2통
  $ git log : 커밋 확인
- 원격저장소 할용하기
  • 원격저장소 설정을 처음 할 때
  $ git remote add origin URL
  • push / pull
  $ git push origin master
  $ git pull origin master
```

## 질문

```bash
- github에 올리고 로컬에서 파일을 지우면 사라지나요?
  => △ 아니오 사라지지는 않는다. 버전을(커밋)하는 것 add,commit하면 그냥 최신 상태의 버전을 보여줄 뿐!
  ! 모든 것은 자동으로 되지 않는다. !
```

## 협업에서의 git활용

```bash
다운로드.zip은 최신버전의 파일을 가져올 뿐
clone은 git 저장소를 받아오는 것으로 모든 버전을 받은 것일 뿐
init은 개인의 로컬에 저장하는 것일 뿐

clone에 저장한다는 것은 금일 github에서 앞서 생성한 'test'폴더의 위치를 가져오는 것이다.
pull은 하나의 저장소를 가져오는 것으로 여러사람이 하나의 원격저장소에 push/pull로 협업하는 것이다.
타인의 저장소에 접근하려면 접근 권한을 부여받아야 push가 가능하다.
```

```bash
- 로컬에서 프로젝트 시작?
  init
- 원격에 있는 프로젝트 시작?
  git clone
- 다른사람 작업내용 가져오기?
  git pull
- 내가 한 로컬작업 공유?
  git push
```

| 명령어                      | 내용                                |
| --------------------------- | ----------------------------------- |
| git clone <url>             | 원격 저장소 복제                    |
| git remote - v              | 원격저장소 정보 확인                |
| git remote add origin <url> | 원격저장소 추가 (일반적으로 origin) |
| git remote rm origin        | 원격저장소 삭제                     |
| git push origin <브랜치>    | 원격저장소에 push                   |
| git pull origin <브랜치>    | 원격저장소로부터 pull               |

---

## 질문

```bash
- 왜 push가 reject되었나? 어떻게 해결하나?
  => 하나의 프로젝트에 두번째 사람의 작업이 pus되면 문제 발생

  1. push 거절
  2. pull 권유, pull 진행
  3. merge commit 자동으로 됨
  4. push 진행

- 같은 파일을 수정했다면?
  => merge conflict(목요일 수업할 예정)
```

### push 실패

```bash
1. 원격저장소의 커밋을 원격저장소로 가져와서(pull)
2. 로컬에서 두 커밋을 병합(추가 커밋 발생) 동시에 같은 파일이 수정된 경우 merge conflict가 발생하나 이 부분은 브랜치 학습
3. 다시 GitHub으로 push
```

# .gitignore

```bash
git으로 관리되지 않는 문서, 파일, 폴더 등을 의미한다.

- 이미 커밋한 경우는?
  => 무시하지 않는다. 그래서 미리 .gitignre를 설정하자.

- 커밋된 정보를 삭제할 수는 있지만, 삭제한 기록이 남게 된다.
  => 그래서 .gitignore를 처음부터 잘 설정하자!!!

- 커밋역사 (commit history)
  잘 기록하되 바꾸려고 하지 말자/// 역사를 만들기만 하자///
```

## gitignore.io

```bash
개발환경에 따른 깃 이그노어 파일이 쭉 나온다.
복붙으로 개발환경 먼저 셋팅하면 편리함
```

```bash
### 메모장은 인코딩의 적... 무조건 vsc로 작성한다...!
```
