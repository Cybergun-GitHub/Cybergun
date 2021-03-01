# AutoHacker
Before you start, you must fill out this form: https://docs.google.com/forms/d/e/1FAIpQLSemQ3ur3DwjZadAmKFWUdnCO2LlRBZ_rkM4Ux9otS0wnTLqCA/viewform

All you really need is a Python shell (3.9.1) and the file. Use the import keyword to import the program into the shell.
If anything happens that shuts you out, use import importlib and then
importlib.reload() to reload the program.

The reason we ask for your name, email address, and password is because:
When you log on to the program for the first time, you will be able to
suggest improvements by emailing us with your comments. If you wish to
remain anonymous, you can just create another account for this program.
The information is not saved anywhere in the program.

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
