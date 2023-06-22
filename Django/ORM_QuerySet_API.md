# ORM

- ORM은 `객체 지향 언어`와 `관계형 데이터베이스`를 연결하는 작업이다.

- Object-Relational Mapping
  - 객체-관계 매핑
  - 매핑(mapping) : 두 가지를 연결

백앤드 프래임워크들은 자기들 만의 ORM을 가지고 DB와 소통한다.

# QuerySet API

Django ORM에서 데이터를 조회, 수정, 삭제하는 도구로써,\
SQL 쿼리문을 직접 작성하지 않아도 Python코드로 데이터에 접근할 수 있게 된다.

쿼리셋 api의 구성은 다음과 같다.\
장고에서 쿼리문을 사용하기 위해 이러한 규칙을 사용한다.\
핵심은 마지막에 작성하는 구문에 따라 데이터 베이스를 조작하게 된다.

`model class`.`manager`.`QuerySetAPI`
```
select * from ...
Article.objects.all()
```
파이썬으로 작성한 코드가 ORM의 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이, Queryset<sub>타입이름</sub>이라는 자료 형태로 변환하여 우리에게 전달한다.



## QuerySet

데이터베이스에서 전달 받은 객체 목록(데이터 모음)

> 순회, 반복 가능

Django ORM을 통해 만들어진 자료형

단일한 객체를 반환할 때는 QuerySet이 아닌 모델class의 인스턴스로 반환됨

---

[ORM read](/Django/ORM_Read.md)

### ORM, QuerySet API를 사용하는 이유 
- 개발자가 데이터와 직접 상호작용하지 않아도 됨
- 개발자의 개발에 **생산성**을 높이기 위함이다.
- 빠른 결과물을 위해

> 단, 복잡한 SQL문이 필요한 경우 데이터에 직접 접근해서 SQL 쿼리문을 사용해야 한다. 
  