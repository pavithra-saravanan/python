employeeid=1001
basic_sal=15000
allowances=6000
monthlysal=basic_sal+allowances
print("employeeid:%d"%employeeid)
print("basic_sal:%d"%basic_sal)
print("allowances:%d"%allowances)
print("monthlysal%d"%monthlysal)
if(monthlysal<5000):
    incometax=0.0
    netsalary=monthlysal-incometax
    print("netsalary:%d"%netsalary)
elif((monthlysal>=5001) and (monthlysal<=10000)):
    incometax=monthlysal*10/100
    netsalary=monthlysal-incometax
    print("netsalary:%d"%netsalary)
elif((monthlysal>=10001) and (monthlysal<=20000)):             
    incometax=monthlysal*20/100
    netsalary=monthlysal-incometax
    print("netsalary:%d"%netsalary)
else :
    incometax=monthlysal*30/100
    netsalary=monthlysal-incometax
    print("netsalary:%d"%netsalary)
