list1 = [1, 5, 4, 4, 5, 1, 2, 3]


def function(list):
    for i in range(len(list[:-2])):
        if list[i] == 1 and list[i + 1] == 2 and list[i + 2] == 3:
            return True
    return False


print(function(list1))
