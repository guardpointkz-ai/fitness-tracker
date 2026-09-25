print("Здравствуйте!")
steps = int(input("Шаги за день "))
calories = int(input("Калории "))
water_ml = int(input("Вода мл "))
sleep_hours = float(input("Сон ч "))
# Цели
water_goal = 2000
steps_goal = 10000
calories_goal = 2000
sleep_hours_goal = 8
# Расчет процентов
water_percent = round(water_ml / water_goal * 100, 1)
steps_percent = round(steps / steps_goal * 100, 1)
calories_percent = round(calories / calories_goal * 100, 1)
sleep_hours_percent = round(sleep_hours / sleep_hours_goal * 100, 1)
if calories_percent > 100:
    print("Превышение нормы")
elif calories_percent >= 90:
    print("Цель почти достигнута")
else:
    print("Нужно доесть норму") 
# Итоговый отчет
print("==ОТЧЕТ==")
print(f'''Процент от цели по воде {water_percent}%
Процент от цели по шагам в день {steps_percent}%
Процент от цели по калориям {calories_percent}%
Процент от цели по сну {sleep_hours_percent}%''')