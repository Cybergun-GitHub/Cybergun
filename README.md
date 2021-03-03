# AutoHacker
Before you start, you must fill out this form: https://docs.google.com/forms/d/e/1FAIpQLSemQ3ur3DwjZadAmKFWUdnCO2LlRBZ_rkM4Ux9otS0wnTLqCA/viewform

All you really need is a [Python](python.org) shell (3.9.1) and the file. Use the import keyword to import the program into the shell.
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
    victim's response.
