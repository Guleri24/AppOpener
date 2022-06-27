import os, json, re

main_path = os.path.dirname(__file__)

check_reference_file = os.path.exists(os.path.join(main_path,"reference_temp.txt"))
check_json_list = os.path.exists(os.path.join(main_path,"apps_list.json"))
check_reference = os.path.join(os.path.join(main_path,"reference.txt"))

def convert_txt_json():
    dictionary ={}
    json_object = json.dumps(dictionary, indent = 4)
    with open((os.path.join(main_path,"apps_list.json")),"w") as outfile:
        outfile.write(json_object)
    file1 = open(os.path.join(main_path,'reference_temp.txt'),'r')
    Lines = file1.readlines()
    for line in Lines:
        line1= line.strip()
        index = line1.find('  ')
        # HERE line1[:index] is the APP-NAME
        # HERE line1[index:] is the APP-ID.
        app_name = line1[:index]
        app_id = (line1[index:]).strip()
        is_digit = app_name[:1].isdigit()
        with open ((os.path.join(main_path,"apps_list.json")),"r") as f:
                data = json.load(f)
        if is_digit == (False):
            val=(re.compile(r'[^a-z-&]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open((os.path.join(main_path,"apps_list.json")),"a+") as f:
                g = open((os.path.join(main_path,"apps_list.json")),"w")
                g.truncate(0)
                json.dump(data,f,indent=4)
        elif is_digit == (True):
            val=(re.compile(r'[^a-z-&^0-9]')).sub(" ",(app_name.lower()))
            final_app_name = re.sub(' +', ' ', val).strip()
            change = {final_app_name:app_id}
            data.update(change)
            with open((os.path.join(main_path,"apps_list.json")),"a+") as f:
                g = open((os.path.join(main_path,"apps_list.json")),"w")
                g.truncate(0)
                json.dump(data,f,indent=4)
                
def blank_lines_check():
    with open((os.path.join(main_path,"reference_temp.txt")),"r") as fd:
        lines = fd.readlines()
    line = []
    with open((os.path.join(main_path,"reference_temp.txt")),"w") as fp:
        for number, line in enumerate(lines):
            if number not in [0, 1,2]:
                fp.write(line)
    with open((os.path.join(main_path,"reference_temp.txt")),"r") as f, open((os.path.join(main_path,"reference.txt")),"w") as outfile:
        for i in f.readlines():
            if not i.strip():
                continue
            if i:
                outfile.write(i) 
                
if check_reference_file == (False):
    command = (("powershell -command "+'"'+"&"+" {&"+"'"+"get-StartApps"+"'"+"}"+'" > ')+'"'+(os.path.join(main_path,"reference_temp.txt"))+'"')
    execute_command = os.system(command)
    if check_reference == (False):
        open((os.path.join(main_path,"reference.txt")),"w").close()
    blank_lines_check()
    
if check_json_list == (False):
    convert_txt_json()
    
print("DATA LOADED, now you can RUN APPS!!!")

