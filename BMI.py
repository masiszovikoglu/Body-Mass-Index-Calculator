# program to calculate BMI(Body Mass Index)
while 0==0:
 print("enter your height(cm)")# kullanıcıdan boyunu girmesini ister
 a=int(input())
 print("enter your weight(kg)")#kullanıcıdan kilosunu girmesini ister
 b=int(input())
 c=(b/(a*a))*10000#vücut kitle endeksini hesaplar
 print("Body Mass Index=", c)#vücut kitle endeksini ekrana basar
 if 18<=c<=25:
    print("normal")
 elif 25<c<30:
     print("overweight")
 elif c>=30:
    print("obese")
 elif c<=18:
    print("skinny")
 print("new calculation")
 
 





    










