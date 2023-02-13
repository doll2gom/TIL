# 3. Filtering data

## DISTINCT

조회 결과에서 중복된 레코드를 제거

## WHERE

조회 시 특정 검색 조건을 지정

## Comparison Operators

비교 연산자
=, >=, <=, !=, IS, LIKE, IN, BETWEEN... AND

## Logical Operators

논리 연산자
AND (&&), OR(11), NOT (!)

## IN operators

값이 특정 목록 안에 있는지 확인

## LIKE operator

값이 특정 패턴에 일치하는지 확인 with wildcards

## wildcard Characters

### '%'

- 0개 이상의 문자열과 일치(앞에 문자가 없어도 됨)
- 하는지 확인

</br>

### '\_'

- 단일 문자와 일치(무조건 1개 이상의 문자를 함께 검색)
- 하는지 확인

## LIMIT clause

조회하는 레코드 수를 제한

# 4. Grouping data

## GROUP BY clause

레코드를 그룹화하여 요약본 생성 with 집계 함수
(Aggregation Functions)

## Aggregation Functions

값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
SUM, AVG, MAX, MIN, COUNT
