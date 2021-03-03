import time
import random
import smtplib
import datetime
access_password=input('''AutoHacker
v. 1.0.0
Type password given in list of risks to gain access: ''')
if access_password=='6an01jdERQisow;[]\slxz_vyhtujtr1ax./m1xc AHAHAH':
    print('Please wait...')
    time.sleep(1)
    print('Access granted')
    print('''Type print(AH_guide)" for help and double-click the squeezed text indicator''')
    AH_guide='''
AutoHacker Guide
PLEASE READ THIS

Before you start, you must fill out this form: https://docs.google.com/forms/d/e/1FAIpQLSemQ3ur3DwjZadAmKFWUdnCO2LlRBZ_rkM4Ux9otS0wnTLqCA/viewform

All you really need is a Python shell (3.9.1) and the file (you can install using pip
if you want). Use the import keyword to import the program into the shell.
If anything happens that shuts you out, use import importlib and then
importlib.reload() to reload the program.

List of Commands:

    hack(victim, domain, email_address, action, pwlist, pwlistpath):
    Function that tells the program to break into the victim's account.
    Inside the parentheses, list a string with the account name of the victim,
    then type the name of the domain (website url) the account is from inside another
    string, and then list the victim's email address inside the third argument,
    then type one of the following words (inside a string): "pi_theft," which will tell the
    program to steal the victim's personal information, or "destroy," which
    will delete all files and apps from the victim's device and replace them
    with virus programs. Lastly, you must include a potential password or an entire list
    of potential passwords for the program to work with. You can either
    create one and put it in the pwlist parameter, or if you find one online,
    you can download it and type the file path into the pwlistpath parameter.

    phish(victim, domain, email_address): Function that will phish for the victim's personal
    information. Type the account name and the domain it is from inside the
    parentheses (both in strings). This function is essentially the same as
    "pi_theft," but it doesn't use account hacking to retrieve information.
    You may have to wait a long time, as this function depends on the
    victim's response.'''
    def hack(victim, domain, email_address, action, pwlist, pwlistpath):
        if victim!=None and domain!=None and email_address!=None and (pwlist!=None or pwlistpath!=None) and (action=='pi_theft' or action=='destroy'):
            you_sure_hack=input('This action cannot be undone. Are you sure? (yes/no): ')
            if you_sure_hack=='yes':                
                print('Please wait...')
                time.sleep(5)
                print('Username: %s' % victim)
                print('Email Address: %s' % email_address)
                number2=random.randint(1, 2)
                if number2==1:
                    number3=random.randint(1, 50)
                    long_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '~', '`', ',', '.', '/', '?', '<', '>', ';', ':', '"', "'", '[', ']', '{', '}', '\\', ' ']
                    print('Password: ', end='')
                    for x in range(0, number3):
                        s=random.choice(long_list)
                        print(s, end='')
                    print('')
                elif number2==2:
                    list1=['qwerty', 'qwerty123', 'password', '1234567890', victim, 'abc123']
                    selection=random.choice(list1)
                    print('Password: %s' % selection)
                if action=='pi_theft':
                    message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to steal your password. If you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, time.asctime())
                    print('Success')
                    age=random.randint(10, 80)
                    print('Age: %s' % age)
                    birthday=datetime.datetime.now()
                    birthday2=(birthday.month-random.randint((-1*(12-birthday.month)), (birthday.month-1)))
                    birthday3=(birthday.day-random.randint((-1*28-birthday.day), (birthday.day-1)))
                    if (birthday2>=1 and birthday2<=28) and (birthday3>=1 and birthday3<=28):
                        print('''Birthday:
Year = %s
Month = %s
Day = %s''' % ((birthday.year-age), birthday2, birthday3))
                    print('Phone number: ', end='')
                    for y in range(1, 11):
                        phone=random.randint(0, 9)
                        print(phone, end='')
                    print('')
                elif action=='destroy':
                    message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to remove all apps and files from your device and replace them with malware. If you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, time.asctime())
                    print('Success')
                server=smtplib.SMTP('smtp.gmail.com', 587)                       
                server.starttls()
                server.login('AutoHacker.Emailer@gmail.com', '6an01jdERQisow;[]\s1xz_vyhtujtr AHAHAH')
                server.sendmail('AutoHacker.Emailer@gmail.com', email_address, message)
                server.quit()
            elif you_sure_hack=='no':
                print('Action stopped')
            else:
                print('Answer not accepted. Type yes or no')
        else:
            print('Syntax error')
    def phish(victim, domain, email_address):
        if victim!=None and domain!=None and email_address!=None:
            you_sure_phish=input('This action cannot be undone. Are you sure? (yes/no): ')
            if you_sure_phish=='yes':
                print('Please wait...')
                server=smtplib.SMTP('smtp.gmail.com', 587)
                message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to phish to get the password of your %s account. If you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, time.asctime())
                server.starttls()
                server.login('AutoHacker.Emailer@gmail.com', '6an01jdERQisow;[]\s1xz_vyhtujtr AHAHAH')
                server.sendmail('AutoHacker.Emailer@gmail.com', email_address, message)
                server.quit()
                time.sleep(random.randint(60, 500000))
                print('Username: %s' % victim)
                print('Email Address: %s' % email_address)
                number2=random.randint(1, 2)
                if number2==1:
                    number3=random.randint(1, 50)
                    long_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '~', '`', ',', '.', '/', '?', '<', '>', ';', ':', '"', "'", '[', ']', '{', '}', '\\', ' ']
                    print('Password: ', end='')
                    for x in range(0, number3):
                        s=random.choice(long_list)
                        print(s, end='')
                elif number2==2:
                    list1=['qwerty', 'qwerty123', 'password', '1234567890', victim, 'abc123']
                    selection=random.choice(list1)
                    print('Password: %s' % selection)
                age=random.randint(10, 80)
                print('Age: %s' % age)
                birthday=datetime.datetime.now()
                birthday2=(birthday.month-random.randint((-1*(12-birthday.month)), (birthday.month-1)))
                birthday3=(birthday.day-random.randint((-1*28-birthday.day), (birthday.day-1)))
                if (birthday2>=1 and birthday2<=28) and (birthday3>=1 and birthday3<=28):
                    print('''Birthday:
Year = %s
Month = %s
Day = %s''' % ((birthday.year-age), birthday2, birthday3))
                print('Phone number: ', end='')
                for y in range(1, 11):
                    phone=random.randint(0, 9)
                    print(phone, end='')
                print('')
            elif you_sure_phish=='no':
                print('Action stopped')
            else:
                print('Answer not accepted. Type yes or no')
        else:
            print('Syntax error')
else:        
    print('Please wait...')
    time.sleep(1)
    print('Access denied')
    access_password=False
