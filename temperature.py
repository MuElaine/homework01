#TempConvert.py
import os,time
def temconvert():
    n=input("请选择温度格式（'C'摄氏度，'F'华氏度，'K'开尔文）：")
    if n=="C":
        val=input("请输入数值：")
        f=1.8*float(val)+32
        k=float(val)+273.15
        print("F="+str(f)+'\n'+"K="+str(k))
        os.system("pause");
    elif n=="F":
        val=input("请输入数值：")
        c=5*(float(val)-32)/9
        k=float(c)+273.15
        print("C="+str(c)+'\n'+"K"+str(k))
        os.system("pause");
    elif n=="K":
        val=input("请输入数值：")
        c=float(val)-273.15
        f=1.8*(float(val)-273.15)+32
        print("C="+str(c)+'\n'+"F"+str(f))
        os.system("pause");
    return
                  
