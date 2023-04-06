from django.test import TestCase, Client

# Create your tests here.
# 하나의 TestCase에서 기본설정은 setUp에서 정의
class TextView(TestCase):
    def setUp(self):
        self.client = Client() # Client함수를 사용하겠다는 내용
        
    def test_post_list(self):
        # 포스트 목록
        # 정상 작동
        # 페이지 타이틀 Blog
        # 네비바 있음
        