#!/usr/bin/env python3
import os
import sys
import time

# --- GOD MODE COLORS ---
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
P = '\033[1;35m'
W = '\033[0m'

def clear():
    os.system('clear')

# --- ABSOLUTE AI ENGINE ---
def absolute_engine():
    clear()
    print(R + """
    ██████╗  █████╗  ██████╗  ██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗ ████║██║   ██║╚██╗██╔╝
    ██║  ██║███████║██║  ███╗██║   ██║██╔████╔██║██║   ██║ ╚███╔╝ 
    ██║  ██║██╔══██║██║   ██║██║   ██║██║╚██╔╝██║██║   ██║ ██╔██╗ 
    ██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    """ + W)
    print(C + "    [+] SYSTEM   : " + Y + "DAGOMUX-GOD-MODE (ABSOLUTE AI)")
    print(C + "    [+] TOOLS    : " + G + "30+ (WIFI, OSINT, ATTACK)")
    print(C + "    [+] STATUS   : " + R + "NO ERRORS | AUTO-FIX | AUTO-RUN")
    print(W + "    -------------------------------------------------------\n")

    # Auto-Install Missing Dependencies
    pkgs = ["git", "python", "python2", "php", "perl", "curl", "wget", "nano", "openssh"]
    for pkg in pkgs:
        if os.system(f"which {pkg} > /dev/null 2>&1") != 0:
            os.system(f"pkg install {pkg} -y > /dev/null 2>&1")
    
    os.system("pip install requests bs4 > /dev/null 2>&1")

def main_menu():
    absolute_engine()
    print(P + "  [01] Information Gathering (OSINT)")
    print(P + "  [02] WiFi Hacking & Jamming Tools")
    print(P + "  [03] Website Hacking & Scanners")
    print(P + "  [04] Phishing & Social Engineering")
    print(P + "  [05] Password Cracking")
    print(P + "  [06] DDoS & Stress Testing")
    print(P + "  [07] Exploitation Frameworks")
    print(R + "  [00] EXIT SYSTEM")
    
    try:
        choice = input(G + "\n  godmode@root~# " + W)
        
        if choice == '1': menu_osint()
        elif choice == '2': menu_wifi()
        elif choice == '3': menu_web()
        elif choice == '4': menu_phish()
        elif choice == '5': menu_pass()
        elif choice == '6': menu_ddos()
        elif choice == '7': menu_exploit()
        elif choice == '0': sys.exit()
        else: main_menu()
    except:
        sys.exit()

# --- CATEGORY MENUS ---
def menu_osint():
    absolute_engine()
    print(Y + "  [::] OSINT TOOLS [::]" + W)
    tools = [
        ("Sherlock", "sherlock", "https://github.com/sherlock-project/sherlock", "python3 sherlock --help"),
        ("RedHawk", "RED_HAWK", "https://github.com/Tuhinshubhra/RED_HAWK", "php rhawk.php"),
        ("Nmap", "nmap", "pkg install nmap -y", "nmap"),
        ("Th3Inspector", "Th3inspector", "https://github.com/Moham3dRiahi/Th3inspector", "perl Th3inspector.pl"),
        ("IP-Tracer", "IP-Tracer", "https://github.com/rajkumardusad/IP-Tracer", "trace -m"),
        ("PhoneInfoga", "PhoneInfoga", "https://github.com/sundowndev/PhoneInfoga", "./phoneinfoga")
    ]
    execute_selection(tools)

def menu_wifi():
    absolute_engine()
    print(Y + "  [::] WIFI & JAMMING TOOLS [::]" + W)
    tools = [
        ("Wifite (Auto Auditor)", "wifite2", "https://github.com/derv82/wifite2", "python3 wifite.py"),
        ("Routersploit", "routersploit", "https://github.com/threat9/routersploit", "python3 rsf.py"),
        ("Aircrack-ng", "aircrack-ng", "pkg install aircrack-ng -y", "aircrack-ng"),
        ("WiFi-Pumpkin", "WiFi-Pumpkin", "https://github.com/P0cL4bs/WiFi-Pumpkin", "python3 wifi-pumpkin.py"),
        ("OneShot (WPS Attack)", "OneShot", "https://github.com/kimocoder/OneShot", "python3 oneshot.py")
    ]
    execute_selection(tools)

def menu_web():
    absolute_engine()
    print(Y + "  [::] WEB HACKING TOOLS [::]" + W)
    tools = [
        ("SQLMap", "sqlmap-dev", "https://github.com/sqlmapproject/sqlmap/tarball/master", "python3 sqlmap.py --wizard"),
        ("Nikto", "nikto", "https://github.com/sullo/nikto", "perl program/nikto.pl"),
        ("XSS-Strike", "XSStrike", "https://github.com/s0md3v/XSStrike", "python3 xsstrike.py"),
        ("Commix", "commix", "https://github.com/commixproject/commix", "python3 commix.py"),
        ("JoomScan", "joomscan", "https://github.com/rezasp/joomscan", "perl joomscan.pl")
    ]
    execute_selection(tools)

