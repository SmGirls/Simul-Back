# 물류 정보 관리

import pandas as pd
import json

json_path = "/home/ec2-user/kch/Simul-Back/share/Data/test_input.json"

def struck_list():
    with open(json_path,'r',encoding='utf-8-sig') as file:
        strucks_list = json.load(file)
    return strucks_list
def add_quantity(struck):
    struck += 1
    return struck
def del_quantity(struck):
    struck -= 1
    return struck

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 1 or sys.argv[1] == "help":
        help(sys.argv)

    elif sys.argv[1]=="struck_list":
        print(struck_list())
    
    else:
        help(sys.argv)