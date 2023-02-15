# 💦 TIL 220215

### 🕘 오전 수업

- 데이터베이스 관련 직종 소개

- SQL\
  Joining table

  [수업노트](/week8/02.15/SQL_memo.md)\
  [수업연습문제](/week8/02.15/SQL_class.sql)

### 🕜 오후 실습 BOJ

[07_SQL 예제](/week8/02.15/DB_07_SQL_Multi_table_queries.sql)

오후 실습문제 5번 때문에 한참을 강의를 돌려보며 이해하려고 노력했다.
Join 쿼리문이 제일 이해하기 어렵다고 하는데, 오늘 잘 이해한건지 모르겠다.\

```
# 5
-- 문제2, 문제3, 문제4 의 조회 결과가 다른 이유를 작성하시오.
# A와 B 두 테이블 속에 겹치는 A.c, B.c 필드가 각각 있을 때(A는 왼쪽, B는 오른쪽)

# 문제 4 INNER는
-- A테이블을 기준으로 A.c필드와 B.c필드 동시에 들어있는 레코드만을 추출해 낸다.
-- (B 테이블에서 A.c와 겹치지 않는 레코드 모두 제외)
-- A.c에는 있지만, B.c에는 없는 레코드 정보는 NULL로 가져온다.
-- A.c에 1개 있지만, B.c에 여러개인 경우, A.c필드의 레코드 정보를 여러개 표시하면서 B.c를 가져온다.

# 문제 2 LEFT는
-- A테이블 전체를 항상 우선 가져오고,
-- INNER와 같이 A테이블을 기준으로 A.c필드와 B.c의 겹치는 정보를 가져온다.

# 문제 3 RIGHT는 A테이블을 기준
-- B테이블 전체를 항상 우선 가져오고,
-- INNER와 같이 A테이블을 기준으로 A.c필드와 B.c의 겹치는 정보를 가져온다.
-- 주의할 점은, INNER와 동일하게 A테이블을 기준으로 해야 한다.
```

</div>
</details>

### 🤨 개인공부

<details>
    <summary> 🎧 Music</summary>

[스테이씨 - teddy bear](https://www.youtube.com/watch?v=4A5_N1CIkPs)\
[부석순 - 파이팅 해야지](https://www.youtube.com/watch?v=MdS-XCjKPcs)

</details>

BOJ 2609 최대공약수, 최소공배수 문제 성공!\
어제 주간문제는 성공했지만, 오늘의 문제는 실패ㅜㅜ
너무 어렵다,,
