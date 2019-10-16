import os
import json

print(os.path.abspath('.'))
print(os.getcwd())
print(os.path.join(os.path.dirname(os.path.abspath(__file__)),'db.txt'))

dic=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'db.txt')))
print(dic)