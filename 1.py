def task(array):
    for i in range(len(array)):
        if array[i] == "0" or array[i] == 0:
            # В тестовом задании было сказано, что на вход подается массив чисел, хотя в task передается строка,
            # поэтому в if я решил добавить еще одно условие
            return i

print(task("111111111110000000000000000"))
print(task([1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]))