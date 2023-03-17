#!/usr/bin/env python
# coding: utf-8

# * 나도코딩의 파이썬 입문

# # 8장. 입출력

# ## 8장 실습 문제 : 보고서 파일 만들기

# * 매주 1회 보고서 작성. 1~50주차까지의 보고서 파일 생성하는 프로그램 작성
# 
# * 조건
# * 1. 파일명은 '1주차.txt', '2주차.txt'
# * 2. 해당 내용
# ```
# - 35주차 주간보고 - 
# 부서 :
# 이름 : 
# 업무 요약 :
# ```

# In[2]:


for i in range(1, 51):
    week_file = open(f"{i}주차.txt", "w", encoding="utf8")
    print(f"- {i}주차 주간보고 -", file=week_file)
    print("부서 : ", file=week_file)
    print("이름 : ", file=week_file)
    print("업무 요약 : ", file=week_file)
    week_file.close()


# ## 8장 셀프체크 : 파일 내용을 읽어 와서 각 반의 정보를 출력하는 프로그램 작성

# In[32]:


# 파일 내용을 읽어 와서 각 반의 정보를 출력하는 프로그램 작성
# 조건
# 1. 초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명 이 포함된 class.txt 파일 생성
# 2. split()을 이용해 내용을 구분하여 출력(빈칸 기준)
# 3. 정보가 '명'으로 끝나는 경우 줄 바꿈. endswith() 사용


# In[11]:


class_file = open("class.txt", "w", encoding="utf8")
print("초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명", file=class_file)
class_file.close()


# In[13]:


with open("class.txt", "r", encoding="utf8") as class_info:
    txt = class_info.read()
    words = txt.split()
    for word in words:
        print(word, end=" ")
        if word.endswith("명"):
            print()

