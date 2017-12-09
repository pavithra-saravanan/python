billid=1001
custid=101
billamt=200.0
discounted_billamt=0.0
print("billid:%d"%billid)
print("custid:%d"%custid)
print("billamt:rs.%f"%billamt)
if((custid>100)and(custid<=1000)) is True:
    if(billamt>=500):
        discounted_billamt=billamt-billamt*10/100
        print("discounted_billamt:rs.%f" %discounted_billamt)
    else:
        print("No discount")
else:
    print("invalid customer id,customer id must between 101 and 1000")