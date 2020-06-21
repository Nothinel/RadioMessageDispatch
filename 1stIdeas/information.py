#!/usr/bin/python

class Information:
    #basic information object to be stored, passed and forwarded in the game
    def __init__(self, infotext="", addr="", org="", idnumber=0, msg="", time="", date=""):
        #initialize an Information type object
        self.infotext = infotext
        self.addr = addr
        self.org = org
        self.idnumber = idnumber
        self.msg = msg
        self.time = time
        self.date = date
    def display(self):
        #to be implemented, should display in IARUFormat
        print("nix")
    
    #define check functions to return True or False by comparing input with the objects attributes
    def check_addr(self, addr2check=""):
        #check addr 
        if addr2check == self.addr:
            return True
        else:
            return False
    def check_org(self, org2check=""):
        #check org 
        if org2check == self.org:
            return True
        else:
            return False
    def check_idnumber(self, idnumber2check=0):
        #check idnumber 
        if idnumber2check == self.addr:
            return True
        else:
            return False

        
test_plain = Information()
test_filled = Information(infotext="Der Techniker ist informiert", addr="Endbenutzer", org="DJ6KR", idnumber=1, time="now", date="yesterday")
print(test_filled.idnumber)
print(test_filled.check_addr("Endbenutzer"))
print(test_filled.check_addr("EndUSER"))
