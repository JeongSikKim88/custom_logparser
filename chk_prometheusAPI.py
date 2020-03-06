# from json_parser import parser
import json


with open('logs/json/20200304_227_pro.json') as data_file:
    data = json.load (data_file)

i=0
sum = 0
for i in range(0,287):

    i+=1
    # print("count :", i)
    # print(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
    
    
    # sum += float(json.dumps(data['data']['result'][0]['values'][i]), indent = 4, sort_keys=True))
    print (json.dumps(data['data']['result'][0]['values'][i]))
    # print (json.loads(json.dumps(data['transmission_record'][i]['time'])),json.loads(json.dumps(data['transmission_record'][i]['total'])))
    # print (json.loads(json.dumps(data['transmission_record'][i]['time'])),json.loads(json.dumps(data['transmission_record'][i]['total'])))
    # print (sum)
# print (" sum : ",sum)