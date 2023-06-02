import pandas as pd
import random

# 표 만들기
box_name = []
box_x = []
box_y = []
box_h = []
box_w = []
box_n = []


# data 넣기
for i in range(1, 101):
    box_name.append("box%s" % i)
    box_x.append(random.randrange(50,251,10)) # 50 ~ 250까지 10의 배수
    box_y.append(random.randrange(50, 251, 10))  # 50 ~ 250까지 10의 배수
    box_h.append(random.randrange(50, 251, 10))  # 50 ~ 250까지 10의 배수

    box_w.append(random.randrange(50,501,50)) # 50 ~501까지 50의 배수
    box_n.append(random.randrange(1,6)) # 1 ~ 5 개


subject = pd.DataFrame()
subject["물류 이름"] = box_name
subject["가로"] = box_x
subject["세로"] = box_y
subject["높이"] = box_h
subject["무게"] = box_w
subject["수량"] = box_n

#csv 파일로 지정
subject.to_csv("./test_input.csv", encoding="utf-8-sig", index=False)
