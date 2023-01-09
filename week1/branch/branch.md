# Branch

- 독립적인 작업흐름을 만들고 관리
- 각자 독립된 버전의 흐름을 만든다

## Branch 주요 명령어

```
1. 브랜치 생성
    (master) $ git branch (branch name)
2. 브랜치 이동
    (master) $ git checkout {branch name
3. 브랜치 생성 및 이동
    (master) $ git checkout -b (branch name}
4. 브랜치 목록
    (master) $ git branch
5. 브랜치 삭제
    (master) $ git branch -d {branch name)
6. 브랜치 그래프 확인
    (master) $ git log --oneline --graph
```

## 해시값(hash)

```
branch에서 표기되는 고유한 값으로 알파벳과 숫자로 이루어진다.
commit을 했을 때 해당 기록과 함께 생성된다.
```

> ⚠️ 내가 지금 어느 branch에 있는지 봐야한다 ⚠️

---

# 3가지 예시 상황

A와 B의 협업 프로젝트

## 상황1 (main)

> A혼자 독박(main)

```
1. (master) A가 main파일 생성+작업 > 커밋

2. (feature/main) B가 도망감

3. (master) A가 merge 했지만 소용없었다.
```

### 상황2 (home)

> A와 B각자 역할을 분담하여 각자 독립적인 버전의 작업 흐름을 가진다.

```
1. (master) A가 home1파일 생성+작업 > 커밋!

2. (feature/home) B가 home2파일 생성+작업 > 커밋!

3. (master) A가 home1파일과 home2파일을 merge하여 하나의 작업물로 모은다 > 커밋!
```

### 상황3 (report)

> A와 B가 함께 모든 역할을 감당하여 하나의 프로젝트를 동시에 작업한다.

```
1. (master) A가 report 생성+작업 > 커밋!

2. (feature/report) B가 report 생성+작업 > 커밋!

3. (master) A가 report 파일을 모두 한번에 merge한다
    > 두개의 report파일이 서로 충돌이 없으면 Git이 알아서 merge를 진행한다
    > 커밋!
```

### 상황4 (hotpix : README)

> 수정하는 현시점에서 A와 B 모두 README.md파일을 수정

```
1. (master) A가 README.md 생성+작업 > 커밋!

2. (feature/report) B가 README.md 생성+작업 > 커밋!

3. (master) A가 README.md파일을 모두 한번에 merge한다
    > 문제발생
    > status로 문제항목을 파악(VSC에서는 심지어 문서 내의 어느 위치인지 색상으로 표시해 알려줌)

4. 겹치는 수정사항을 리더가 적절히 선별하여 결정 및 조합(=merge)

    > 커밋!
```

> merge + commit 작업이 완료되면 쓰임을 다한 branch를 삭제

### commit message

    $ git commt만 입력시
    기존 커밋 메세지를 바탕으로 자동 입력되어 있다.

### release branch

    버그/오류확인 + 검수 (=QA라고 많이 말함)

### git 유의사항

    커밋은 저장이 아님!
    commit은 의미있는 과정으로 인식해야 한다.
    예) 밥먹기 전에 중간저장하는 그런 용도가 아님
