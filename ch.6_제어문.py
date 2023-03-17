#!/usr/bin/env python
# coding: utf-8

# * 나도코딩의 파이썬 입문

# # 6장. 제어문

# ## 6장 실습 문제 : 택시 승객 수 구하기

# In[29]:


# 손님은 총 50명
# 조건을 만족하는 총 탑승객 수를 구하는 프로그램을 작성하시오.

# 조건
# 1. 손님별 운행 소요시간은 5~50분에서 난수로 정한다.
# 2. 운행 소요시간 5~15분인 손님만 매칭
# 3. 실행결과는 다음 형태로 출력, 매칭되면 [0], 매칭 되지 않으면 [] 표시


# In[30]:


# 모듈 로드
from random import *


# In[31]:


customer = 0

# 총 승객 50명 
for i in range(1, 51):
    # 운행 소요시간 정의
    time = randrange(5, 51)
    # 소요시간 5~15분 손님 매칭
    if 5 <= time <= 15:
        # 매칭 성공시 반환
        print(f"[0] {i}번째 손님 (소요시간 : {time}분)")
        # 성공시 count + 1
        customer += 1
    else:
        # 매칭 실패시 반환
        print(f"[] {i}번째 손님 (소요시간 : {time}분)")
print(f"총 탑승객 : {customer}명")


# ## 6장 셀프체크 : 구매 상품 수에 따라 가격을 계산하는 프로그램 작성

# In[32]:


# 구매 상품 수에 따라 가격을 계산하는 프로그램 작성

# 조건
# 1. 상품 1개의 가격 : 1,000원
# 2. 고객은 3의 배수에 해당하는 상품을 구매(가정)
# 3. 상품은 각각 스캔하며, 스캔시 '2+1 상품입니다'를 출력


# In[33]:


# 상품 가격
price = 1000
# 총 가격
total = 0
# 구매 상품 수가 3개일 떄
items = 3

for i in range(1, items + 1):
    print("2+1 상품입니다.")
    if i % 3 ==0:
        continue
    total += price
    
print("총 가격은 " + str(total) + "원입니다.")


# In[34]:


# 상품 가격
price = 1000
# 총 가격
total = 0
# 구매 상품 수가 3개일 떄
items = 6


for i in range(1, items + 1):
    print("2+1 상품입니다.")
    if i % 3 ==0:
        continue
    total += price
    
print("총 가격은 " + str(total) + "원입니다.")

