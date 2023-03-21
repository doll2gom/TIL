# Workbench 활용 가이드

## Workbench 활용 MySQL 접속 방법

1. MySQLWorkbench 어플리케이션 실행

2. 첫 화면에서 MySQL Connections에서 기본 설정된 Local MySQL Server 실행\
   2-1. password입력

3. 새로운 Connection을 만들려면 \
    첫 화면 MySQL Connections 옆의 작은 플러스(+)를 누른다.\
   3-1. Name 이름생성\
   3-2. Password : Store in Keychain 클릭하여 뜨는 화면에서 입력 > Username root로 지정\
   3-3. Test Connection 클릭하여 테스트한다.
   3-4. Successfully로 시작하는 화면 뜨면 > OK로 되돌아가 > close눌러 설정을 닫고 첫 화면으로 돌아간다.

4. 데이터베이스 여는 법\
   4-1. 원하는 db선택\
   4-2. SQL아이콘 선택 (새 SQL 입력창 불러오기)\
   4-3. SQL 쿼리문 작성\
   4-4. 번개아이콘 선택 (쿼리 실행)\
   4-5. 결과 확인

5. 만일 선택 가능한 데이터가 없을 경우 \
   \> [Administration]에서 [Data Import/Restore] 클릭하여 원하는 데이터 가져오기\
   \> Import from Self-Contained File\
   \> (.)선택 \
   \> 열리는 문서 탐색 창에서 원하는 데이터 파일 선택\
   \> start import 클릭하여 불러오기

## 데이터베이스에 대한 쿼리(Query)문 작성 및 쿼리문 실행 방법

- MySQL [공식문서 사용법](https://dev.mysql.com/doc/workbench/en/)\
- [reference](https://blog.naver.com/PostView.nhn?blogId=rlarbtjq7913&logNo=221805728231)

### 기본 4가지 쿼리

1. create(생성)

```sql
create database 생성할데이터베이스명;
```

</br>

2. select(호출)

```sql
select * from 데이터베이스명.테이블명;
```

Table Name : 생성할 테이블명\
Column Name : 생성할 컬럼명\
Datatype : 입력될 데이터의 속성(int : 숫자열, VARCHAR(문자 길이) : 문자열)\
PK(primary key) : 중복 허용 X, 반드시 필요, 각 데이터를 구별하기 제일 좋은 컬럼에 사용\
NN(not null) : 비어있으면 안 된다. (체크해제하면 값이 없어도 됨)
</br>
</br>

3. update(변경)

```sql
update 데이터베이스명.테이블명 set 바꿀내용 where 바뀔조건;
update notepad.tn set codename = '세타' where No = 4;
```

</br>

4. drop & delect(삭제)\

```sql
delect from 데이터베이스명.테이블명 where 삭제할행의조건;
drop database 삭제할데이터베이스명;
```

etc. 검색 문자(like와 함께 사용)\
 % : 없거나 하나이상의 문자에 대응\
 \_ : 하나의 문자에 대응

```sql
- 2번째 글자가 n
where colunm like '_n%';

- 글자 길이가 3자
where colunm like '___';
```
