# азработай систему управления учетными записями пользователей для небольшой
# компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов
# ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа
# и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы
# (например, get и set методы).


#сделала списки двумя способами:
# 1)user_list добавление в список в виде словаря(не работает!!),
# потому что тогда при изменении атрибута пользователя в классе User не меняется конечный список.
#2)user_list_original добавление в список самих обьектов класса User- работает



class User:

    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._access = 'user'

    def get_user_name(self):
        #print(f"user name for User ID {self._id} is {self._name}")
        return self._name

    def get_user_id(self):
        #print(f"user id for {self._name} is {self._id}")
        return self._id


    def get_user_access(self):
        #print(f"access level for {self._name} is {self._access}")
        return self._access


    def set_user_name(self, new_name):
        print(f"Old user name for User ID {self._id} is {self._name}")
        self._name = new_name
        print(f"user name for User ID {self._id} has been changed to {self._name}")


class Admin(User):

    def __init__(self,id,name):
        super().__init__(id, name)
        self._access = 'admin'


    def add_user(self,user):
        user_list_original.append(user)
        user_list.append({"user_id":user._id, "user_name":user._name,"user_access":user._access})
        print(f"user {user._name} with User ID {user._id} has been successfully added to the user list as {user._access}")

    def show_user_list(self):
        print(user_list)
        for user in user_list_original:
            print(user.get_user_id(), user.get_user_name(), user.get_user_access())

    def remove_user_original (self,name=None,id=None):
        for user in user_list_original:
            if name and user._name.lower() == name.lower():
                user_list_original.remove(user)
                print(f"user {user._name} has been removed from the original list")
                return
            elif id and user._id == id:
                user_list_original.remove(user)
                print(f"user {user._id} has been removed from the list")
                return
            else:
                print(f"no such user with Name {user._name} or User ID {user._id} has been found in the list ")


    def remove_user(self,name=None,id=None):
        for user in user_list:
            if name and user["user_name"].lower() == name.lower():
                user_list.remove(user)
                print(f"user {user["user_name"]} has been removed from the list")
                return
            elif id and user['user_id'] == id:
                user_list.remove(user)
                print(f"user {user["user_id"]} has been removed from the list")
                return
            else:
                print(f"no such user with Name {user["user_name"]} or User ID {user["user_id"]} has been found in the list ")
    def make_user_admin_original(self, name=None, id = None):
        for user in user_list_original:
            if (name and user._name.lower() == name.lower()) or (id and user._id == id):
                user._access = "admin"
                print(f"{user._name} became an admin in the original list")
    def make_user_admin(self, name=None, id = None):
        for user in user_list:
            if (name and user["user_name"].lower() == name.lower()) or (id and user['user_id'] == id):
                user["user_access"] = "admin"
                print(f"{user["user_name"]} became an admin")


user_list = []
user_list_original=[]

user1 = User("123","Anna")
user2 = User("111","Boris")
user3 = User("122","Eva")
admin = Admin("100", "George")
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(admin)

admin.show_user_list()

admin.remove_user(name="Anna")
admin.remove_user_original(name="Anna")

admin.show_user_list()

admin.remove_user(id="111")
admin.remove_user_original(id="111")


admin.show_user_list()

admin.make_user_admin(name="Eva")
admin.make_user_admin_original(name="Eva")

admin.show_user_list()

user3.get_user_id()
user3.get_user_name()
user3.get_user_access()
user3.set_user_name("Kris")
admin.show_user_list()

