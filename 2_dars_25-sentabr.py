#1) son = int(input("son kiriting"))
# if son % 2 == 0:
#   print("juft son")
# else :
#   print("toq son") 

# 2)harorat = float (input("haroratingizni kiriting:"))
# if harorat < 36.6 or  harorat > 36.6 :
#     print("tana haroratingiz normal emas")
# else :
#     print("tana haroratingiz normal")     

# 3)son1 = int (input ("son1"))
# son2 = int (input ("son2"))
# son3 = int (input ("son3"))
# if son1 > son2  and son1 > son3 :
#     print("max son1")
# elif  son2 > son1  and son2 > son3 :
#     print("max son2")
# else :
#     print("max son3") 


# 4)son1 = int (input ("son1"))
# son2 = int (input ("son2"))
# son3 = int (input ("son3"))
# if son1 < son2  and son1 < son3 :
#     print("min son1")
# elif  son2 < son1  and son2 < son3 :
#     print("min son2")
# else :
#     print("min son3")

# 5)son = int (input ("son kiriting :"))
# if son > 0:
#     print("musbat son")
# else :
#     print("manfiy son") 

# 6)tomon1 = int (input("uchburchakning birinchi tomonini kiriting: "))   
# tomon2 = int (input("uchburchakning ikkinchi tomonini kiriting: "))   
# tomon3 = int (input("uchburchakning uchinchi tomonini kiriting: ")) 
# if tomon1 + tomon2 > tomon3:
#     print("uchburchak yasab bo'ladi")
# elif tomon3 + tomon2 > tomon1:
#     print("uchburchak yasab bo'ladi")        
# elif tomon1 + tomon3 > tomon2:
#     print("uchburchak yasab bo'ladi")      
# else :
#     print("uchburchak yasab bo'lmaydi")    

# 7)a = int (input(" a son kirit"))
# b  = int (input(" b son kirit"))
# c = int (input(" c son kirit"))
# if b<a and b<c:
#     print("b oraliqda")
# else :
#     print("oraliqda emas")  

# 8)num1 = int (input("kiriting son")) 
# num2  = int (input("kiriting son")) 
# if num1 % 2 == 1 and num2 % 2 == 1 :
#     print("to'g'ri")
# else :
#     print("noto'g'ri")   

# 9)a = int (input(" a son kirit"))
# b = int (input(" b son kirit"))
# c = int (input(" c son kirit"))
# if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
#     print("3lasi ham toq")
# elif  b % 2 == 1 and c % 2 == 1:
#     print("2 tasi toq")    
# elif c % 2 == 1:
#     print("1tasi toq")
# else :
#     print("toq son yo'q")   

# 10) musbat_son = int (input(" 2 yoki 3 xonali musbat son kiriting ")) 
# if musbat_son % 2 == 1 :
#     print("toq son")
# else :
#     print("toq son emas")      
 
son = int (input("son kiriting "))
if son % 3 == 0 :
    print("fiz")
elif  son % 5 == 0 :
    print("biz") 
elif son % 3 == 0 and son % 5 == 0 :
    print("fizbiz")  