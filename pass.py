import datetime
import pyttsx3
import time




#------------------------------ password checker --------------------------

#------------------------------- wish fuction ------------------------------
def wishme():
    hour = datetime.datetime.now().hour

    if hour <12:
        print("good morning sir & mam")
        print("welcome to password checker")
        speak("good morning sir & mam")
        speak("welcome to password checker")
    elif hour <18:
        print("good afternoon sir & mam")
        print("welcome to password checker")
        speak("good afternoon sir & mam")
        speak("welcome to password checker")
    else:
        print("good evining sir & mam")
        print("welcome to password checker")
        speak("good eivining sir & mam")
        speak("welcome to password checker")

#----------------------------speak fuction --------------------------------------
def speak(audio):
    """fuction convert text to specch"""
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150) # speak speed
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    time.sleep(1)#small pause for avoide overlap



#----------------------------------- starting validation  ----------------------------
wishme()

password = input("enter your password: ") # take input from a user 

symbols = "!@#$%^&*()_+~:"# using symbole in a password
common_password = ("password","12345678","admin","welcome")

has_upper = has_lower = has_digit = has_symbol = False

#------------------------------- second validation ----------------------------
if " " in password:
    print("password should not  containe space")
    speak("password should not containe speace")

elif password.lower() in common_password:
    print("password is to common")
    speak("password is to common")

else:
    for cha in password:
        if cha.isupper():
            has_upper = True
    for cha in password:
        if cha.islower():
            has_lower = True
    for cha in password:
        if cha.isdigit():
            has_digit = True
    for cha in password:
        if cha in symbols:
            has_symbol = True

#----------------------------------- final validation --------------------

    if len(password)<8:# the lenth of password minnimum 8 charcters
         print("password was is to shortes at least 8 character are requried")
         speak("password was is to shortes at least 8 character are requried")
    elif not has_upper:
        print("password requried at least one upper case in the password")
        speak("password requried at least one upper case in the password")
    elif not has_digit:
        print("password requried at least one digit in the password")
        speak("password requried at least one digit in the password")
    elif not has_lower:
        print("password at least requried one lower case in the password")
        speak("password at least requried one lower case in the password")
    elif not has_symbol:
        print("password requried at least one symbole in the password")
        speak("password requried at least one symbole in the password")
    else:
        print("password was strong")
        speak("password was strong")


    

