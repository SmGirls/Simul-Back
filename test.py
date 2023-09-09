import json
import visualize_func

select_list=[{'productname': 'box1', 'width': 250, 'depth': 220, 'height': 220, 'weight': 100, 'count': 5}, {'productname': 'box2', 'width': 180, 'depth': 160, 'height': 250, 'weight': 300, 'count': 4}]

select_items_list=[]
for item in select_list:
    select_items_list.append([
        item['productname'],
        item['width'],
        item['depth'],
        item['height'],
        item['weight'],
        item['count']
    ])   

print("select_list:",select_items_list)

containers = [
    [1000, 1000, 1000],
]

visualize_func.simulation(containers,select_items_list)