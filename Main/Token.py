import json

token = "5950507768:AAG5OWXQtfIV2vVyskqOj0QBzIXS4zfEgeg"

with open("Admins.json", "r") as read_file:
    admin_list = json.load(read_file)

def adm_pls(ID):
    admin_list.append(ID)
    with open("Admins.json", "w") as write_file:
        json.dump(admin_list, write_file)

def adm_mns(ID):
    try:
        admin_list.remove(ID)
        with open("Admins.json", "w") as write_file:
            json.dump(admin_list, write_file)
    except:
        print("ERROR. NOT FOUND ID.")