import pandas as pd
import os

start_row = int(os.getenv('START_ROW', '1'))

# csv skiprows ~ 10개 읽어오기
# csv type : DataFrame
csv = pd.read_csv("./share/Data/test_input.csv", encoding='utf-8-sig', header=None, skiprows=start_row, nrows=10)

items_data = csv.values.tolist() # DataFrame -> list 변환
print(items_data)