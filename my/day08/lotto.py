import random as rnd

lotto = ""
lotto_num = []
compare =[]
rnd_no=0

for i in range(0,45):
    lotto_num.append(i+1)

for i in range(0,6):
    
    rnd_no = rnd.randrange(1,45)
    
    for j in range(len(compare)):
        
        if (compare[j] == rnd_no):
            i = i-1
            break
        # end of if() -----------
    # end of for () -------------
    
    if (i<5):
        compare.append(rnd_no)
        add =","
    else:
        add = ""
    # end of if () ---------------    
    lotto += str(lotto_num[rnd_no]) + add
# end of for () -------------

print("로또 당첨 번호 : ",  lotto)