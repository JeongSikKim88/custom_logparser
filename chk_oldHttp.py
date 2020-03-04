# from json_parser import parser
import json


with open('oldAPI_mkr_http.json') as data_file:
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
time = json.dumps(data['http_cache_status_record'].keys(), indent = 4, sort_keys=True)

print(type(time))

dickTime = json.loads(time)

# json_accept_string = dickTime.replace("',''/'")
# print(json_accept_string)
print(type(dickTime))

# sortTime = sorted(dickTime.items(),reverse=True)
dickTime.sort()
# print(dickTime)



# print(sortTime)

# print(time[0])

# end = dataLen-1
# print(end)

for i in range(0,288):
    a = dickTime[i]
    ######## status code ########
    # print (a,json.dumps(data['error_status_record'][a]["4xx"], indent = 4, sort_keys=True)) 
    ######## cache status #######
    print (a,json.dumps(data['http_cache_status_record'][a]["HIT"], indent = 4, sort_keys=True)) 
    
    # sum += int(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
    # print (json.dumps(data['error_status_record'][i]['time']),json.dumps(data['error_status_record'][i]['total']))
    # print (json.dumps(data['error_status_record'][i]['4xx']))
    # print (sum)
    # print (" sum : ",sum)