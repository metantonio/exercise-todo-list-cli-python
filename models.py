from base64 import b64encode
import os
import sys

#reload(sys).setdefaultencoding("ISO-8859-1")

class Base():
    self.id= b64encode(os.urandom(32).decode('utf-8'))

class UserList(Base):

    def __init__(self, name):
        super().__init__()
        self.name=name

    def create():
        pass

    def add_task():
        pass

    def complete_task():
        pass

    def delete_task():
        pass

    def print_list():
        pass

    def delete():
        pass

    def serialize():
        return {
            "id": self.id,
            "name":self.name,
        }

class Task(Base):

    def __init__(self, label, user_list_id):
        super().__init__()
        self.label=label
        self.done=False
        self.result=None
        self.user_list_id=user_list_id
    
    def serialize(self):
        return{
            "id":self.id,
            "user_list_id":self.user_list_id,
            "label":self.label,
            "done":self.done,
            "result":self.result if self.result is not None else ""
        }
    
def load_user():
    """ carga todos los diccionarios del archivo users_lists.json
    y crea instancias de UserList con estos diccionarios
    """ 
    if os.path.isfile(os.path.join(os,getcwd(), "user_list.json")):
        #existe, abrimos el archivo
        users_list_dictionaries = []
        with open(os.path.join(os.getcwd(), "user_list.json"), "r") as users_file:
            user_list_dictionaries = json.load(user_file)
        for dictionay in user_list_dictionaries:
            new_user = UserList(dictionary["Name"])
            new_user.id = dictionary["id"]
            users.append(new_user)
        return users  
    else:
        return users   

# new_user=UserList("metantonio")
# print(new_user.serialize())
# new_task = Task("hacer cfe", new_user.id)
# print(new_task.serialize)
users = load_user()
orint([user.serialize() for user in users])