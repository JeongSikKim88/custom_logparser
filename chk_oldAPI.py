# from json_parser import parser
import json

### api call ###
### curl -X POST "https://skbapi.myskcdn.net/gtm/get-statistic/origin_status " -H "Authorization: Token bfd907cb63763422efdbf5cf71132470d7b01380" --data "format=json&date_from=2020-03-04&date_to=2020-03-04&domain_name=mkr-l2m.ncupdate.com" ###


with open('logs/json/20200304_oldAPI.json') as data_file:
    data = json.load (data_file)
    #jdata=json.dump(data, indent = 4, sort_keys=True)

# req=data['request_record']

### data list : concurrent_record, request_record, traffic_record, transmission_record ###
# print(json.dumps(data['request_record'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'], indent = 4, sort_keys=True))


# print(json.dumps(data['request_record'][0]['total'], indent = 4, sort_keys=True))
# print(json.dumps(data['request_record'][2]['total'], indent = 4, sort_keys=True))

# print(len(json.dumps(data['request_record'])))


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
    
    sum += int(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
    # print (json.dumps(data['request_record'][i]['time']),json.dumps(data['request_record'][i]['total']))

    print (json.loads(json.dumps(data['request_record'][i]['time'])),json.loads(json.dumps(data['request_record'][i]['total'])))
    # print (sum)
print (" sum : ",sum)