# 9-1. Advanced

## Transaction

- Transaction : (다 성공하던지 혹은 다 실패하던지 해야하는) 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법\
  ex) 계좌이체 (인출 & 입금)

```sql
START TRANSACTION;
state_ments;
...
[ROLLBACK or COMMIT];
```

- START TRANSACTION : 트랜잭션 구문의 시작을 알림

- COMMIT : 모든 작업이 정상적으로 완료되면 한꺼번에 DB에 반영

- ROLLBACK : 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림

## Triggers

- Triggers : <U>특정 이벤트</U>에 대한 응답으로 자동으로 `실행`되는 것\

  (INSERT, UPDATE, DELETE)\
  ~를 추가한 `후`에 `~ 하겠다.`\
  ~를 수정하기 `전`에 `~ 하겠다.`\
  ~를 삭제한 `후`에 `~ 하겠다.`\

```sql
CREATE TRIGGER trigger name
{BEFORE AFTER} {INSERT | UPDATE ( DELETE }
ON table_name FOR EACH ROW
trigger_body;
```

만들기 : CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정\
언제? : 각 레코드의 어느 시점에 트리거가 실행될지 지정 (삽입, 수정, 삭제 전/후)\
어디서? : ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정\
어떻게? : 어떤 동작을 할지 trigger_body에 지정\

- 여러 명령문을 실행하려면 BEGIN END 키워드로 묶어서 사용
- 트리거는 `DML`의 영향을 필드 값에만 적용할 수 있음(insert, update, delete)

```sql
-- 트리거를 사용해 기존 게시글이 수정되면, 게시글의 수정일자 필드 값을 최신 일자로 업데이트 하기
DELIMITER //
CREATE TRIGGER beforeArticleUpdate
    BEFORE UPDATE
    ON articles FOR EACH ROW
BEGIN
    SET NEW.updatedAt = CURRENT_TIME();
END//
DELIMITER ;
```

• SQL의 구문 문자(;)를 변경
• BEGIN-END 구문 사이에 여러
SQL 문이 작성되기 때문에 하나의 트리거로써 작동될 수 있도록
사용

• 트리거에서 특점 시점 `전/후`의 값에 접근 할 수 있도록 제공하는 키워드\
• OLD 와 NEW 2개 제공
상황별로 사용할 수 있는 여부
| |OLD|NO|
| ---| ---| ---|
| INSERT | NO | YES |
| UPDATE|YES|YES|
| DELETE|YES|NO|

---

### Triggers 에러 해결

- 트랜잭션이 정상 적으로 종료되지 않아 발생하는 에러

> Error Code:2013. Lost connection to MySQL server during query

> Error Code:2015. Lock wait timeout exceeded; try restarting transaction

```sql
-- 실행중인 프로세스 목록 확인
SELECT * FROM information_schema.INNODB_TRX;
```

```sql
-- 특정 프로세스의 trx_mysql_ thread_1d 삭제
KILL[trx_mysql_thread_id1];
```
