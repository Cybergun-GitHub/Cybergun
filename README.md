# AutoHacker

All you really need is a [Python](python.org) shell (3.9.1) and the file. Use the import keyword to import the program into the shell.

>>> import AutoHacker as ah
Note: The "as" part is not necessary, but if you want to save yourself some typing you should add it.

If you get locked out, use this code snippet:

>>> import importlib
>>> importlib.reload(ah)

to reload the program.

List of Commands:

    hack(victim, domain, email_address, action, loan_amount, loanto=(username, domain, email_address), pwlist, pwlistpath):
    Function that tells the program to break into the victim's account.
    Inside the parentheses, list a string with the account name of the victim,
    then type the name of the domain (website url) the account is from inside another
    string, and then list the victim's email address inside the third argument. In the fourth argument, list a keyword.
    One built-in keyword is "loan," where you are able to draw money from the victim's account into another account.
    Another built-in you can use is "pi_theft," which will tell the
    program to steal the victim's personal information, or "destroy," which
    will delete all files and apps from the victim's device and replace them
    with malware. When using "loan," provide the account you want to transfer the money to (useful mostly when you are hired and your client wants to steal money).     Lastly, you must include a potential password or an entire list
    of potential passwords for the program to work with. You can either
    create one inside the program:
    >>> listname=['string1', 'string2', 'string3'...]
    >>> #This is how you create a list in Python, so you can apply this code snippet anywhere in Python.
    and put it in the pwlist parameter, or you can create/find a file,
    and download it and type the file path into the pwlistpath parameter. Preferred file type is .txt or .lst.
    When typing urls, please omit anything before the website name (e.g. if the url is https://www.amazon.com, type it as amazon.com).

    phish(victim, domain, email_address): Function that will phish for the victim's personal
    information. Type the account name and the domain it is from inside the
    parentheses (both in strings). This function is essentially the same as
    "pi_theft," but it doesn't use account hacking to retrieve information.
    You may have to wait a long time, as this function depends on the
    victim's response. This function uses scam emails.

    Additional notes:
    
    1. Spelling DOES matter for EVERY parameter. You are essentially telling the program what it's got to work with, and it cannot auto-correct if you make a mistake in your spelling.
    2. This program performs hybrid attacks - when you provide the list of passwords, it will use them, then start playing around with the characters. If all else fails, the program will run a pure brute-force attack for some time, and if that doesn't work, it will print "Attempt failed."
    3. If you want to run AutoHacker in the command prompt, open it and type "python," then when it opens, type import AutoHacker as ah.
    4. Not much user control (sorry). However, this program is still very early in development, and we've only scraped together the minimum needed for this program to work.
