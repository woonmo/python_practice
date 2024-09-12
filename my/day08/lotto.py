import random as rnd

lotto :str  = ""
lotto_num   = []
compare     = []
rnd_no :int = 0

for i in range(0,45):
    lotto_num.append(i+1)

for i in range(0,6):
    
    rnd_no = rnd.randrange(1,45)
    
    for j in range(len(compare)):
        
        if (compare[j] == rnd_no):
            i = i-1
            break
    # end of for () -------------
    
    if (i<5):
        compare.append(rnd_no)
        add = ","
    else:
        add = ""    
    lotto += str(lotto_num[rnd_no]) + add
# end of for () -------------

print("로또 당첨 번호 :",  lotto)