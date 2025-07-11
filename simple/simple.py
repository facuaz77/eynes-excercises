import random

def simple_list():
    users = []
    for i in range(1, 11):  
        user = {
            'id': str(i),
            'age': random.randint(1, 100)  
        }
        users.append(user)
    return users


def sort_list(dicts):
    return sorted(dicts, key=lambda user: user['age'])
    

users = simple_list()

for user in sort_list(users):
    print(user)