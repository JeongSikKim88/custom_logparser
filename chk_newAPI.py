# from json_parser import parser
import json


with open('logs/json/20200304_179_newAPI.json') as data_file:
    data = json.load (data_file)


i=0
sum = 0
for i in range(0,287):

    i+=1
    
    sum += int(json.dumps(data['transmission_record'][i]['mkr-l2m.ncupdate.com'], indent = 4, sort_keys=True))
    print (json.loads(json.dumps(data['transmission_record'][i]['time'])),json.loads(json.dumps(data['transmission_record'][i]['mkr-l2m.ncupdate.com'])))
print (" sum : ",sum)