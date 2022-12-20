token = ""
admin_list = []

def adm_pls(ID):
    admin_list.append(ID)

def adm_mns(ID):
    try:
        admin_list.remove(ID)
    except:
        print("ERROR. NOT FOUND ID.")