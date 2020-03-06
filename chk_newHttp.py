# from json_parser import parser
import json


with open('logs/json/20200304_newAPI_status.json') as data_file:
    data = json.load (data_file)
    
time = json.dumps(data['error_status_record'].keys(), indent = 4, sort_keys=True)

dickTime = json.loads(time)

# sortTime = sorted(dickTime.items(),reverse=True)
dickTime.sort()
# print(dickTime)

sum=0
for i in range(0,288):
    a = dickTime[i]
    ######## status code ########
    # print (a,json.dumps(data['error_status_record'][a]["4xx"], indent = 4, sort_keys=True)) 
    ######## cache status #######
    #print (a,json.dumps(data['error_status_r/ecord'][a]["hit"], indent = 4, sort_keys=True)) 
    print (a,json.dumps(data['error_status_record'][a]["2xx"], indent = 4, sort_keys=True)) 
    
    sum += int(json.dumps(data['error_status_record'][a]['2xx'], indent = 4, sort_keys=True))
    # print (json.dumps(data['error_status_record'][i]['time']),json.dumps(data['error_status_record'][i]['total']))
    # print (json.dumps(data['error_status_record'][i]['4xx']))
    # print (sum)
print (" sum : ",sum)