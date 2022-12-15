answ1 = input("Вы голодны? ")
answ2 = input("Вам холодно? ")
if answ1 == "да" and answ2 == "да":
    print("Вам голодно и холодно")
elif answ1 == "да" and answ2 == "нет":
    print("Ну хотя бы не замёрзните")
elif answ1 == "нет" and answ2 == "да":
    print("Скоро согреетесь")
elif answ1 == "нет" and answ2 == "нет":
    print("Ну это ГГ")
else:
    print("Вы ввели не верный ответ")