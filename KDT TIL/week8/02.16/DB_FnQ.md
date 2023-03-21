# Q. 지금까지 배운 데이터베이스 어떤 상황에 적용이 가능할까?

## A. 게시글, 댓글, 작성자 3개의 정보 테이블이 있을 때, 각각의 테이블을 연결하는 외래키가 어디에 있어야 할까??

---

### 상황1

```
1명의 유저는 게시글을 여러개 작성할 수 있다.(작성하지 않을 수도 있음)
>> 게시글이 외래키를 가져감
```

### 상황2

```
1개의 게시글에는 여러 댓글이 작성될 수 있다.(작성되지 않을 수도 있음)
>> 댓글이 외래키를 가져감
```

### 상황3

```
1명의 작성자는 여러 댓글을 작성할 수 있다.(작성하지 않을 수도 있음)
>> 댓글이 외래키를 가져감
```

####N : 1의 관계에서 Foreign Key(FK)는 N이 가져간다.

게시글(N) : 작성자(1)\
\>> 여러 게시글을 1명이 작성하기 때문에 FK는 N쪽에서 가져간다\
\>> 댓글(N) : 게시글(1)\
\>> 여러 댓글이 1개의 게시글에 작성될 수 있기 때문에 FK는 N쪽에서 가져간다