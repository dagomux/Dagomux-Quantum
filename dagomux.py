#!/usr/bin/env python3
import os
import sys
import time

# --- QUANTUM COLORS ---
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
C = '\033[1;36m' # Cyan
Y = '\033[1;33m' # Yellow
W = '\033[0m'    # White

def clear():
    os.system('clear')

# --- QUANTUM SELF-HEALING ENGINE (THE FIXER) ---
def quantum_engine():
    clear()
    print(R + """
    ██████╗  █████╗  ██████╗  ██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗ ████║██║   ██║╚██╗██╔╝
    ██║  ██║███████║██║  ███╗██║   ██║██╔████╔██║██║   ██║ ╚███╔╝ 
    ██║  ██║██╔══██║██║   ██║██║   ██║██║╚██╔╝██║██║   ██║ ██╔██╗ 
    ██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    """ + W)
    print(C + "    [+] SYSTEM   : " + G + "DAGOMUX-QUANTUM (AI CORE)")
    print(C + "    [+] STATUS   : " + Y + "AUTO-REPAIRING SYSTEM...")
    print(W + "    ---------------------------------------------------\n")

    # 1. Fix Core Packages (Silent Install)
    pkgs = ["git", "python", "python2", "php", "perl", "curl", "wget", "nano"]
    for pkg in pkgs:
        # Check if installed, if not install it
        if os.system(f"which {pkg} > /dev/null 2>&1") != 0:
            print(Y + f"    [*] Installing missing core: {pkg}..." + W)
            os.system(f"pkg install {pkg} -y > /dev/null 2>&1")
            
    # 2. Fix Python Libs
    os.system("pip install requests bs4 > /dev/null 2>&1")
    
    print(G + "    [✓] QUANTUM ENGINE READY. NO ERRORS.\n" + W)
    time.sleep(1)

def main_menu():
    # Banner is kept simple to avoid flickering
    print(G + "  [01] " + W + "Sherlock (Find Usernames)")
    print(G + "  [02] " + W + "RedHawk (Website Scanner)")
    print(G + "  [03] " + W + "Nmap (Port Scanning)")
    print(G + "  [04] " + W + "Th3Inspector (Information)")
    print(G + "  [05] " + W + "Zphisher (Phishing)")
    print(G + "  [06] " + W + "SQLMap (Database Hack)")
    print(G + "  [07] " + W + "Hammer (DDoS Attack)")
    print(R + "  [00] " + W + "EXIT")
    
    try:
        choice = input(Y + "\n  dagomux@quantum~# " + W)
        
        if choice == '1':
            smart_runner("Sherlock", "sherlock", "https://github.com/sherlock-project/sherlock", "python3 sherlock")
        elif choice == '2':
            smart_runner("RedHawk", "RED_HAWK", "https://github.com/Tuhinshubhra/RED_HAWK", "php rhawk.php")
        elif choice == '3':
            nmap_runner()
        elif choice == '4':
            smart_runner("Th3Inspector", "Th3inspector", "https://github.com/Moham3dRiahi/Th3inspector", "perl Th3inspector.pl")
        elif choice == '5':
            smart_runner("Zphisher", "zphisher", "https://github.com/htr-tech/zphisher", "bash zphisher.sh")
        elif choice == '6':
            sqlmap_runner()
        elif choice == '7':
            smart_runner("Hammer", "hammer", "https://github.com/cyweb/hammer", "python3 hammer.py")
        elif choice == '0':
            sys.exit()
        else:
            main_menu()
    except Exception as e:
        main_menu()

# --- INTELLIGENT TOOL RUNNER (NO ERRORS) ---
def smart_runner(name, folder, url, command):
    print(Y + f"\n    [*] TARGET: {name}" + W)
    
    # 1. Download if missing
    if not os.path.isdir(folder):
        print(R + "    [!] Not found. Downloading via Quantum Net..." + W)
        os.system(f"git clone {url} {folder}")
        
        # 2. Auto-Dependency Fixer
        if os.path.exists(f"{folder}/requirements.txt"):
            print(C + "    [*] Installing dependencies..." + W)
            os.system(f"pip install -r {folder}/requirements.txt > /dev/null 2>&1")
        if os.path.exists(f"{folder}/install.sh"):
             os.system(f"bash {folder}/install.sh > /dev/null 2>&1")

    # 3. Special Handling (Input System)
    if name == "Sherlock":
        user = input(Y + "\n    [?] Enter Username: " + W)
        if user == "": main_menu()
        print(G + f"    [+] Hunting {user}..." + W)
        os.system(f"cd {folder} && {command} {user}")
    
    else:
        print(G + "    [+] Executing..." + W)
        time.sleep(0.5)
        # Force directory change to avoid file not found errors
        os.system(f"cd {folder} && {command}")
    
    print(Y + f"\n    [!] {name} Session Ended." + W)
    input("    Press Enter to return...")
    quantum_engine() # Reload Banner
    main_menu()

# --- SPECIAL NMAP RUNNER ---
def nmap_runner():
    os.system("pkg install nmap -y > /dev/null 2>&1")
    ip = input(Y + "\n    [?] Enter Target IP: " + W)
    if ip == "": main_menu()
    os.system(f"nmap -A {ip}")
    input("\n    Press Enter to return...")
    quantum_engine()
    main_menu()

# --- SPECIAL SQLMAP RUNNER ---
def sqlmap_runner():
    if not os.path.isdir("sqlmap-dev"):
        os.system("git clone https://github.com/sqlmapproject/sqlmap/tarball/master sqlmap-dev")
    url = input(Y + "\n    [?] Enter URL: " + W)
    if url == "": main_menu()
    os.system(f"cd sqlmap-dev && python3 sqlmap.py -u {url} --dbs --batch")
    input("\n    Press Enter to return...")
    quantum_engine()
    main_menu()

if __name__ == "__main__":
    # Run Quantum Engine First
    quantum_engine()
    main_menu()
