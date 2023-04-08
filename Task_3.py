# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

len_ticket = 6
ticket = input("Введите шестизначный номер билета: ")
if(len(ticket) != len_ticket):
    print("Вы ввели не шестизначный номер билета.")
else:
    sum_left = int(ticket[0:1])+int(ticket[1:2])+int(ticket[2:3])
    sum_right = int(ticket[3:4])+int(ticket[4:5])+int(ticket[5:6])
    if(sum_left == sum_right):
        print("yes")
    else:
        print("no")