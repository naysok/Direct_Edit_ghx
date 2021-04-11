import datetime
import re


def get_current_time():
        return str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))


def get_current_time_yymmdd():
        return str(datetime.datetime.now().strftime("%Y-%m-%d"))


def change_ghx_filename(line):

    current_time = get_current_time()
    yymmdd = get_current_time_yymmdd()
    elm = re.split("[<>]", line)
    
    ### Define New Name
    old_name = elm[2]
    e = old_name.split(".")
    n = e[0]

    ### Include Timestamp
    if "_ts_" in n:
        nn = n.split("_ts_")
        n = nn[0]
    
    else:
        n = n
    
    new_name = "{}_ts_{}.ghx".format(n, current_time)
    new_line = "{}<{}>{}<{}>{}".format(elm[0], elm[1], new_name, elm[3], elm[4])
    
    # print(line)
    # print(new_line)
    
    return new_line, new_name


def change_ghx_scrible(line):

    current_time = get_current_time()
    elm = re.split("[<>]", line)
    # print(elm)
    
    ### Define New Text
    old_text = elm[2]
    add_text = "Add Timestamp with Python : {}".format(current_time)
    new_text = "{} / {}".format(old_text, add_text)
    # print(new_text)

    new_line = "{}<{}>{}<{}>{}".format(elm[0], elm[1], new_text, elm[3], elm[4])

    # print(line)
    # print(new_line)

    return new_line, None


def filter_filename_scrible(line):
    
    ### FileName
    s0 = '<item name="Name" type_name="gh_string" type_code="10">'

    ### Scrible
    s1 = '<item name="Text" type_name="gh_string" type_code="10">Hello World!!'

    if (s0 in line) and (".ghx" in line):
        return change_ghx_filename(line)

    elif s1 in line:
        return change_ghx_scrible(line)

    else:
        return line, None



########################################



ghx_path = input("Drag and Drop! : ")
# print(ghx_path)

tmp = ghx_path.split("\\")
for i in range(len(tmp)):

    if i < len(tmp) - 1:
        if i == 0:
            dir_path = tmp[0]
        else:
            dir_path = dir_path + "\\" + tmp[i]

dir_path = dir_path + "\\"
# print(dir_path)


new_ghx = []
new_name = []


### Read ghx
f = open(ghx_path, 'r')

lines = f.readlines()
for line in lines:
    new_line, n = filter_filename_scrible(line)
    new_ghx.append(new_line)
    new_name.append(n)

f.close()


### Remove None
new_name = [a for a in new_name if a != None]
new_name = new_name[0]

### Write ghx

new_ghx_path = dir_path + new_name
with open(new_ghx_path, mode='w') as f:
    f.writelines(new_ghx)


print("Export : {}".format(new_name))