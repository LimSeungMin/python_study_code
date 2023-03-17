#!/usr/bin/env python
# coding: utf-8

# * 나도코딩의 파이썬 입문

# # 7장. 함수

# ## 7장 실습 문제 : 표준 체중 구하기

# In[29]:


# 표준 체중을 구하는 프로그램을 작성.
# 표준 체중 : 키에 따른 평균 체중
# 성별에 따른 표준 체중 공식
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건
# 1. 표준 체중은 별도 함수로 계산한다. 키는 미터(m)단위로 받음
#  함수명 : std_wegiht
# 전달값 : 키(height), 성별(gender)
# 2. 표준 체중은 소수점 이하 둘째 자리까지 표기


# In[13]:


def std_weight(height, gender):
    if gender == "남자":
        weight = (float(height) / 100) *(float(height) / 100) * 22
        weight = round(weight, 2)
        print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다")
    else:
        weight = (float(height) / 100) * (float(height) / 100) * 21
        weight = round(weight, 2)
        print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다")


# In[14]:


std_weight(175, "남자")


# ## 7장 셀프체크 : 미세먼지 수치를 입력받아 대기질 상태를 출력하는 함수 작성

# In[32]:


# 미세먼지 수치를 입력받아 대기질 상태를 출력하는 함수 작성

# 조건
# 1. 함수명 : get_air_quality
# 2. 전달값으로 미세먼지 수치 입력, 대기실 상태 반환
# 3. 미세먼지 수치에 따른 대기질 상태
# 좋음 : 0 ~ 30
# 보통 : 31 ~ 80
# 나쁨 : 81 ~ 150
# 매우 나쁨 : 151 이상
# 전달값은 항상 0 이상의 값이라 가정


# In[15]:


def get_air_quality(pm):
    if 0 <= pm <= 30:
        print("좋음")
    elif 31 <= pm <= 80:
        print("보통")    
    elif 81 <= pm <= 150:
        print("나쁨")       
    else:
        print("매우 나쁨")


# In[16]:


# 테스트 코드
# 미세먼지 수치가 15일 떄
get_air_quality(15)


# In[17]:


# 테스트 코드
# 미세먼지 수치가 85일 떄
get_air_quality(85)

