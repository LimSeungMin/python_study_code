#!/usr/bin/env python
# coding: utf-8

# * 나도코딩의 파이썬 입문

# # 9장. 클래스

# ## 9장 실습 문제 : 부동산 프로그램 만들기

# * 부동산 프로그램 작성
# 
# * 조건
# * 1. 생성자로 인스턴스 변수를 정의. 매물 정보를 표시하는 show_detail() 메서드로 인스턴스 변수를 순서대로 출력.
# * 2. 실행결과에 나온 3가지 매물을 객체로 만들고, 총 매물 수를 출력, show_detail() 메서드를 호출해 각 매물 정보를 표시
# ```
# 총 3가지 매물이 있습니다.
# 강남 아파트 매맴 10억원 2010년
# 마포 오피스텔 전세 5억 원 2007년
# 송파 빌라 월세 500/50만 원 2000년
# ```

# In[7]:


class House:
    # 매물 초기화: 위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)        


# In[10]:


real_estates = []
real_estate1 = House("강남", "아파트", "매매", "10억 원", "2010년")
real_estate2 = House("마포", "오피스텔", "전세", "5억 원", "2007년")
real_estate3 = House("송파", "빌라", "월세", "500/50만 원", "2000년")


# In[11]:


real_estates.append(real_estate1)
real_estates.append(real_estate2)
real_estates.append(real_estate3)


# In[15]:


print(f"총 {len(real_estate)}가지 매물이 있습니다.")
for i in real_estates:
    i.show_detail()


# ## 9장 셀프체크 : 주차 차량 등록 관리 프로그램 작성

# In[32]:


# 주차 차량 등록 관리 프로그램 작성
# 조건
# 1. 총 주차 가능 대수인 capacity는 객체를 생성시 전달받아 인스턴스 변수로 정의
# 2. 현재 등록된 차량 수를 관리하는 count는 객체를 생성할 때 0으로 정의
# 3. 객체를 생성시 등록 가능한 대수를 출력
# 4. 차를 신규로 등록하는 register() 함수를 정의
# 5. 신규 등록 시 등록 현황을 출력
# 6. 총 주차 가능 대수를 초과하는 경우 "더 이상 등록할 수 없습니다" 메세지 출력


# In[18]:


class ParkingManager:
    # 주차 정보 초기화 : 총 주차 가능 대수
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f"총 {capacity}대를 등록할 수 있습니다.")
    
    # 신규 차량 등록          
    def register(self):
        if self.count >= self.capacity:
            print("더 이상 등록할 수 없습니다.")
            return
        self.count += 1
        print(f"차량 신규 등록({self.count}/{self.capacity})")     


# In[19]:


# 테스트 코드
manager = ParkingManager(5)
for i in range(6):
    manager.register()

