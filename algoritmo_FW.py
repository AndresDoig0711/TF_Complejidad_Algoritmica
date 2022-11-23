list = [0,1,2,3,2,8,7,8,11]
list1 = [0,1,2,3,0,5,6,7,7]
list2 = [0,1,2,3,0,5,6,7,7,8,1]

new_list = []

for i in list:
    if i != list[len(list)-1]:
        if i not in new_list:
            new_list.append(i)
            print(new_list)
            j = len(new_list)-1
        else:
            if new_list[j] != i:
                new_list.remove(new_list[j])
                while new_list[j-1] != i:
                    new_list.remove(new_list[j-1])
                    j -= 1    
            print(new_list)
    else:
        if i not in new_list:
            new_list.append(i)
            print(new_list) 
        break

print(new_list)