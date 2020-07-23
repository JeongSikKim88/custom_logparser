import json # import json module


def parser():
    with open('getnode.out') as json_file:
        # print(type(json_file))
        json_data = json.load(json_file)
        # print(json_data)
        print(type(json_data))

    with open('logs/json/20200304_newAPI.json','w') as out_file:
        a=json.dump(json_data, out_file, indent = 4, sort_keys=True)
        print(type(a))
        #json.dump('example.json', json_file)
        #json_data = json.load(json_file)
        b=json.dumps(json_data, indent = 4, sort_keys=True)
        print(type(b))
        print(b)
        c=json.loads(b)
        print(type(c))
        print(c)
        # print(json.dumps(json_data, indent = 4, sort_keys=True))
        #print(json.dump)


parser()