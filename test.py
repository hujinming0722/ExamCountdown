import json
 
data = {'name':'Lee','age':'16'}
a=json.dumps(data)
print(json.loads(a))