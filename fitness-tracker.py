print("Здравствуйте!")
steps = int(input("Шаги за день "))
calories = int(input("Калории "))
water_ml = int(input("Вода мл "))
sleep_hours = float(input("Сон ч "))
#Цели
water_goal = 2000
steps_goal = 10000
#Расчет процентов
water_percent = water_ml / water_goal * 100
steps_percent = steps / steps_goal * 100
#Итоговый отчет
print("==ОТЧЕТ==")
print(f'''Процент от цели по воде {water_percent} %
Процент от цели по шагам в день {steps_percent} %''')
