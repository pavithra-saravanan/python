billid=1001
custid=101
billamt=1200.0
discounted_billamt=0.0
discount=0
print("billid:%d"%billid)
print("custid:%d"%custid)
print("billamt:rs.%f"%billamt)
if(billamt>=1000):
    discount=5
elif billamt>=500:
    discount=2
else:
    discount=1
discounted_billamt=billamt-billamt*discount/100
*print("discounted_billamt:rs.%f" %discounted_billamt)