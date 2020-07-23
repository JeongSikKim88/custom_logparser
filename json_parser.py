import json # import json module


def parser():
    with open('sample.json') as json_file:
        json_data = json.load(json_file)

    # with statement
    with open('sample2.json','w') as out_file:
        json.dump(json_data, out_file, indent = 4, sort_keys=True)
        #json.dump('example.json', json_file)
        #json_data = json.load(json_file)
        print(json.dumps(json_data, indent = 4, sort_keys=True))
        #print(json.dump)

#with open()

parser()
