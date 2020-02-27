# from json_parser import parser
import json

def chk_old():
    with open('oldAPI.json') as data_file:
        data = json.load (data_file)
        #jdata=json.dump(data, indent = 4, sort_keys=True)

    # req=data['request_record']

    # print(json.dumps(data['request_record'], indent = 4, sort_keys=True))
    # print(json.dumps(data['request_record'][0]['total'], indent = 4, sort_keys=True))
    # print(json.dumps(data['request_record'][2]['total'], indent = 4, sort_keys=True))


    i=0
    global oldSum
    oldSum=0
    for i in range(9,22):

        i+=1
        # print("count :", i)
        # print(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
        
        
        oldSum += float(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
        # print (json.dumps(data['request_record'][i]['time']),json.dumps(data['request_record'][i]['total']))
        # print (sum)
        # print (" sum : ",oldSum)

def chk_new():
    with open('newAPI.json') as data_file:
        data = json.load (data_file)
        #jdata=json.dump(data, indent = 4, sort_keys=True)

    # req=data['request_record']

    # print(json.dumps(data['request_record'], indent = 4, sort_keys=True))
    # print(json.dumps(data['request_record'][0]['total'], indent = 4, sort_keys=True))
    # print(json.dumps(data['request_record'][2]['total'], indent = 4, sort_keys=True))


    i=0
    global newSum
    newSum =0
    for i in range(10,23):

        i+=1
        # print("count :", i)
        # print(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
        
        
        newSum += float(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
        # print (json.dumps(data['request_record'][i]['time']),json.dumps(data['request_record'][i]['total']))
        # print (sum)
        # print (" sum : ",newSum)


def percent():
    chk_old()
    print("oldSum : ",oldSum)
    chk_new()
    print("newSum : ", newSum)
    
    print((oldSum-newSum)/newSum)
    print(float((oldSum-newSum)/newSum*100))

    print("error_percentage : ", float((oldSum-newSum)/newSum*100))

if __name__ == "__main__":
    # chk_old()
    # chk_new()
    percent()
