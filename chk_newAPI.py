# from json_parser import parser
import json


with open('logs/json/20200304_179_newAPI.json') as data_file:
    data = json.load (data_file)
    #jdata=json.dump(data, indent = 4, sort_keys=True)

# req=data['request_record']

### data list : concurrent_record, request_record, traffic_record, transmission_record ###
# print(json.dumps(data['request_record'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'][0]['total'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'][2]['total'], indent = 4, sort_keys=True))
#dataLen=len(json.dumps(data['request_record']))


#end = dataLen-1
# print(end)

i=0
sum = 0
for i in range(0,287):

    i+=1
    # print("count :", i)
    # print(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
    
    
    sum += int(json.dumps(data['transmission_record'][i]['mkr-l2m.ncupdate.com'], indent = 4, sort_keys=True))
    # print (json.loads(json.dumps(data['transmission_record'][i]['time'])),json.loads(json.dumps(data['transmission_record'][i]['total'])))
    print (json.loads(json.dumps(data['transmission_record'][i]['time'])),json.loads(json.dumps(data['transmission_record'][i]['mkr-l2m.ncupdate.com'])))
    # print (sum)
print (" sum : ",sum)