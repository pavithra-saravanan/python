employeeid=1001
basic_sal=15000
allowances=6000
monthlysal=basic_sal+allowances
incometax=20/100*monthlysal
print("employeeid:%d"%employeeid)
print("basic_sal:%d"%basic_sal)
print("allowances:%d"%allowances)
print("incometax:%d"%incometax)
if(monthlysal>10000)is True:
    netsalary=monthlysal-incometax
    print("netsalary:%d"%netsalary)