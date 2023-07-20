# base_list - база данных как SQL, не может хранить классы , функции и методы храниться где то на сервере


# registered_users - обработанная база данных с сервера, хранит в себе весь функционал пользователей, модераторов и админа

# registered_users = [
    
# ]
# '[{"first_name" : "Денис","last_name" : "Кириллов","birthday" : "01.06.2001","gender" : "Мужской","login" : "denis161","password" : "12345"},]'
# # r - только чтение файла read()
# # w - перезапись write()
# # a - добавить в конец файла текст wtite()
# # + - чтение и запись
# fileW = open("text.txt","w",encoding="utf-8")
# fileW.write("Новый текст2\n")
# fileW.write("Новый текст2")
# fileW.close()

# fileR = open("text.txt","r",encoding="utf-8")
# print(fileR.read())
# fileR.close()
# открыли файл с возможностью чтения 
import json
base_list = open("base.json","r",encoding="utf-8")
# открыли файл на чтение
base_list_read = base_list.read()
new_base = json.loads(base_list_read)
new_base.append({
        "first_name": input(),
        "last_name": "",
        "birthday": "17.08.2021",
        "gender": "Мужской",
        "login": "dog",
        "password": "12345"
    })
print(new_base[5])
dumps_base = json.dumps(new_base,ensure_ascii=False)
file = open("base.json", "w", encoding="utf-8")
file.write(dumps_base)
# primer = '[{"first_name" : "Denis", "age" : 22},{"first_name" : "Masha", "age" : 18}]'
# print(primer[0])
# massiv = json.loads(primer)
# print(massiv[0])