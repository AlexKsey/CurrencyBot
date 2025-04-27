import time

# Получаем текущее время в виде структуры struct_time
current_time = time.localtime()

# 1. Текущее время в формате ЧЧ:ММ:СС
print("Текущее время:", time.strftime("%H:%M:%S", current_time))

# 2. Только минуты
print("Только минуты:", time.strftime("%M", current_time))

# 3. Только дата (день месяца)
print("Только дата (день):", time.strftime("%d", current_time))

# 4. Только месяц (число)
print("Только месяц (число):", time.strftime("%m", current_time))

# Дополнительно: месяц текстом
print("Месяц (название):", time.strftime("%B", current_time))