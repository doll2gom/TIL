# 1. Querying data

SELECT statement

## SELECT syntax (기본 체계)

```sql
-- 테이블 A에서 B 필드의 모든 데이터 조회
SELECT
	B
FROM
	A;
```

```sql
-- 테이블 A에서 B, C 필드의 모든 데이터 조회
SELECT
	B,C
FROM
	A;
```

```sql
-- 테이블 A에서 모든 필드의 데이터를 조회
SELECT
	*
FROM
	A;
```

```sql
-- 테이블 A에서 B 필드의 모든 데이터를 조회
(단, B가 아닌 '이름'으로 출력되게 변경)
SELECT
	B AS '이름'
FROM
	A;
```

```sql
-- 테이블 A에서 B, C 필드의 모든 데이터를 조회
(단, C 필드는 c1,c2 필드를 곱한 결과 값)
SELECT
	B,
    c1 * c2 AS 'C'
FROM
	A;
```

# 2. Sorting data

## ORDER BY clause

```sql
-- FROM 뒤에 위치하여 해당 컬럼을 기준으로 오름차순, 내림차순 정렬 --
SELECT
	b,c
FROM
	a
ORDER BY
	b DESC, -- b 컬럼을 내림차순
	c ASC;	-- c 컬럼을 오름차순
-- 생략할 경우 (기본설정) 오름차순으로 정렬
```

```sql
-- 테이블 A에서 B필드를 기준으로 정렬한 다음 C필드 기준으로 오름차순 정렬하여 조회
SELECT
	B, C
FROM
	A
ORDER BY
	B DESC, -- B를 기준으로 먼저 정렬
	C ;	-- B의 중복 항목들이 오름차순으로 정렬됨
```

```sql
-- 테이블 A에서 C필드를 기준으로 내림차순 정렬한 다음 B, C필드의 모든 데이터를 조회
(단, C필드는 c1, c2필드를 곱한 결과 값)
SELECT
	B,
	c1 * c2 AS C
FROM
	A
ORDER BY
	C DESC;
```
