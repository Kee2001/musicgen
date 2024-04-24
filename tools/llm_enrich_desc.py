DATA_ROOT='./'
import json
import ollama

MODEL='codellama:7b-instruct' 
MODEL='mistral:7b-instruct' 

with open(f"{DATA_ROOT}train/data.jsonl", "r") as file, \
    open(f"{DATA_ROOT}train/data_llm.jsonl", "a") as llm_file, \
    open(f"{DATA_ROOT}train/data_llm.jsonl", "r") as read_llm_file:
    json_list = list(file)
    curr_llm_length = len(list(read_llm_file))
    prompt = '''I would like to enrich info in “keywords” field and provide a natural language information as detail as possible in the "description" using other tags. Do not include any explanations, only provide a JSON response following this format without deviation:
    {"description": ..., "keywords": ..., }. The reference json source: 
    '''
    # print(json_list[452])
    # exit()
    idx = curr_llm_length
    while idx < len(json_list):
        print('---------------------------------------------- idx', idx)
        json_str = json_list[idx]
        data = json.loads(json_str)
        print(prompt + json_str + '\nThe JSON response: \n')
        response = ollama.chat(model=MODEL, messages=[
        {
            'role': 'user',
            'content': prompt + json_str + '\nThe JSON response: \n',
        },
        ])
        r = response['message']['content']
        print(r)
        try:
            r_dict = json.loads(r.replace('\'','\"'))
            idx +=1
        except: # Try again
            print('Try again at idx', idx)
            continue
        print(r_dict['description'])
        print(r_dict['keywords'])
        data['description'] = r_dict['description'].replace('\n','')
        data['keywords'] = r_dict['keywords']
        llm_file.write(json.dumps(data) + '\n')

    # keyword = ''
    # description = 'laama'

