# API 
Application Programming Interface\
애플리케이션과 프로그래밍으로 소통하는 방법

#### - API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공
  > 예를 들어 집의 가전 제품에 전기를 공급해야 한다고 가정해보자.
  >> 우리는 그저 가전 제품의 플러그를 소켓에 꽂으면 제품이 작동함\
  >> 중요한 것은 우리가 가전 제품에 전기를 공급하기 위해 **직접 배선을 하지 않는다는 것**\
  >> 매우 위험하면서도 비효율적인 일

# Web API 
- 웹 서버 또는 웹 브라우저를 위한 API
- 현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 Open API를 활용하는 추세
- 대표적인 Third Party Open API 서비스 목록
  - Youtube API
  - Naver Papago API
  - Kakao Map API
- AP1은 다양한 타입의 데이터를 응답
  - HTML, JSON 등

# REST API
REST라는 API 디자인 아키텍처를 지켜 구현한 API

---

## REST 
Representational State Transfer

- API Server를 개발하기 위한 일종의 소프트웨어 설계 **방법론**
   -  2000년 로이 필딩의 박사학위 논문에서 처음으로 소개 된 후 네트워킹 문화에 널리 퍼짐
   -  처음에는 방법론으로 시작했으나 현재는 규약처럼 자리를 잡아 널리 지켜지고 있다.
- '소프트웨어 아키텍쳐 디자인 제약 모음'\
    (a group of software architecture design constraints)
- REST 원리를 따르는 시스템을 **RESTful**하다고 부름
- **자원을 정의**하고 **자원에 대한 주소를 지정**하는 전반적인 방법을 서술

---

### REST에서 자원을 정의하고 주소를 지정하는 방법
1. 자원의 식별
    - URL, URI 
2. 자원의 행위
    - HTTP Methods(GET, POST, DELETE, PUT)
3. 자원의 표현
    - 궁극적으로 표현되는 결과물
    - JSON으로 표현된 데이터를 제공

---

#### 대표 HTTP Request Methods
1. GET
    - GET을 사용하는 요청은 데이터만 검색해야 함
    - 서버의 상태를 변경
2. POST
    - 데이터를 지정된 리소스에 제출
    - 서버에 리소스의 표현을 요청
3. PUT
    - 요청한 주소의 리소스를 수정
4. DELETE
    - 지정된 리소스를 삭제
