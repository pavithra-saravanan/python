billamt=1000
discount=0.0
if(billamt>500):
    discount=billamt*(2/100)
    orgamt=billamt-discount 
    print(orgamt)
else:
    discount=billamt*(1/100)
    orgamt=billamt-discount
    print(orgamt)