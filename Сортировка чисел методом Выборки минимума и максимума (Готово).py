# Метод вставки. Начало.
size = int(input("Введите, пожалуйста, положительный целочисленный размер массива: "))
if size <= 0:
    print("Некорректный размер массива!")
else:
    i = 0
    arr = []
    while i < size: # Создание массива
        print("Введите, пожалуйста, " + str(i+1) + "-й числовой элемент массива: ")
        n = int(input())
        arr.append(n)
        i = i+1
    x = 0
    while x < (size-1):
        j = x+1
        while j < size: 
            if arr[x] > arr[j]:
                temp = arr[j]
                arr[j] = arr[x]
                arr[x] = temp
            j = j+1
        x = x+1
    print(arr)
# Метод вставки. Конец.
