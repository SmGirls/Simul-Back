# 물류 정보 관리

import pandas as pd

def struck_list():
    strucks_list = pd.read_csv("../share/Data/test_input.csv") 
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