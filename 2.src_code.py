class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=100,sname='',saddress='',scindate='',scoutdate='',srno=1000):

        print(" " * 5 + "-"*50+" Welcome To CareAll "+"-"*50+" "*5)

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
        self.sname=sname
        self.saddress=saddress
        self.scindate=scindate
        self.scoutdate=scoutdate
        self.srno=srno
        """This Code Has NO Inbuilt Data For Providing Services.  
           
           By Verifying All The Available Options These Will Provide You A Better Understanding Of The Project
           
           Please Try By 
           Registering
           Registering As A Service Provider
           Check Pricing
           Add Reviews And Ratings
           Register A New user Again
           Show Total Description          """


    def inputdata(self):
        self.rno+=1
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter date for Appointment(DD/MM/YYYY):")
        
        while True:
            self.coutdate=input("\nEnter your 10 digit mobile number:")
            if (self.coutdate[0]=='6' or self.coutdate[0]=='7' or self.coutdate[0]=='8' or self.coutdate[0]=='9') and len(self.coutdate)==10:
                break
            else:
                print("Enter a Valid Mobile Number:")

        print("Your Appointment id:",self.rno,"\n")
        
        l=[self.name,self.address,self.cindate,self.coutdate]
        inputdatalist.append(l)

        if inputsdatalist:
            print("The Users Based Upon Reviews And Ratings : " )
            if reviewRating:
                print(reviewRating)
            else:
                print("No Reviews And Ratings Provided Yet")
            print("You Can Get Service From :\n")
            for i in inputsdatalist:
                print(i,"\n")
        else:
            print("-"*10,"Sorry To Hear You That We Are Unable To Allocate A Service Provider","-"*10,"\n ","-"*10,"We don't have Service Providers For You As Per Your Preference","-"*10,"\n   ","-"*10,"We Will Allocate for You In No Time.....Check The Status","-"*11,"\n      ","-"*10,"Thanks A Lot For Your Love And Being With Us","-"*16,"\n\n")
            for r in range(1,6):
                for c in range(7):
                    if (r==1 and c%3!=0 ) or (r==2 and c%3==0) or (r-c==2) or (r+c==8):
                        print(" ❤ ",end = "  ")
                    else:
                        print("  ",end="  ")
                print()
                print()    
     
    def roomrent(self):

        print ("We have the following services for you Based on Ratings:-")

        print ("1.  type A---->rs 600 Per Hour\-")

        print ("2.  type B---->rs 500 Per Hour\-")

        print ("3.  type C---->rs 400 Per Hour\-")

        print ("4.  type D---->rs 300 Per Hour\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Hours Did You Need Service:"))

        if(x==1):

            print ("you have opted Service type A")

            self.s=600*n

        elif (x==2):

            print ("you have opted Service type B")

            self.s=500*n

        elif (x==3):

            print ("you have opted Service type C")

            self.s=400*n

        elif (x==4):
            print ("you have opted Service type D")

            self.s=300*n

        else:

            print ("please choose a Service")

        print ("your Service Charge is =",self.s,"\n")

    def inputsdata(self):
        
        self.sname=input("\nEnter your name:")
        self.saddress=input("\nEnter your address:")
        self.scindate=input("\nEnter Your Email Id: ")
        while True:
            self.scoutdate=input("\nEnter your 10 digit mobile number:")
            if (self.scoutdate[0]=='6' or self.scoutdate[0]=='7' or self.scoutdate[0]=='8' or self.scoutdate[0]=='9') and len(self.scoutdate)==10:
                break
            else:
                print("Enter a Valid Mobile Number:")

        print("Your id:",self.srno,"\n")
        sl=[self.sname,self.saddress,self.scindate,self.scoutdate]
        inputsdatalist.append(sl)
        #for k in inputsdatalist:
        #   print(k,"\n") 

        print("The Adult You Can Serve :\n")
        for j in inputdatalist:
            print(j,"\n")
     
    
    def status(self):
        
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Registered Phone Number:",self.coutdate)
        print ("Id:",self.rno)
        print("Available Service Providers")
        if inputsdatalist:
            print("You Can Get Service From:")
            for i in inputsdatalist:
                print(i,"\n")
        if inputsdatalist:
            print("The Users Based Upon Reviews And Ratings : " )
            if reviewRating:
                print(reviewRating)
            else:
                print("No Reviews And Ratings Provided Yet")
            print("You Can Get Service From :\n")
            for i in inputsdatalist:
                print(i,"\n")

    def sstatus(self):

        print ("Customer name:",self.sname)
        print ("Customer address:",self.saddress)
        print ("Check in date:",self.scindate)
        print ("Check out date",self.scoutdate)
        print ("Room no.",self.srno)
        print("The Adult You Can Serve :")
        for j in inputdatalist:
            print(j,"\n")
    
    def review(self):
        name=input("Enter The Name Of Service Provider Whom You Wish To Provider Review And Rating : ")
        ide=int(input("Enter Id:"))
        print("1. ❤ ")
        print("2. ❤ ❤")
        print("3. ❤ ❤ ❤")
        print("4. ❤ ❤ ❤ ❤")
        print("5. ❤ ❤ ❤ ❤ ❤")
        select=int(input("Enter Your Rating: "))
        review=input("Enter Review: ")
        if select==1:
            star ="❤" 
        elif select == 2:
            star ="❤ ❤"
        elif select == 3:
            star ="❤ ❤ ❤"
        elif select == 4:
            star ="❤ ❤ ❤ ❤"
        elif select == 5:
            star ="❤ ❤ ❤ ❤ ❤"
    
        p=["Name:",name,"Id:",ide,"Rating:",star,"Review:",review]
        reviewRating.append(p)
        print(reviewRating)
   
    def display(self):
        print(" " * 5 + "-"*50+" Total Description "+"-"*50+" "*5)
        print ("\nCustomer details:")
        print ("\nCustomer name:",self.name)
        print ("\nCustomer address:",self.address)
        print ("\nCheck In Date:",self.cindate)
        print ("\nRegisered Phone Number:",self.coutdate)
        print ("\nRegistration Id:",self.rno)
        print("\nPerson Who Serves You")
        print ("\nName Of A :",self.sname)
        print ("\n address:",self.saddress)
        print ("\nEmail Id:",self.scindate)
        print ("\nPhone Number",self.scoutdate)
        print ("\nId:",self.srno)
        N = 10
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N)) 
        print("\nThe generated Tracking Id : " + str(res)) 
    

def main():


    a=hotelfarecal()
    
    
    while (1):
        print("1.Register To Get Service ")
        
        print("2.Calculate Service Charges")

        print("3.Register As Servce Provider")

        print("4.Check Status")

        print("5.Check Available User Who Need Service")

        print("6.Show Total Description")

        print("7.Review & Rating")

        print("8.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()
        
        if (b==3):

            a.inputsdata()


        if (b==4):

            a.status()

        if (b==5):

            a.sstatus()

        if (b==6):

            a.display()

        if (b==7):
            a.review()

        if (b==8):

            quit()

import random
import string
inputdatalist=[]
inputsdatalist=[]
reviewRating=[]
main()