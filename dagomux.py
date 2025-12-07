#!/usr/bin/env python3
import os
import sys
import time
import subprocess

# --- UNIVERSAL COLORS ---
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
W = '\033[0m'

def clear():
    os.system('clear')

# --- UNIVERSAL FILE FINDER (THE AI BRAIN) ---
# This function searches for the file anywhere inside the folder
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

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
    print(C + "    [+] ENGINE   : " + Y + "UNIVERSAL AI (AUTO-PATH FINDER)")
    print(C + "    [+] POWER    : " + G + "INFINITE (NO ERROR MODE)")
    print(W + "    ---------------------------------------------------\n")

def main_menu():
    banner()
    print(G + "  [01] " + W + "Sherlock (Find Usernames)")
    print(G + "  [02] " + W + "RedHawk (Website Scanner)")
    print(G + "  [03] " + W + "Nmap (Port Scanning)")
    print(G + "  [04] " + W + "Th3Inspector (Info)")
    print(G + "  [05] " + W + "Zphisher (Phishing)")
    print(G + "  [06] " + W + "SQLMap (Database Hack)")
    print(G + "  [07] " + W + "Hammer (DDoS)")
    print(R + "  [00] " + W + "EXIT")
    
    try:
        choice = input(Y + "\n  dagomux@universal~# " + W)
        
        if choice == '1':
            # Sherlock needs searching for 'sherlock.py'
            universal_runner("Sherlock", "sherlock", "https://github.com/sherlock-project/sherlock", "sherlock.py", "python3")
        elif choice == '2':
            universal_runner("RedHawk", "RED_HAWK", "https://github.com/Tuhinshubhra/RED_HAWK", "rhawk.php", "php")
        elif choice == '3':
            nmap_runner()
        elif choice == '4':
            universal_runner("Th3Inspector", "Th3inspector", "https://github.com/Moham3dRiahi/Th3inspector", "Th3inspector.pl", "perl")
        elif choice == '5':
            universal_runner("Zphisher", "zphisher", "https://github.com/htr-tech/zphisher", "zphisher.sh", "bash")
        elif choice == '6':
            sqlmap_runner()
        elif choice == '7':
            universal_runner("Hammer", "hammer", "https://github.com/cyweb/hammer", "hammer.py", "python3")
        elif choice == '0':
            sys.exit()
        else:
            main_menu()
    except Exception as e:
        print(R + f"Error: {e}")
        time.sleep(2)
        main_menu()

# --- THE UNIVERSAL RUNNER ---
def universal_runner(name, folder, url, script_name, interpreter):
    banner()
    print(Y + f"[*] TARGET: {name}" + W)
    
    # 1. Download
    if not os.path.isdir(folder):
        print(R + "    [!] Downloading..." + W)
        os.system(f"git clone {url} {folder}")
        
        # 2. Auto-Install Deps (Searches for requirements.txt anywhere)
        req_file = find_file("requirements.txt", folder)
        if req_file:
            print(C + "    [*] Installing dependencies..." + W)
            os.system(f"pip install -r {req_file} > /dev/null 2>&1")

    # 3. AI PATH FINDER (The Magic Fix)
    print(C + "    [*] Searching for executable file..." + W)
    script_path = find_file(script_name, folder)
    
    if script_path:
        print(G + f"    [+] File Found at: {script_path}" + W)
        
        # 4. Special Input Handling
        extra_args = ""
        if name == "Sherlock":
            user = input(Y + "\n    [?] Enter Username: " + W)
            extra_args = f" {user}"
        
        print(G + f"    [+] Launching {name}..." + W)
        time.sleep(1)
        
        # Execute using full path
        os.system(f"{interpreter} {script_path}{extra_args}")
        
    else:
        print(R + f"    [!] CRITICAL ERROR: Could not find {script_name} inside {folder}." + W)
        print(R + "    [!] The tool structure might have changed drastically." + W)
    
    print(Y + f"\n[!] {name} Closed." + W)
    input("Press Enter to return...")
    main_menu()

def nmap_runner():
    banner()
    os.system("pkg install nmap -y > /dev/null 2>&1")
    ip = input(Y + "\n[?] Enter Target IP: " + W)
    if ip: os.system(f"nmap -A {ip}")
    input("\nPress Enter to return...")
    main_menu()

def sqlmap_runner():
    banner()
    if not os.path.isdir("sqlmap-dev"):
        os.system("git clone https://github.com/sqlmapproject/sqlmap/tarball/master sqlmap-dev")
    url = input(Y + "\n[?] Enter URL: " + W)
    
    # Find sqlmap.py dynamically
    script_path = find_file("sqlmap.py", "sqlmap-dev")
    if script_path:
        os.system(f"python3 {script_path} -u {url} --dbs --batch")
    else:
        print(R + "Could not find sqlmap.py")
        
    input("\nPress Enter to return...")
    main_menu()

if __name__ == "__main__":
    # AUTO FIX SYSTEM ON START
    if not os.path.exists(".quantum_ready"):
        print(Y + "[*] UNIVERSAL ENGINE: FIXING SYSTEM..." + W)
        os.system("pkg update -y > /dev/null 2>&1")
        pkgs = "git python python2 php perl curl wget nano"
        os.system(f"pkg install {pkgs} -y > /dev/null 2>&1")
        os.system("touch .quantum_ready")
    main_menu()
