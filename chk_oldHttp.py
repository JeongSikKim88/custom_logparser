# from json_parser import parser
import json


with open('logs/json/20200304_oldAPI_status.json') as data_file:
    data = json.load (data_file)
    
    #jdata=json.dump(data, indent = 4, sort_keys=True)

# req=data['request_record']

# print(json.dumps(data['request_record'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'][0]['total'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'][2]['total'], indent = 4, sort_keys=True))
# dataLen=len(json.dumps(data['error_status_record']))
# print (json.dumps(data['error_status_record']["2020-02-25 23:35:00"]["4xx"], indent = 4, sort_keys=True))
# print (json.dumps(data['error_status_record'].keys(), indent = 4, sort_keys=True))
# print (json.dumps(data['error_status_record'].keys(), indent = 4, sort_keys=False))
time = json.dumps(data['origin_status_record'].keys(), indent = 4, sort_keys=True)

#print(type(time))

#print(time)

### convert to dictionary
dickTime = json.loads(time)
dickTime.sort()

print(dickTime[0])

test = json.dumps(dickTime, indent = 4, sort_keys=True)


sum=0
for i in range(0,288):
    #a = dickTime[i]
    ######## status code ########
    print (a,json.dumps(data['error_status_record'][a]["4xx"], indent = 4, sort_keys=True)) 
    ######## cache status #######
    print (a,json.dumps(data['http_cache_status_record'][a]["HIT"], indent = 4, sort_keys=True))
    for ip in range(0,10):
        sum+= json.dumps(data['origin_status_record'][a][ip]["200"], indent = 4, sort_keys=True)
    #print(a,sum)
    sum += int(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
    # print (json.dumps(data['error_status_record'][i]['time']),json.dumps(data['error_status_record'][i]['total']))
    # print (sum)
#print (" sum : ",sum)