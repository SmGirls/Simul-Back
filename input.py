import pandas as pd
import os

START_ROW = int(os.getenv('START_ROW' , 1)) # 환경 변수로 시작 row 받아오기

print(os.getenv('START_ROW'))

# csv skiprows ~ 10개 읽어오기
# csv type : DataFrame
csv = pd.read_csv("test_input.csv" , encoding='utf-8-sig'
                ,header=None,skiprows=os.getenv('START_ROW'),nrows = 10)

items_data = csv.values.tolist() # DataFrame -> list 변환
