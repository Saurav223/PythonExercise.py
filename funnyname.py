import random 

def swapping(lst):
    final = []
    for i in range(len(lst)):
        ran = random.randint(0, len(lst) - 1)
        ran2 = random.randint(0, len(lst) - 1)
        tmp1 = lst[ran].split(' ')
        tmp2 = lst[ran2].split(" ")
        
        if len(tmp1) >= 3:
            tmp1.pop(2)
        
        if len(tmp2) >= 3:
            tmp2.pop(2)
        
        tmp1[0], tmp2[1]= tmp2[0], tmp1[1]
        final.append(tmp1[0] + tmp1[1])
        final.append(tmp2[0] + tmp2[1])
    
    return final
    
lst = ['Saurav Subedi', 'Ram hari', 'Shyram sigh']
print(swapping(lst))
