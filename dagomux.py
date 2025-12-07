#!/usr/bin/env python3
import os
import sys
import time
import subprocess

# --- COLORS ---
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
C = '\033[1;36m' # Cyan
Y = '\033[1;33m' # Yellow
W = '\033[0m'    # White

def clear():
    os.system('clear')

# --- SYSTEM DOCTOR (Fixes Missing Packages) ---
def system_doctor():
    clear()
    print(R + """
    ██████╗  █████╗  ██████╗  ██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗ ████║██║   ██║╚██╗██╔╝
    ██║  ██║███████║██║  ███╗██║   ██║██╔████╔██║██║   ██║ ╚███╔╝ 
    ██║  ██║██╔══██║██║   ██║██║   ██║██║╚██╔╝██║██║   ██║ ██╔██╗ 
    ██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    """ + W)
    print(C + "    [+] OWNER    : " + Y + "AMIT DAGOMUX")
    print(C + "    [+] ENGINE   : " + G + "PRIME AI (AUTO-PATH FINDER)")
    print(C + "    [+] STATUS   : " + R + "CHECKING SYSTEM HEALTH...")
    print(W + "    ---------------------------------------------------\n")

    # Install basics
    pkgs = ["git", "python", "python2", "php", "perl", "curl", "wget", "nano"]
    for pkg in pkgs:
        if os.system(f"which {pkg} > /dev/null 2>&1") != 0:
            print(Y + f"    [*] Installing missing package: {pkg}..." + W)
            os.system(f"pkg install {pkg} -y > /dev/null 2>&1")
    
    os.system("pip install requests bs4 > /dev/null 2>&1")
    print(G + "    [✓] SYSTEM READY. STARTING ENGINE.\n" + W)
    time.sleep(1)

# --- THE AI FINDER FUNCTION (MAGIC FIX) ---
def find_file(root_folder, filename):
    """Recursively finds a file inside a directory"""
    for root, dirs, files in os.walk(root_folder):
        if filename in files:
            return os.path.join(root, filename)
    return None

def launcher(name, folder, url, target_file, interpreter, arg_type):
    print(Y + f"\n    [*] TARGET SELECTED: {name}" + W)
    
    # 1. DOWNLOAD
    if not os.path.isdir(folder):
        print(R + "    [!] Downloading Tool..." + W)
        os.system(f"git clone {url} {folder}")
    
    # 2. FIND THE FILE (AI SEARCH)
    print(C + "    [*] Scanning directory for executable..." + W)
    script_path = find_file(folder, target_file)
    
    if not script_path:
        print(R + f"    [!] CRITICAL: Could not find {target_file} inside {folder}." + W)
        input("    Press Enter to return...")
        main_menu()
        return

    # 3. GET DIRECTORY OF THE SCRIPT
    script_dir = os.path.dirname(script_path)
    
    # 4. AUTO INSTALL REQUIREMENTS (If found in that dir)
    if os.path.exists(os.path.join(script_dir, "requirements.txt")):
        print(C + "    [*] Installing Python Dependencies..." + W)
        os.system(f"pip install -r {os.path.join(script_dir, 'requirements.txt')} > /dev/null 2>&1")

    # 5. INPUT HANDLING
    user_input = ""
    if arg_type == "username":
        inp = input(Y + "    [?] Enter Username: " + W)
        user_input = f" {inp}"
    elif arg_type == "ip":
        inp = input(Y + "    [?] Enter IP/Domain: " + W)
        user_input = f" -A {inp}" if "nmap" not in name.lower() else f" {inp}"
    elif arg_type == "url":
        inp = input(Y + "    [?] Enter URL: " + W)
        user_input = f" -u {inp} --dbs --batch"

    # 6. EXECUTE (Change Dir -> Run)
    print(G + f"    [+] Launching from: {script_dir}..." + W)
    time.sleep(1)
    
    # This creates a sub-shell, enters the folder, and runs the command
    final_cmd = f"cd {script_dir} && {interpreter} {target_file} {user_input}"
    os.system(final_cmd)
    
    print(Y + f"\n    [!] {name} Finished." + W)
    input("    Press Enter to return...")
    main_menu()

def main_menu():
    print(G + "  [01] " + W + "Sherlock (Find Usernames)")
    print(G + "  [02] " + W + "RedHawk (Website Scanner)")
    print(G + "  [03] " + W + "Th3Inspector (Info Gathering)")
    print(G + "  [04] " + W + "Zphisher (Phishing)")
    print(G + "  [05] " + W + "SQLMap (Database Hack)")
    print(G + "  [06] " + W + "Cupp (Password List)")
    print(G + "  [07] " + W + "Hammer (DDoS)")
    print(R + "  [00] " + W + "EXIT")
    
    try:
        choice = input(Y + "\n  dagomux@prime~# " + W)
        
        if choice == '1':
            # Sherlock might be sherlock.py or just sherlock (__main__.py)
            # We look for 'sherlock.py' OR folder structure handles it
            launcher("Sherlock", "sherlock", "https://github.com/sherlock-project/sherlock", "sherlock", "python3", "username")
        elif choice == '2':
            launcher("RedHawk", "RED_HAWK", "https://github.com/Tuhinshubhra/RED_HAWK", "rhawk.php", "php", "none")
        elif choice == '3':
            launcher("Th3Inspector", "Th3inspector", "https://github.com/Moham3dRiahi/Th3inspector", "Th3inspector.pl", "perl", "none")
        elif choice == '4':
            launcher("Zphisher", "zphisher", "https://github.com/htr-tech/zphisher", "zphisher.sh", "bash", "none")
        elif choice == '5':
            launcher("SQLMap", "sqlmap-dev", "https://github.com/sqlmapproject/sqlmap/tarball/master", "sqlmap.py", "python3", "url")
        elif choice == '6':
            launcher("Cupp", "cupp", "https://github.com/Mebus/cupp", "cupp.py", "python3", "none")
        elif choice == '7':
            launcher("Hammer", "hammer", "https://github.com/cyweb/hammer", "hammer.py", "python3", "none")
        elif choice == '0':
            sys.exit()
        else:
            main_menu()
    except Exception as e:
        main_menu()

# --- SPECIAL HANDLER FOR NMAP (System Pkg) ---
def nmap_runner():
    os.system("pkg install nmap -y > /dev/null 2>&1")
    inp = input(Y + "\n    [?] Enter Target IP: " + W)
    os.system(f"nmap -A {inp}")
    input("\n    Press Enter to return...")
    main_menu()

if __name__ == "__main__":
    system_doctor() # Auto-Fix System First
    main_menu()
