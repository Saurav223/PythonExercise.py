def inbuilt(lst):
    lst.reverse()
    return lst

def slicing(lst):
    return lst[::-1]

def swapping(lst):
    for i in range(len(lst) // 2):  # // return integer insted of float i.e. no decimal
        lst[i],lst[len(lst)-i-1] = lst[len(lst)-i-1],  lst[i]
    return lst

lst = [3,45,3,35,6]
print(f"Before reversing \n {lst} \n After Reversing")

lst_copy1 = lst.copy()
lst_copy2 = lst.copy()
lst_copy3 = lst.copy()

print(f"After reversing with inbuilt: {inbuilt(lst_copy1)}")
print(f"After reversing with slicing: {slicing(lst_copy2)}")
print(f"After reversing with swapping: {swapping(lst_copy3)}")

            
            
