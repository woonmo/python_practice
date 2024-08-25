
result = ""
star = "*"
'''
== 숙제 1 == 
*
**
***
****
*****

'''
print("=== 별찍기 1 ===")

for i in range(0,5):
    result += star
    print(result)
# end of for() ----------    

'''
== 숙제 2 == 
	      *
	     **
	    ***
	   ****
	  ***** 
'''

print("=== 별찍기 2 ===")
result = ""

for i in range(0,5):
    result += star
    print(result.rjust(12))
# end of for() ----------

print("=== 별찍기 3 ===")
result = ""
cnt = 5

for i in range(0,5):
    result = ""
    
    for j in range(cnt):
        result += star 
    # end of for() --------
    
    cnt = cnt-1
    print(result)
# end of for() -----------    
'''
	      == 숙제 4 ==
	     
	          *
	         ***
	        ***** 
'''
print("=== 별찍기 4 ===\n")
result = ""
cnt = 1

for i in range(0,3):
    result = ""
    
    for j in range(cnt):
        result += star
    # end of for() --------
    
    cnt = cnt+2
    print(result.center(15))
# end of for() --------

'''
         == 숙제 5 ==
	              
	        *****
	         ***
	          *
'''

print("=== 별찍기 5 ===\n")
result = ""
cnt = 5

for i in range(0,3):
    result = ""

    for j in range(cnt):
        result += star
    # end of for () --------
    
    cnt = cnt-2
    print(result.center(15))
 # end of for () --------

'''
         == 숙제 6 ==
	           
	          *
	         ***
	        *****
	         ***   
	          * 
'''

print("=== 별찍기 6 ===\n")
result = ""
cnt = 1
cnt2 = 3

for i in range(0,5):
    result = ""

    if (i<3):           # 1~3열 별찍기
        for j in range(cnt):
            result += star
        # end of for () --------
        cnt = cnt+2
    else:               # 4~5열 별찍기
        for j in range(cnt2):
            result += star
        # end of for () --------
        cnt2 = cnt2-2
    # end of if() --------
    print(result.center(15))
# end of for () --------


'''
	    == 입사문제 == 
	            
	    *********1
	    ********2
	    *******3
	    ******4
	    *****5
	    ****6
	    ***7
	    **8
	    *9
'''

print("=== 입사문제 ===\n")
result = ""
cnt = 9

for i in range(1,10):
    result = ""
    
    for j in range(cnt):
        result += star
    # end of for () --------
    cnt = cnt-1
    print(result,i)
# end of for () --------