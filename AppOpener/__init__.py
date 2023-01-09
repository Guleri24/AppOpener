__version__ = "1.6"
from . import check, update_list, commands, features
import os, re

# Checking if required files exists or not
check.check_json()
check.app_names()

# Get the path of working directory
main_path = os.path.join((check.get_path()), "Data")

# REDIRECTED FUNCTION FOR SIMPLIFICATION
def give_appnames(upper=False):
    if upper:
        upper = True
    keys = features.give_appnames(upper=upper)
    return keys

# For making list
def mklist(name=None, path=None, output=True):
    '''
    Hello
    '''
    name = name
    path = path
    output = output
    features.mklist(name=name, path=path, output=output)

# Run application (Regex implemented)
def run(self, output=True):
    print()
    print("'RUN' FUNCTION IS REPLACED BY 'OPEN' FUNCTION")
    print("TRY USING 'OPEN(app_name)'")
    print()

# Open application (Regex implemented)
def open(self, output=True, match_closest=False):
    if not output:
        output = False
    if match_closest:
        match_closest = True
    inp = (self).lower()
    val=(re.compile(r'[^a-zA-Z-^0-9?,>&]').sub(" ",inp)).strip()
    if val == (""):
        pass
    elif val == ("cls"):
        os.system("cls")
    elif val == ("version"):
        print("AppOpener version "+__version__)
    elif inp == ("?"):
        invsys = '"'
        os.system(f"explorer {invsys}https://appopener.readthedocs.io/en/latest/{invsys}")
    elif val == ("help"):
        print()
        commands.commands()
        print()
    elif val == ("ls"):
        features.list_apps()
    elif val == ("rename -m"):
        os.startfile(os.path.join(main_path,"app_names.json"))
        print("RELOAD PROGRAM TO APPEND CHANGES")
    elif val == ("update"):
        update_list.update(output=output)
    elif " > " in val:
        update_list.do_changes_cli(val)
        update_list.check_new_name()
        update_list.pre_change()
        update_list.modify()
    elif val == ("default"):
        update_list.default(output=output)
        update_list.check_new_name()
        update_list.pre_change()
        update_list.modify()
    elif val == "mklist":
        mklist(output=output)
    elif "find " in val:
        print()
        val2 = val.replace("find ","")
        if "," in val2:
            splited = val2.split(",")
            for i in splited:
                j = i.strip()
                if j != "":
                    features.find_apps(j)
        else:
            features.find_apps(val2)
        print()
    elif val == "log -c" or val == "log":
        print()
        val2 = val.replace("log -","")
        features.change_log(val)
        print()
    else:
        if "," in val:
            splited = val.split(",")
            for i in splited:
                j = i.strip()
                if j != "":
                    features.open_things(j, output=output, match_closest=match_closest)
        else:
           features.open_things(val, output=output, match_closest=match_closest)

# Close any application by just its name :)
def close(self, output=True, match_closest=False):
    if not output:
        output = False
    if match_closest:
        match_closest = True
    inp = (self).lower()
    val=(re.compile(r'[^a-zA-Z-^0-9?,>&+.]').sub(" ",inp)).strip()
    if "," in val:
        splited = val.split(",")
        for i in splited:
            j = i.strip()
            if j != "":
                features.close_things(j, output=output, match_closest=match_closest)
    else:
        features.close_things(val, output=output, match_closest=match_closest)
