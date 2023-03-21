# DDL(Data Definition Language)

데이터의 기본 구조 및 형식 변경

1. Introduction to Join
2. Joining tables

### JOIN 종류

- INNER JOIN
- OUTER JOIN
  - LEFT JOIN
  - RIGHT JOIN
- CROSS JOIN
- DROP TABLE

---

## 1. Introduction to Join

---

## 2. Joining tables

- INNER JOIN clause : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

- LEFT JOIN clause : 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환

- RIGHT JOIN clause : 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환

**RIGHT JOIN 특징**\
• 오른쪽은 무조건 표시하고, 매치되는 레코드가 없으면 NULL을 표시\
• 오른쪽 테이블 한 개의 레코드에 여러 개의 왼쪽 테이블 레코드가 일치할 경우, 해당 오른쪽 레코드를 여러 번 표시
