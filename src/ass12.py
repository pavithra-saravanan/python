billid=1001
custid=101
billamt=200.0
discounted_billamt=0
print("billid:%d"%billid)
print("custid:%d"%custid)
print("billamt:rs.%f"%billamt)
if(billamt>500):
    discounted_billamt=billamt-billamt*2/100
else:
    discounted_billamt=billamt-billamt*1/100
    print("discounted_billamt:rs.%f" %discounted_billamt)