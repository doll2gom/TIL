# 01 Normalization 정규화

RDB 설계 단계에서 중복을 최소화하여 데이터를 `구조화`하는 과정\
`구조화` : 크고, 제대로 조직되지 않은 테이블들과 관계들을 작고 잘 조직된 테이블과 관계들로 나누는 것

## 정규화 목적

데이터를 쉽게 관리하기 위해

- 하나의 데이터를 무조건 한 곳에만 위치하도록
- 테이블 간의 관계는 키를 통해 형성
- 데이터를 변경하더라도 한 곳만 변경하는 구조 확립

---

# 02 Data Modeling

데이터베이스 시스템을 시각적으로 표현하는 프로세스

for 데이터 유형, 데이터 간의 관계 및 분석 등을 통해 비즈니스 요구사항을 만들어 낼 수 있도록 도움

## ER(Entity-Relationship) Diagram

다이어그램을 사용하여 데이터베이스의 Entity 간 관계를 나타내는 방법\
2가지
![2가지 방법](</02.21/ER(Entity-Relationship)%20Diagram.png>)

## ER Diagram 구성 요소

```
☐ Entity ➡︎ Table
〇 Attribute ➡︎ Field
◊ Relation ➡︎ PK, FK
```

## Relationship 표현 방법

#### # Cardinality & Optionality

- Cardinality : (1:1, N:1, N:M)
- Optionality : 필수 & 선택

> 두 테이블 간의 관계에 따라 표현 방법이 달라진다.
>
> > 회원이 없으면 게시글이 생길 수 없다.\
> > 게시글이 없으면 댓글이 생길 수 없다.\
> > 회원은 N개의 게시글을 작성할 수 있다.

#### # Cardinality와 Optionality을 조합

"하나의 회원은 여러 개의 글을 작성할 수 있고, 하나의 글은 한 명의 회원이 작성할 수 있다"

> 회원과 글의 관계는 `1:N`이며,\
> 글은 `필수적`으로 회원과 연결되어야 하지만\
> 회원은 `선택적`으로 글과 연결될 수 있는 관계

## 데이터 모델링의 중요성

- 데이터베이스 소프트웨어 개발 오류 감소
- 데이터베이스 설계 및 생성 속도와 효율성 촉진
- 조직 전체에서 데이터 문서화 및 시스템 설계의 **일관성** 조성
- 데이터 엔지니어와 비즈니스 팀 간의 커뮤니케이션 촉진

---

# 03 ERD 작성 사이트

1. [draw.io](draw.io)
2. [http://aquerytool.com/](http://aquerytool.com/)
3. [https://www.erdcloud.com/](https://www.erdcloud.com/)
