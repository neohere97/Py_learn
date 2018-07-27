import json

# with open('D:\Code\Py\data.json', 'r') as f:
#     logic = json.load(f)

# print(logic['ProjectID'])

f1 = open('D:\Code\Py\data.json','r')

jsobj = json.load(f1)

print(jsobj['FunctionalBlocks']['Block1']['InputConnections']['IN0'])


