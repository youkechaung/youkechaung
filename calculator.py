#!/usr/bin/env python3
import sys
def f():
    for i in sys.argv[1:]:
        uid,salary = i.split(':')
        try:
            salary = int(salary)
        #n = i[:3]
        #s = int(i[4:)
        except:        
            print("Parameter Error")
        t = '{}:{:.2f}'.format(uid, calculator(salary))
        print(t)

def calculator(salary):
    cs=int(salary)*(1-0.08-0.02-0.005-0.06)-3500
    if cs<0:
        tax=0
    elif 0<cs<=1500:
        tax=cs*0.03
    elif 1500<cs<=4500:
        tax=cs*0.1-105
    elif 4500<cs<=9000:
        tax=cs*0.2-555
    elif 9000<cs<=35000:
        tax=cs*0.25-1005
    elif 35000<cs<=55000:
        tax=cs*0.3-2755
    elif 55000<cs<=80000:
        tax=cs*0.35-5505
    else:
        tax=cs*0.45-13505
    return int(salary)*0.835-tax
if __name__=='__main__':
    f()
