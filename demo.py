from flask import Flask, render_template
import speech_recognition as sr


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Enter title of presentation:")
    audio = r.record(source , duration=4)
    try:
        titl = r.recognize_google(audio)
        print("You said : {}".format(titl))
    except:
        titl = "You have not specified title"
        print(titl)


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want heading in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want heading"
        head=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter heading of slide :")
        audio = r.record(source , duration=4)
        try:
          head = r.recognize_google(audio)
          print("You said : {}".format(head))
        except:
          head = "You have said nothing"
          print(head)

        
    
    else:
      head=""
      print("You have not specified heading")



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want content in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want content"
        cont=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter content of slide :")
        audio = r.record(source , duration=4)
        try:
          cont = r.recognize_google(audio)
          print("You said : {}".format(cont))
        except:
          cont = "You have said nothing"
          print(cont)

        
    
    else:
      cont=""
      print("You have not specified content")






r=sr.Recognizer()
with sr.Microphone() as source:
   print ("Do You Want Bullets")
   audio = r.record(source , duration=4)
   try:
      answer=r.recognize_google(audio)
      print("You said : {}".format(answer))
   except:
      answer="You have said nothing"
      print(answer)

if (answer=="yes"):
   r=sr.Recognizer()
   with sr.Microphone() as source:
     print ("How many bullets you want")
     audio = r.record(source , duration=4)
     try:
       bull=r.recognize_google(audio)
       print("You said : {}".format(bull))
     except:
       bull="You have said nothing"
       print(bull)

   if (bull=="three" or bull=="free" or bull=="3"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet1="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet1))
         except:
             bullet1="You have said nothing"
             print(bullet1)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet2="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet2))
         except:
            bullet2="You have said nothing"
            print(bullet2)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet3="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet3))
         except:
            bullet3="You have said nothing"
            print(bullet3)
         bullet4=""


   elif (bull=="four"  or bull=="4"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet1=r.recognize_google(audio)
            print("You said : {}".format(bullet1))
         except:
             bullet1="You have said nothing"
             print(bullet1)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet2=r.recognize_google(audio)
            print("You said : {}".format(bullet2))
         except:
            bullet2="You have said nothing"
            print(bullet2)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet3=r.recognize_google(audio)
            print("You said : {}".format(bullet3))
         except:
            bullet3="You have said nothing"
            print(bullet3)
         print ("Enter Content of bullet four")
         audio = r.record(source , duration=4)
         try:
            bullet4=r.recognize_google(audio)
            print("You said : {}".format(bullet4))
         except:
            bullet4="You have said nothing"
            print(bullet4)  
            

else:
   bullet1=""
   bullet2=""
   bullet3=""
   bullet4=""
   print("Not specified Bullets")




# Second slide


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want heading in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want heading"
        head2=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter heading of slide :")
        audio = r.record(source , duration=4)
        try:
          head2 = r.recognize_google(audio)
          print("You said : {}".format(head2))
        except:
          head2 = "You have said nothing"
          print(head2)

        
    
    else:
      head2=""
      print("You have not specified heading")



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want content in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want content"
        cont2=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter content of slide :")
        audio = r.record(source , duration=4)
        try:
          cont2 = r.recognize_google(audio)
          print("You said : {}".format(cont2))
        except:
          cont2 = "You have said nothing"
          print(cont2)

        
    
    else:
      cont2=""
      print("You have not specified content")






r=sr.Recognizer()
with sr.Microphone() as source:
   print ("Do You Want Bullets")
   audio = r.record(source , duration=4)
   try:
      answer=r.recognize_google(audio)
      print("You said : {}".format(answer))
   except:
      answer="You have said nothing"
      print(answer)

if (answer=="yes"):
   r=sr.Recognizer()
   with sr.Microphone() as source:
     print ("How many bullets you want")
     audio = r.record(source , duration=4)
     try:
       bull=r.recognize_google(audio)
       print("You said : {}".format(bull))
     except:
       bull="You have said nothing"
       print(bull)

   if (bull=="three" or bull=="free" or bull=="3"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet21="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet21))
         except:
             bullet21="You have said nothing"
             print(bullet21)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet22="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet22))
         except:
            bullet22="You have said nothing"
            print(bullet22)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet23="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet23))
         except:
            bullet23="You have said nothing"
            print(bullet23)
         bullet24=""


   elif (bull=="four"  or bull=="4"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet21=r.recognize_google(audio)
            print("You said : {}".format(bullet21))
         except:
             bullet21="You have said nothing"
             print(bullet21)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet22=r.recognize_google(audio)
            print("You said : {}".format(bullet22))
         except:
            bullet22="You have said nothing"
            print(bullet22)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet23=r.recognize_google(audio)
            print("You said : {}".format(bullet23))
         except:
            bullet23="You have said nothing"
            print(bullet23)
         print ("Enter Content of bullet four")
         audio = r.record(source , duration=4)
         try:
            bullet24=r.recognize_google(audio)
            print("You said : {}".format(bullet24))
         except:
            bullet24="You have said nothing"
            print(bullet24)  
            

else:
   bullet21=""
   bullet22=""
   bullet23=""
   bullet24=""
   print("Not specified Bullets")




# Third Slide





r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want heading in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want heading"
        head3=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter heading of slide :")
        audio = r.record(source , duration=4)
        try:
          head3 = r.recognize_google(audio)
          print("You said : {}".format(head3))
        except:
          head3 = "You have said nothing"
          print(head3)

        
    
    else:
      head3=""
      print("You have not specified heading")



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want content in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want content"
        cont3=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter content of slide :")
        audio = r.record(source , duration=4)
        try:
          cont3 = r.recognize_google(audio)
          print("You said : {}".format(cont3))
        except:
          cont3 = "You have said nothing"
          print(cont3)

        
    
    else:
      cont3=""
      print("You have not specified content")






r=sr.Recognizer()
with sr.Microphone() as source:
   print ("Do You Want Bullets")
   audio = r.record(source , duration=4)
   try:
      answer=r.recognize_google(audio)
      print("You said : {}".format(answer))
   except:
      answer="You have said nothing"
      print(answer)

if (answer=="yes"):
   r=sr.Recognizer()
   with sr.Microphone() as source:
     print ("How many bullets you want")
     audio = r.record(source , duration=4)
     try:
       bull=r.recognize_google(audio)
       print("You said : {}".format(bull))
     except:
       bull="You have said nothing"
       print(bull)

   if (bull=="three" or bull=="free" or bull=="3"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet31="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet31))
         except:
             bullet31="You have said nothing"
             print(bullet31)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet32="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet22))
         except:
            bullet32="You have said nothing"
            print(bullet32)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet33="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet33))
         except:
            bullet33="You have said nothing"
            print(bullet33)
         bullet34=""


   elif (bull=="four"  or bull=="4"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet31=r.recognize_google(audio)
            print("You said : {}".format(bullet31))
         except:
             bullet31="You have said nothing"
             print(bullet31)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet32=r.recognize_google(audio)
            print("You said : {}".format(bullet32))
         except:
            bullet32="You have said nothing"
            print(bullet32)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet33=r.recognize_google(audio)
            print("You said : {}".format(bullet33))
         except:
            bullet33="You have said nothing"
            print(bullet33)
         print ("Enter Content of bullet four")
         audio = r.record(source , duration=4)
         try:
            bullet34=r.recognize_google(audio)
            print("You said : {}".format(bullet34))
         except:
            bullet34="You have said nothing"
            print(bullet34)  
            

else:
   bullet31=""
   bullet32=""
   bullet33=""
   bullet34=""
   print("Not specified Bullets")




# Fourth Slide





r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want heading in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want heading"
        head4=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter heading of slide :")
        audio = r.record(source , duration=4)
        try:
          head4 = r.recognize_google(audio)
          print("You said : {}".format(head4))
        except:
          head4 = "You have said nothing"
          print(head4)

        
    
    else:
      head4=""
      print("You have not specified heading")



r = sr.Recognizer()
with sr.Microphone() as source:
    print("Do you want content in slide:")
    audio = r.record(source , duration=4)
    try:
        head1 = r.recognize_google(audio)
        print("You said : {}".format(head1))
    except:
        head1 = "You Don't want content"
        cont4=""
        print(head1)

r = sr.Recognizer()
with sr.Microphone() as source:
    if(head1=="yes"):
        print("Enter content of slide :")
        audio = r.record(source , duration=4)
        try:
          cont4 = r.recognize_google(audio)
          print("You said : {}".format(cont4))
        except:
          cont4 = "You have said nothing"
          print(cont4)

        
    
    else:
      cont4=""
      print("You have not specified content")






r=sr.Recognizer()
with sr.Microphone() as source:
   print ("Do You Want Bullets")
   audio = r.record(source , duration=4)
   try:
      answer=r.recognize_google(audio)
      print("You said : {}".format(answer))
   except:
      answer="You have said nothing"
      print(answer)

if (answer=="yes"):
   r=sr.Recognizer()
   with sr.Microphone() as source:
     print ("How many bullets you want")
     audio = r.record(source , duration=4)
     try:
       bull=r.recognize_google(audio)
       print("You said : {}".format(bull))
     except:
       bull="You have said nothing"
       print(bull)

   if (bull=="three" or bull=="free" or bull=="3"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet41="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet41))
         except:
             bullet41="You have said nothing"
             print(bullet41)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet42="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet42))
         except:
            bullet42="You have said nothing"
            print(bullet42)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet43="> "+r.recognize_google(audio)
            print("You said : {}".format(bullet43))
         except:
            bullet43="You have said nothing"
            print(bullet43)
         bullet44=""


   elif (bull=="four"  or bull=="4"):
      r=sr.Recognizer()
      with sr.Microphone() as source:
         print ("Enter Content of bullet one")
         audio = r.record(source , duration=4)
         try:
            bullet41=r.recognize_google(audio)
            print("You said : {}".format(bullet41))
         except:
             bullet41="You have said nothing"
             print(bullet41)
         print ("Enter Content of bullet two")
         audio = r.record(source , duration=4)
         try:
            bullet42=r.recognize_google(audio)
            print("You said : {}".format(bullet42))
         except:
            bullet42="You have said nothing"
            print(bullet42)
         print ("Enter Content of bullet three")
         audio = r.record(source , duration=4)
         try:
            bullet43=r.recognize_google(audio)
            print("You said : {}".format(bullet43))
         except:
            bullet43="You have said nothing"
            print(bullet43)
         print ("Enter Content of bullet four")
         audio = r.record(source , duration=4)
         try:
            bullet44=r.recognize_google(audio)
            print("You said : {}".format(bullet44))
         except:
            bullet44="You have said nothing"
            print(bullet44)  
            

else:
   bullet41=""
   bullet42=""
   bullet43=""
   bullet44=""
   print("Not specified Bullets")




app = Flask(__name__)
 
@app.route("/")
def slide():
    title=titl
    header=head
    content=cont
    bullets1=bullet1
    bullets2=bullet2
    bullets3=bullet3
    bullets4=bullet4
    header2=head2
    content2=cont2
    bullets21=bullet21
    bullets22=bullet22
    bullets23=bullet23
    bullets24=bullet24
    header3=head3
    content3=cont3
    bullets31=bullet31
    bullets32=bullet32
    bullets33=bullet33
    bullets34=bullet34
    header4=head4
    content4=cont4
    bullets41=bullet41
    bullets42=bullet42
    bullets43=bullet43
    bullets44=bullet44
    return render_template('slide.html',header=header, content=content ,bullets1=bullets1,
                           bullets2=bullets2, bullets3=bullets3, bullets4=bullets4,title=title,header2=header2, content2=content2 ,bullets21=bullets21,
                           bullets22=bullets22, bullets23=bullets23, bullets24=bullets24
                           ,header3=header3, content3=content3 ,bullets31=bullets31,
                           bullets32=bullets32, bullets33=bullets33, bullets34=bullets34
                           ,header4=header4, content4=content4 ,bullets41=bullets41,
                           bullets42=bullets42, bullets43=bullets43, bullets44=bullets44)
 
 
if __name__ == "__main__":
    app.run()

   
       
   



 


   
