import time
i = 10
while i >= 0:  # Включаем 0
    print(i)
    time.sleep(1)  # Правильный вызов sleep
    i -= 1
print("Время вышло!")  # Сообщение после цикла