def baggagecheck(baggageAMOUNT):
    if (baggageAMOUNT>=0  and baggageAMOUNT<=40):
        print(True)
    else:
        print(False)
def immigrationcheck(EXPIRYYEAR):
    if (EXPIRYYEAR>=2001 and  EXPIRYYEAR<=2025):
        print(True)
    else:
        print(True)
def securitycheck(NOCSTATUS):
    
    if (NOCSTATUS):
    
        print(True)
    
    else:
        print(False)
        
def traveler(traveler_id,traveler_name):
    baggagecheck(baggageAMOUNT=35)
    immigrationcheck(EXPIRYYEAR=2019)
    securitycheck(NOCSTATUS=True)
    if(bool(baggagecheck) is True and bool(immigrationcheck) is True and bool(securitycheck) is True):
        print("traveler_id=", traveler_id)
        print("traveler_name=", traveler_name)
        print("allow to travel to fly")
    else:
        print("traveler_id=", traveler_id)
        print("traveler_name=", traveler_name)
        print("detained to travel")
        
traveler(traveler_id=1001, traveler_name="jim")  
