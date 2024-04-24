import json
import csv
import io

DATA_ROOT='./'
# get the JSON objects from JSONL
with open(f"{DATA_ROOT}eval/data_llm.jsonl", "r") as file, \
    open(f"{DATA_ROOT}eval/test.jsonl", 'w', newline='') as jsonFile:
    json_lines = list(file)
    print(len(json_lines))
    # json_lines = tuple(json_line
    #                 for json_line in jsonl_data.splitlines()
    #                 if json_line.strip())
    jsons_objs = tuple(json.loads(json_line)
                    for json_line in json_lines)
    for j in jsons_objs:
        j['description'] = j['description'].replace('\n','')
        # j['keywords'] = j['keywords'].replace('\n','')
    for j in jsons_objs:
        if '\n' in j['description']:
            print(j['description'])
        jsonFile.write(json.dumps(j) + '\n')
        # print(j['keywords'])
    # print(jsons_objs[0]['description'])

    # data = json.loads(json_str)
    # # write them into a CSV file
    # fake_file = io.StringIO()
    # # fake_file = 'test.csv'
    # writer = csv.writer(jsonFile, delimiter=';')
    #                         # quotechar='', quoting=csv.QUOTE_MINIMAL)
    # # writer = csv.writer(fake_file)
    # writer.writerow(["key", "artist", "sample_rate", "file_extension", "description", "keywords", "duration","bpm", "genre", "title","name", "instrument","moods", "path"])
    # writer.writerows((str(value).replace('\n','') for key, value in json_obj.items())
    #                 for json_obj in jsons_objs)
    # csvfnt(fake_file.getvalue())

