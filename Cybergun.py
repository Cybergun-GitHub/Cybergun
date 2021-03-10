import time
import random
import smtplib
import datetime
print('''Cybergun v1.0.0
Link to GitHub repository: https://github.com/Cybergun-GitHub/Cybergun-1.0.0''')
def hack(victim, domain, email_address, action, loan_amount, loantoemail, pwlist):
    if victim!=None and (domain!=None and (domain=='google.com' or domain=='yahoo.com' or domain=='microsoft.com' or domain=='paypal.com' or domain=='facebook.com' or domain=='twitter.com' or domain=='youtube.com' or domain=='instagram.com')) and email_address!=None and pwlist!=None and (action=='loan' or action=='pi_theft' or action==None) and (((action=='loan' and loan_amount!=None and int(loan_amount)>0 and loantoea!=None) or ((action=='pi_theft' or action==None) and (loan_amount==None and loanto==None)))):
        if action=='pi_theft':
            message='''HACKER ALERT. THIS IS NOT FAKE.
Hi, %s. A hacker has tried to break into your %s account to steal your personal information, such as your age and credit card number. If you did not grant this person access to your account, change your passwords first. Then, contact the IC3 immediately at ic3.gov or call 911. Provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
This email was sent from a Python emailing program called Cybergun at %s.''' % (victim, domain, time.asctime())
        elif action=='loan':
            message='''HACKER ALERT. THIS IS NOT FAKE.
Hi, %s. A hacker has tried to break into your %s account to steal money (%s dollars) and transfer it to %s. If you did not grant this person access to your account, change your passwords first. Then, contact the IC3 immediately at ic3.gov or call 911. Provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
This email was sent from a Python emailing program called Cybergun at %s.''' % (victim, domain, loan_amount, loanto, time.asctime())
        elif action==None:
            message='''HACKER ALERT. THIS IS NOT FAKE.
Hi, %s. A hacker has tried to break into your %s account. If you did not grant this person access to your account, change your passwords first. Then, contact the IC3 immediately at ic3.gov or call 911. Provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
This email was sent from a Python emailing program called Cybergun at %s.''' % (victim, domain, time.asctime())
        def qwer():
            if action=='pi_theft':
                age=random.randint(10, 80)
                print('Age: %s' % age)
                birthday=datetime.datetime.now()
                birthday2=(birthday.month-random.randint((-1*(12-birthday.month)), birthday.month))
                birthday3=(birthday.day-random.randint(-1*(28-birthday.day), birthday.day))
                if (birthday2>=1 and birthday2<=28) and (birthday3>=1 and birthday3<=28):
                    print('''Birthday Info:
    Year = %s
    Month = %s
    Day = %s''' % ((birthday.year-age), birthday2, birthday3))
                print('Phone number: ', end='')
                phone_list=['971', '503', '800']
                oooof=random.choice(phone_list)
                print(oooof, end='')
                phone_list2=random.randint(100, 999)
                print(phone_list2, end='')
                phone_list3=random.randint(1000, 9999)
                print(phone_list3, end='')    
                print('')
                credit_number_of=random.randint(15, 16)
                print('Credit number: ', end='')
                oefwibv=random.randint(100000000000000, 9999999999999999)
                print(oefwibv, end='')
                print('')
                gender=['Male', 'Female', 'Not obtained']
                pick=random.choice(gender)
                print('Gender: %s' % pick)
                message='''HACKER ALERT. THIS IS NOT FAKE.
    Hi, %s. A hacker has tried to break into your %s account to steal your personal information, such as your age and credit card number. So far, your attacker has been told that you are %s years old and that your birthday is %s/%s/%s (month/day/year). He/she has also been told that your gender is %s and your credit card number is %s and your phone number is %s%s%s. If you did not grant this person access to your account, change your passwords first. Then, contact the IC3 immediately at ic3.gov or call 911. Provide all the information that is given here. Visit ic3.gov/Home/FAQ for more information.
    This email was sent from a Python emailing program called Cybergun at %s.''' % (victim, domain, age, birthday2, birthday3, (birthday.year-age), pick, oefwibv, oooof, phone_list2, phone_list3, time.asctime())
            elif action=='loan':
                print('%s dollars were successfully delivered to %s' % (loan_amount, loanto))
        print('Please wait...')
        time.sleep(2)
        print('Searching for %s...' % domain, end='')
        print(' found')
        time.sleep(1)
        print('Trying username...', end='')
        time.sleep(0.75)
        efibvw=random.randint(1, 2)
        if efibvw==1:
            print(' success')
        elif efibvw==2:
            print(' failed. Trying email address...', end='')
            time.sleep(0.75)
            print(' success')
        time.sleep(0.75)
        print('Trying passwords...')
        time.sleep(3)
        wefwrbgqfeb=random.randint(1, 4)
        if wefwrbgqfeb!=4:
            print(' success')
            print('Success')
            print('Username: %s' % victim)
            print('Email Address: %s' % email_address)
            print('Password: %s' % random.choice(pwlist))
            qwer()
        elif wefwrbgqfeb==4:
            print(' failed. Switching to status=char_modify...', end='')
            time.sleep(0.5)
            print(' performing character modifications...', end='')
            time.sleep(5)
            erwwrb=random.randint(1, 15)
            if erwwrb!=15:
                print(' success')
                print('Success')
                print('Username: %s' % victim)
                print('Email Address: %s' % email_address)
                cc=random.choice(pwlist)
                ccc=random.choice(cc)
                long_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '~', '`', ',', '.', '/', '?', '<', '>', ';', ':', '"', "'", '[', ']', '{', '}', '\\', ' ']
                choice=random.choice(long_list)
                cccc=cc.split(ccc, 1)
                new_string=cccc[0]+choice+cccc[1]
                for xx in range(1, random.randint(1, len(new_string))):
                    choicc=random.choice(long_list)
                    choicec=random.choice(new_string)
                    ccccc=new_string.split(choicec, 1)
                    new_string=ccccc[0]+choicc+ccccc[1]
                print('Password: %s' % new_string)
                qwer()
            elif erwwrb==15:
                print(' failed. Switching to status=pure_brute_force...', end='')
                time.sleep(0.5)
                print(' generating passwords...', end='')
                time.sleep(10)
                WWWW=random.randint(1, 30)
                if WWWW!=30:
                    print(' success')
                    number2=random.randint(1, 2)
                    if number2==1:
                        number3=random.randint(1, 50)
                        long_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '~', '`', ',', '.', '/', '?', '<', '>', ';', ':', '"', "'", '[', ']', '{', '}', '\\', ' ']
                        print('Password: ', end='')
                        lll=['']
                        for x in range(0, number3):
                            s=random.choice(long_list)
                            lll.append(s)
                        pwd=''.join(lll)
                        print(pwd)
                    elif number2==2:
                        list1=['qwerty', 'qwerty123', 'password', '1234567890', victim, 'abc123']
                        selection=random.choice(list1)
                        print('Password: %s' % selection)
                    qwer()
                elif WWWW==30:
                    print(' failed')
                    print('Attempt failed')
        server=smtplib.SMTP('smtp.gmail.com', 587)                       
        server.starttls()
        server.login('AutoHacker.Emailer@gmail.com', '6an01jdERQisow;[]\s1xz_vyhtujtr AHAHAH')
        server.sendmail('AutoHacker.Emailer@gmail.com', email_address, message)
        server.quit()
    else:
        print('Syntax error')
def phish(victim, domain, email_address, phish_type):
    if victim!=None and domain!=None and email_address!=None and phish_type!=None and (phish_type=='phish' or phish_type=='destroy') and (domain=='google.com' or domain=='yahoo.com' or domain=='microsoft.com' or domain=='paypal.com' or domain=='facebook.com' or domain=='twitter.com' or domain=='youtube.com' or domain=='instagram.com'):
        print('Please wait...')
        time.sleep(2)
        print('Sending scareware/malware email to %s...' % email_address)
        time.sleep(3)
        print('''Awaiting victim's response. Do not close this program...''')
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
    else:
        print('Syntax error')
