# Найдите сумму цифр трехзначного числа

number = int(input("Введите трехзанчное число: "))
if(number>999 or number<100):
    print("Вы ввели не трехзначное число!")
else:
    print(f"{(number//100%10)+(number//10%10)+(number%10)} ({(number//100%10)} + {(number//10%10)} + {(number%10)})")