import time
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list) and int(my_list[i]) >= 0:
    if int(my_list[i]) > 0:
        print(my_list[i])
        time.sleep(1)
        i += 1
    else:
        i += 1