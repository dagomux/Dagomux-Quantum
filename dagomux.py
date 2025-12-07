#!/usr/bin/env python3
import os
import sys
import time

# --- COLORS ---
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
W = '\033[0m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(R + """
    ██████╗  █████╗  ██████╗  ██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗ ████║██║   ██║╚██╗██╔╝
    ██║  ██║███████║██║  ███╗██║   ██║██╔████╔██║██║   ██║ ╚███╔╝ 
    ██║  ██║██╔══██║██║   ██║██║   ██║██║╚██╔╝██║██║   ██║ ██╔██╗ 
    ██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    """ + W)
    print(C + "    [+] TOOL     : " + Y + "DAGOMUX-QUANTUM")
    print(C + "    [+] STATUS   : " + G + "FILE PATHS FIXED (100%)")
    print(W + "    ---------------------------------------------------\n")

def main_menu():
    banner()
    print(G + "  [01] " + W + "Sherlock (Find Usernames)")
    print(G + "  [02] " + W + "RedHawk (Website Scanner)")
    print(G + "  [03] " + W + "Nmap (Port Scanning)")
    print(G + "  [04] " + W + "Th3Inspector (All Info)")
    print(G + "  [05] " + W + "Zphisher (Phishing)")
    print(G + "  [06] " + W + "SQLMap (Database Hack)")
    print(G + "  [07] " + W + "Hammer (DDoS)")
    print(R + "  [00] " + W + "EXIT")
    
    try:
        choice = input(Y + "\n  dagomux@admin~# " + W)
        
        if choice == '1':
            # FIXED: Added .py to command
            runner("Sherlock", "sherlock", "https://github.com/sherlock-project/sherlock", "python3 sherlock.py")
        elif choice == '2':
            runner("RedHawk", "RED_HAWK", "https://github.com/Tuhinshubhra/RED_HAWK", "php rhawk.php")
        elif choice == '3':
            nmap_runner()
        elif choice == '4':
            runner("Th3Inspector", "Th3inspector", "https://github.com/Moham3dRiahi/Th3inspector", "perl Th3inspector.pl")
        elif choice == '5':
            runner("Zphisher", "zphisher", "https://github.com/htr-tech/zphisher", "bash zphisher.sh")
        elif choice == '6':
            sqlmap_runner()
        elif choice == '7':
            runner("Hammer", "hammer", "https://github.com/cyweb/hammer", "python3 hammer.py")
        elif choice == '0':
            sys.exit()
        else:
            main_menu()
    except Exception as e:
        main_menu()

def runner(name, folder, url, command):
    banner()
    print(Y + f"[*] TARGET: {name}" + W)
    
    # 1. Download
    if not os.path.isdir(folder):
        print(R + "    [!] Downloading..." + W)
        os.system(f"git clone {url} {folder}")
        
        # Auto-Install Requirements
        if os.path.exists(f"{folder}/requirements.txt"):
            print(C + "    [*] Installing dependencies..." + W)
            os.system(f"pip install -r {folder}/requirements.txt > /dev/null 2>&1")

    # 2. Sherlock Special Input
    if name == "Sherlock":
        user = input(Y + "\n    [?] Enter Username: " + W)
        if user == "": main_menu()
        print(G + f"    [+] Hunting for {user}..." + W)
        # CRITICAL FIX HERE:
        os.system(f"cd {folder} && {command} {user}")
    
    else:
        print(G + "    [+] Launching..." + W)
        time.sleep(1)
        os.system(f"cd {folder} && {command}")
    
    print(Y + f"\n[!] {name} Closed." + W)
    input("Press Enter to return...")
    main_menu()

def nmap_runner():
    banner()
    # Install Nmap silently if missing
    os.system("pkg install nmap -y > /dev/null 2>&1")
    ip = input(Y + "\n[?] Enter Target IP: " + W)
    if ip == "": main_menu()
    os.system(f"nmap -A {ip}")
    input("\nPress Enter to return...")
    main_menu()

def sqlmap_runner():
    banner()
    if not os.path.isdir("sqlmap-dev"):
        os.system("git clone https://github.com/sqlmapproject/sqlmap/tarball/master sqlmap-dev")
    url = input(Y + "\n[?] Enter URL: " + W)
    if url == "": main_menu()
    os.system(f"cd sqlmap-dev && python3 sqlmap.py -u {url} --dbs --batch")
    input("\nPress Enter to return...")
    main_menu()

if __name__ == "__main__":
    # AUTO INSTALL DEPENDENCIES ON STARTUP
    if not os.path.exists(".setup_complete"):
        os.system("pkg update -y > /dev/null 2>&1")
        os.system("pkg install git python python2 php perl -y > /dev/null 2>&1")
        os.system("touch .setup_complete")
    main_menu()
