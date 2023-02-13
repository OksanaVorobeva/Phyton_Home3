#Первая задача:
#Задаем длину списка наполненного рандомными числами от 1 до 100.
#Вводим искомое число X
#Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
#которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
number=int(input("Введите длину списка "))
my_list=[]
for i in range(number):
    my_list.append(random.randint(1,100))
print(my_list)
x=int(input("Введите x "))
count=0

for i in range(1,len(my_list)):
    if x==my_list[i]:
        count+=1   
print(f"встречается в заданном списке искомое число X {count}")
for i in range(1,len(my_list)):
    if x!=my_list[i]:
        j=0
        while x==my_list[j]:
            j+=1
        seach_num=my_list[i]
        for list in my_list:
            if list!=x:
                if abs(list-x)<abs(seach_num-x):
                    seach_num=list
print(f"Ближайщее число к числу {x} это {seach_num}")
                
              

