# 관계형 데이터베이스 기초 개념과 용어

## 1. Table (aka Relation)

- 표(엑셀시트)\

  관계형 데이터베이스에서는 테이블 자체를 그냥 관계라고 부르기도 한다.\
  하나하나의 데이터를 저장하는 공간

## 2. Field (aka Column, Attribute)

- 열, _세로_(엑셀 열)\

  관계형 데이터베이스에서는 row와 column이라는 명칭은 잘 쓰지 않는다.\
  하나하나의 필드라고 말한다.\
  필드에는 어떤 데이터 타입이 들어갈지 데이터의 형식이 지정된다. (ex. 정수, 문자열….)\
  누군가는 속성(Attribute)이라고 부르기도 한다.

## 3. Record (aka Row, Tuple)

- 행, _가로_(엑셀 행)\

  하나하나의 레코드에는 구체적인 데이터 값이 저장된다.\
  즉, 데이터 그 자체로만 이루어져 있다.

## 4. Database (aka Schema)

- (엑셀 파일)\

  데이터들의 모음이자 데이터들이 저장되는 테이블(표)들의 모음\
  테이블의 집합\
  스키마라고도 부른다

## 5. Primary Key(기본 키)

- 각 레코드의 고유한 값\

  고유한 값이어야 하기에 중복이 있으면 안 된다.\
  관계형 데이터베이스에서 각각의 레코드를 식별할 수 있는 식별자로 활용한다.

## 6. Foreign Key(외래 키)

- 테이블(표)의 필드(열;_세로_) 중 다른 테이블의 레코드(행;_가로_)를 식별할 수 있는 키\

  각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용\
  외래 키가 중요한 이유는 다른 관계형 데이터베이스의 핵심인 데이터 간의 관계를 만들어내기 때문이다.\
  물리적으로 연결되지 않은 것들 사이를 연결해준다.
