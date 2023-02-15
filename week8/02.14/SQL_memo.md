# DDL(Data Definition Language)

데이터의 기본 구조 및 형식 변경

1. Create a table
2. Delete a table
3. Modifying table fields

---

## 1. CREATE TABLE statement

테이블 생성

```sql
-- 기본구조
CREATE TABLE table name (
  column_1 data_type,
  column_2 data type,
...,
constraints
);

--- 예시
CREATE TABLE examples (
    examId INT AUTO_INCREMENT,
    lastName VARCHAR (50) NOT NULL,
    firstName VARCHAR (50) NOT NULL,
    PRIMARY KEY (examId)
);

--Table 구조 확인
SHOW COLUMNS FROM examples;
```

### 1-1. 데이터 타입 Data Type

**대표적인 데이터 타입 3가지**\
숫자형, 문자형, 날짜형

- CHAR(50): 고정 길이\
  설정된 () 안의 숫자만큼만 지정 가능

- VARCHAR(50): 가변적인 길이\
  들어오는 만큼 입력받을 수 있다.\
  ()안의 숫자는 최대 입력 받을 수 있는 limit

- TEXT: 완전히 무한은 아닌(컴퓨터 데이터 저장 능력에 따라 다름) 길이를 따로 지정하지 않는 데이터 베이스

### 1-2. 제약 조건 Constraint

- PRIMARY KEY
  : 해당 필드를 기본 키로 지정
- NOT NULL
  : 해당 필드에 NULL 값을 저장하지 못하도록 지정

> 데이터 *무결성*을 지키기 위해 데이터를 입력 받을 때 실행하는 검사 규칙\
>
> > 무결성 : 데이터의 정확성과 일관성을 보증(아무런 데이터나 받지 않는 것이 중요하다)\
>
> 제약조건이 쓰이는 위치 특히 프라이머리 키가 쓰여지는 위치는 사람마다 표현의 차이로 인해 달라질 수 있다.

### 1-3. 속성

- AUTO INCREMENT attribute : 테이블의 기본 키에 대한 번호 자동 생성

AUTO INCREMENT 특징

기본 키 필드에 사용(고유한 숫자를 부여)\
시작 값은 1이며 데이터 입력 시 자동으로 1씩 증가\
이미 사용한 값을 재사용하지 않음\
기본적으로 NOT NULL이 적용됨

---

## 2. DELETE TABLE statement

- DROP TABLE statement : 테이블 삭제

---

## 3 Modifying table fields

- ALTER TABLE statement : 테이블 필드 조작
  (생성, 수정, 삭제)

  ALTER TABLE **ADD** : 필드 추가\
   ALTER TABLE **MODIFY** : 필드 속성 변경\
   ALTER TABLE **CHANGE COLUMN** : 필드 이름 변경\
   ALTER TABLE **DROP COLUMN** : 필드 삭제

  - ALTER TABLE ADD \
    : ADD키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성

> **NOT NULL을 사용하는 이유는?**\
> mysql을 사용하는 프로그래밍 언어에서 연동되기 위해 되도록 데이터베이스의 확장성을 위해 NOT NULL을 설정하고, 0이나 빈 문자열로 대체하여 사용한다.\
> NOT NULL설정을 안 하고, NULL을 입력하면 다른 프로그래밍 언어에서 번거롭게 데이터 타입 변환을 해줘야한다.

---

---

# DML(Data Manipulation Language)

데이터 조작(추가, 수정, 삭제)

1. Insert data into table
2. Update data in table
3. Delete data from table

---

## 1. INSERT statement

테이블 레코드 삽입

- INSERT INTO 절 다음에 테이블 이름과 괄호 안에 필드 목록을 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록을 작성

## 2. UPDATE statement

테이블 레코드 수정

- SET 절 다음에 수정 할 필드와 새 값을 지정
- WHERE 절에서 수정 할 레코드를 지정하는 조건 작성\
  (WHERE 절을 작성하지 않으면 모든 레코드를 수정)

## 3. DELETE statement

테이블 레코드 삭제

- DELETE FROM 절 다음에 테이블 이름 작성
- WHERE 절에서 삭제할 레코드를 지정하는 조건 작성\
  (WHERE 절을 작성하지 않으면 모든 레코드를 삭제)
