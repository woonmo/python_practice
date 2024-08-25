
menu_select_no = 0
member_list = []
member_cnt = 0

while not menu_select_no == 3 :
    try:
        print("\n============= >> 메뉴 << =============\n"
        ,	"1.회원가입   2.모든회원조회   3.프로그램종료\n"
        ,   "===================================")
        
        print("\n메뉴 입력 : ", end="")
        menu_select_no = int(input())
        
        if menu_select_no == 1 :
            flag=True
            if(member_cnt < 5):
                while True:
                    print("\n아이디를 입력하세요 : ", end="")
                    id = str(input())
                    if(id.isspace()):
                        print("\n공백은 사용할 수 없습니다.")
                        continue
                    for i in range(member_cnt):
                        if(id == member_list[i]):
                            print("\n중복된 아이디 입니다.")
                            flag=False
                            break
                    # end of for() ------------
                    
                    if (flag==False) :
                        flag=True
                        continue
                    member_cnt = member_cnt+1
                    member_list.append(id)
                    print("\n >> 회원가입 완료 <<")
                    break
                # end of while() ----------- 
            else:
                print("정원초과로 회원가입이 불가합니다.")
            # end of if(member_cnt < 5) ------------
        elif menu_select_no == 2:
            if (member_cnt == 0):
                print("\n가입된 회원이 없습니다.")
            else:
                print(member_list)
        
    except:
        print("\n== [경고] 메뉴에 없는 것입니다. ==")
        
# end of while() -------------

    
print("\n>> 프로그램 종료 <<")