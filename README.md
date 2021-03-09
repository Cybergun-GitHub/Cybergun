# Cybergun

All you really need is a [Python](python.org) shell (3.9.1) and the file. Use the import keyword to import the program into the shell.

>>> import Cybergun as cg
Note: The "as" part is not necessary, but if you want to save yourself some typing you should add it.

If you get locked out, use this code snippet:

>>> import importlib
>>> importlib.reload(cg)

to reload the program.

List of Commands:

hack(victim, domain, email_address, action, loan_amount, loanto=(username, domain, email_address), pwlist, pwlistpath):
Function that tells the program to break into the victim's account.
Inside the parentheses, list a string with the account name of the victim,
then type the name of the domain (website url) the account is from inside another
string (include https://), and then list the victim's email address inside the third argument. In the fourth argument, list a keyword.
One built-in keyword is "loan," where you are able to draw money from the victim's account into another account.
Another built-in you can use is "pi_theft," which will tell the
program to steal the victim's personal information. When using "loan," provide the account you want to transfer the money to (useful mostly when you are hired and your client wants to steal money). Lastly, you must include a list
of potential passwords for the program to work with. You can either
create one inside the program:
>>> listname=['string1', 'string2', 'string3'...]
>>> #This is how you create a list in Python, so you can apply this code snippet anywhere in Python.
and put it in the pwlist parameter.

phish(victim, domain, email_address, phish_type): Function that will phish for the victim's personal
information. Type the account name and the domain it is from inside the
parentheses (both in strings). Also list the email address of the victim, and type either "phish" or "destroy" into the last parameter. "phish" will send a scareware email to the victim, and the victim is supposed to provide their information to "verufy their account." "destroy" will send a malware email which will infect the device the victim is using. You may have to wait a long time, as this function depends on the
victim's response.
    
    
Cybergun Pros and Cons:

Pros:
1. Fast
2. Easy to use
3. Can hack, phish, or upload malware to the victim's device
4. Uses a variety of attacks
5. Completely anonymous

Cons:
1. Cannot hack local accounts or phones
2. Low user interactivity level


Examples:
>>> #Not filled in yet. Fill in later.

Additional notes:

1. If you want to run Cybergun in the command prompt, open it and type "python," then when it opens, type import Cybergun as cg
2. Cannot hack phones or local accounts (was not designed for that).
3. If you have any ideas, feel free to tell us.

Happy Cybergunning!
