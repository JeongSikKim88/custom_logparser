# from json_parser import parser
import json


with open('oldAPI_nclauncherw.json') as data_file:
    data = json.load (data_file)
    #jdata=json.dump(data, indent = 4, sort_keys=True)

# req=data['request_record']

# print(json.dumps(data['request_record'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'][0]['total'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'][2]['total'], indent = 4, sort_keys=True))

# print(len(json.dumps(data['request_record'])))
# dataLen=len(json.dumps(data['request_record']))
# dataLen=len(json.dumps(data['transmission_record']))


# end = dataLen-1

i=0
sum = 0
for i in range(0,288):

    i+=1
    # print("count :", i)
    # print(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
    


    # transmission = json.loads(json.dumps(data['transmission_record'][i]['total']))
    # trans = json.loads(transmission)

    # print (transmission)
    
    # sum += int(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
    # print (json.dumps(data['request_record'][i]['time']),json.dumps(data['request_record'][i]['total']))

    print (json.loads(json.dumps(data['transmission_record'][i]['time'])),json.loads(json.dumps(data['transmission_record'][i]['total'])))
    # print (sum)
    # print (" sum : ",sum)