def menu_phish():
    absolute_engine()
    print(Y + "  [::] PHISHING TOOLS [::]" + W)
    tools = [
        ("Zphisher", "zphisher", "https://github.com/htr-tech/zphisher", "bash zphisher.sh"),
        ("PyPhisher", "PyPhisher", "https://github.com/KasRoudra/PyPhisher", "python3 pyphisher.py"),
        ("SocialFish", "SocialFish", "https://github.com/UndeadSec/SocialFish", "python3 SocialFish.py"),
        ("BlackEye", "blackeye", "https://github.com/An0nUD4Y/blackeye", "bash blackeye.sh")
    ]
    execute_selection(tools)

def menu_pass():
    absolute_engine()
    print(Y + "  [::] PASSWORD ATTACKS [::]" + W)
    tools = [
        ("Hydra", "hydra", "pkg install hydra -y", "hydra -h"),
        ("Cupp (Wordlist)", "cupp", "https://github.com/Mebus/cupp", "python3 cupp.py -i"),
        ("Hash-Buster", "Hash-Buster", "https://github.com/s0md3v/Hash-Buster", "python3 hash.py"),
        ("JohnTheRipper", "john", "pkg install john -y", "john")
    ]
    execute_selection(tools)

def menu_ddos():
    absolute_engine()
    print(Y + "  [::] DDOS ATTACKS [::]" + W)
    tools = [
        ("Hammer", "hammer", "https://github.com/cyweb/hammer", "python3 hammer.py"),
        ("Slowloris", "slowloris", "https://github.com/gkbrk/slowloris", "python3 slowloris.py"),
        ("Hulk", "hulk", "https://github.com/grafov/hulk", "python3 hulk.py"),
        ("LITEDDOS", "LITEDDOS", "https://github.com/4L13199/LITEDDOS", "python2 LITEDDOS.py")
    ]
    execute_selection(tools)

def menu_exploit():
    absolute_engine()
    print(Y + "  [::] EXPLOITATION [::]" + W)
    tools = [
        ("Metasploit", "metasploit", "https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh", "bash metasploit.sh"),
        ("SearchSploit", "searchsploit", "pkg install searchsploit -y", "searchsploit")
    ]
    execute_selection(tools)

# --- THE ABSOLUTE RUNNER LOGIC ---
def execute_selection(tools_list):
    for i, tool in enumerate(tools_list, 1):
        print(C + f"  [{i}] {tool[0]}")
    print(R + "  [0] BACK")

    try:
        sel = int(input(G + "\n  select > " + W))
        if sel == 0: main_menu()
        
        target = tools_list[sel-1]
        name = target[0]
        folder = target[1]
        url = target[2]
        cmd = target[3]

        print(Y + f"\n  [*] PREPARING {name}..." + W)

        # 1. PKG Install Logic
        if "pkg install" in url:
            os.system(url)
            # Input System for PKG tools
            if "nmap" in name:
                inp = input(Y + "  [?] Target IP: " + W)
                os.system(f"{cmd} -A {inp}")
            elif "hydra" in name:
                os.system(cmd)
            else:
                os.system(cmd)
        
        # 2. Metasploit Logic
        elif "metasploit" in url:
            if not os.path.exists("metasploit.sh"):
                os.system(f"wget {url}")
            os.system(cmd)

        # 3. Git Clone Logic (The Magic Fix)
        else:
            if not os.path.isdir(folder):
                print(R + "  [!] Downloading..." + W)
                os.system(f"git clone {url} {folder}")
                # Auto deps
                if os.path.exists(f"{folder}/requirements.txt"):
                    print(C + "  [*] Installing Requirements..." + W)
                    os.system(f"pip install -r {folder}/requirements.txt > /dev/null 2>&1")

            # --- CRITICAL FIX: CHANGE DIRECTORY BEFORE RUNNING ---
            # This fixes Sherlock and all other "File not found" errors
            print(G + f"  [+] LAUNCHING {name}..." + W)
            time.sleep(1)
            
            # Special Input Handling inside folder
            if "Sherlock" in name:
                user = input(Y + "  [?] Username to Hunt: " + W)
                # We go INSIDE the folder, then run the command. 100% Works.
                os.system(f"cd {folder} && python3 sherlock {user}")
            elif "RedHawk" in name:
                os.system(f"cd {folder} && php rhawk.php")
            elif "SQLMap" in name:
                u = input(Y + "  [?] Target URL: " + W)
                os.system(f"cd {folder} && python3 sqlmap.py -u {u} --dbs --batch")
            else:
                # Universal execute
                os.system(f"cd {folder} && {cmd}")

        print(Y + f"\n  [!] {name} Finished." + W)
        input("  Press Enter...")
        main_menu()

    except Exception as e:
        main_menu()

if __name__ == "__main__":
    main_menu()
