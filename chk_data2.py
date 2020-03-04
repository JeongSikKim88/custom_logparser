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
    for i in range(21,33):

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
    for i in range(22,35):

        i+=1
        # print("count :", i)
        # print(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
        
        
        newSum += float(json.dumps(data['request_record'][i]['total'], indent = 4, sort_keys=True))
        # print (json.dumps(data['request_record'][i]['time']),json.dumps(data['request_record'][i]['total']))
        # print (sum)
        # print (" sum : ",newSum)


def percent():
    chk_old()
    print("oldSum : ", oldSum)
    chk_new()
    print("newSum : ", newSum)


    # print(oldSum-newSum)
    print((oldSum-newSum)/newSum)
    
    error = ((oldSum-newSum)/newSum)*100

    # print(error)

    print("error_percentage : ", round((oldSum-newSum)/newSum*100,4))

if __name__ == "__main__":
    # chk_old()
    # chk_new()
    percent()





