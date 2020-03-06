# from json_parser import parser
import json

### api call ###
### curl -X POST "https://skbapi.myskcdn.net/gtm/get-statistic/origin_status " -H "Authorization: Token bfd907cb63763422efdbf5cf71132470d7b01380" --data "format=json&date_from=2020-03-04&date_to=2020-03-04&domain_name=mkr-l2m.ncupdate.com" ###


with open('logs/json/20200304_oldAPI.json') as data_file:
    data = json.load (data_file)

i=0
sum = 0
for i in range(0,288):

    i+=1
    
    sum += int(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))

    print (json.loads(json.dumps(data['request_record'][i]['time'])),json.loads(json.dumps(data['request_record'][i]['total'])))
print (" sum : ",sum)