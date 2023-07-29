import csv,json

data=[]
with open('./test_input.csv','r',encoding='utf-8-sig') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

with open('./test_input.json','w') as json_file:
    json.dump(data,json_file)