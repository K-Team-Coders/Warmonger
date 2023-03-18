import json

def user_agent_randomizer(file_name):
    number_array = []
    user_agent_list = []
    with open(file_name, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            
            user_agent_list.append({'id': i, 'user_agent':lines[i][:lines[i].find('\t')]})
        x = json.dumps(user_agent_list)
        f.write(x)
        


      

user_agent_randomizer('user-agents_copy.json')