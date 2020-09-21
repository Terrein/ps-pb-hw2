account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

input_value = input("Введите ключ (name или account): ").lower()

name_value = (f"значение ключа name для юзера 1 = {user1['name']}\n" +
              f"значение ключа name для юзера 2 = {user2['name']}\n" +
              f"значение ключа name для юзера 3 = {user3['name']}\n" +
              f"значение ключа name для юзера 4 = {user4['name']}")

account_value = (f"значение ключа login для юзера 1 = {account1['login']}\n" +
                 f"значение ключа login для юзера 2 = {account2['login']}\n" +
                 f"значение ключа login для юзера 3 = {account3['login']}\n" +
                 f"значение ключа login для юзера 4 = {account2['login']}")

if input_value == 'name':
    print(name_value)
elif input_value == 'account':
    print(account_value)
else:
    print("Введенный ключ не найден")

serial_number = int(input("Введите порядковый номер: "))

sum_age = 0
for i in user_list:
    sum_age += i['age']

avarage_age = sum_age/len(user_list)

user_index = 0

if serial_number > 4:
    print("Пользователь с указанным номером не найден")
else:
    user_index = serial_number - 1
    user_inf = (f"Данные по юзеру № {serial_number}: \n" +
                f"Имя: {user_list[user_index]['name']}\n" +
                f"Возраст: {user_list[user_index]['age']}\n" +
                f"Логин: {user_list[user_index]['account']['login']}\n" +
                f"Пароль: {user_list[user_index]['account']['password']}\n" +
                f"Пароль: {user_list[user_index]['account']['password']}\n" +
                f"Средний возраст пользователей: {avarage_age}")
    print(user_inf)

change_place = int(
    input("Введите номер пользователя, которого нужно переместить в конец: "))

user_numb = 0
new_user_list = user_list
if change_place > 4:
    print("Пользователь с указанным номером не найден")
else:
    user_numb = change_place - 1
    print(f"Список до изменений: \n" + f"{user_list}")
    print(
        f"Пользователь с именем : {new_user_list[user_numb]['name']} перемещен в конец")
    replace_el = new_user_list.pop(change_place - 1)
    new_user_list.append(replace_el)
    print(f"Список после изменений: \n" + f"{new_user_list}")
