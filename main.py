import sys
import csv
import os

def main():
    user_list = read_csv(sys.argv[1])

    # Create OU

    ou_list = list(set([user["OU"] for user in user_list]))

    for ou in ou_list:
        create_ou(ou)

    # Create User

    for user in user_list:
        create_user(user["First Name"], user["Last Name"], user["Role"], user["Phone"], user["OU"], user["Password"])
    

def read_csv(file):
    with open(file, mode='r', encoding='windows-1252') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        return [i for i in csv_reader]

def create_ou(ou_name):
    os.system(f"samba-tool ou create {ou_name}")

def create_user(f_name, l_name, role, phone, ou, password):
    os.system(f"samba-tool user create {f_name.lower()}.{l_name.lower()} {password} --given-name {f_name} --surname {l_name} --job-title {role} --telephone-number {phone} --userou OU={ou}")

if __name__ == "__main__":
    main()
