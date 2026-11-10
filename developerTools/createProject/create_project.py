#!/bin/bash
"""
v 1.1.0
update checker and file extension supported 
"""

import os
import subprocess
import sys
import re
import urllib.request

lang=False
support=["js","ts","jsx","tsx","jsx","go","py"]

CURRENT_VERSION="1.1.0"

def updates():
    try:
      url="https://raw.githubusercontent.com/migz-0day/script_vault/refs/heads/master/developerTools/createProject/changelog.md"
      req=urllib.request.Request(
         url,
         headers={"User-Agent":"changelog-check"}
      )
      with urllib.request.urlopen(req,timeout=3) as response:
         first_line=response.readline().decode().strip()
         match=re.search(r"\[v\s*([\d\.]+)\]",first_line)

         if match:
            latest_v=match.group(1)
            if latest_v != CURRENT_VERSION:
               print(f"[*] Update available: v{latest_v}.You are using v{CURRENT_VERSION}")
               print("run 'git pull' to get the update")
    except Exception:
       pass

def run_cmd(command):
   subprocess.run(command,shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== make project === ")
FOLDER_NAME=input("enter the project folder name : ")
FILE_NAME=input("enter file name without extension : ")
FILE_EXT=input("enter file extension (js,ts,py,go,rs,) : ")

if FILE_EXT in support:
    if not FOLDER_NAME or not FILE_NAME or not FILE_EXT:
        print(f"[!]error all field required")
        sys.exit(1)

    os.makedirs(FOLDER_NAME)
    os.chdir(FOLDER_NAME)

    with open(".env","w") as f:
        f.write("# enviroment variable\n")

    with open(".gitignore","w") as f:
        f.write(".env\nnode_modules/\n__pycache__/\n*.exe\n")

    FULL_FILE=f"{FILE_NAME}.{FILE_EXT}"
    with open(FULL_FILE,"w") as f:
        if FILE_EXT=="py":
            lang=True
            f.write("# main entry point\nprint('hello script_vault')\n")
        elif FILE_EXT in ["js","ts"]:
            f.write("// main entry point\nconsole.log('hello script_vault');\n")

    print(f"[*]created{FULL_FILE}")

    if FILE_EXT in ["js","ts"]:
        lang=True
        print("javascript/typescript found.initializing node project...")
        subprocess.run("npm init -y", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if FILE_EXT in ["ts","tsx"]:
        lang=True
        print("[*]installing typescript depende....")
        subprocess.run("npm install --save-dev typescript @types/node", shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run("npx tsc --init",shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if FILE_EXT in ["jsx","tsx"]:
        lang=True
        print("[*]react......")
        run_cmd("npm install react react-dom")
    if FILE_EXT=="tsx":
        run_cmd("npm install --save-dev @types/react @types/react-dom")

    with open(FULL_FILE,"w") as f:
        if FILE_EXT in ["jsx","tsx"]:
            lang=True
            f.write("import React from 'react'\nexport default function App(){\n return <h1>hello script_vault</h1>;\n}\nexport default App\n") 
        else:
            f.write("// main entry\n console.log('hello script_vault');\n") 

    with open(FULL_FILE,"w") as f:    
        if FILE_EXT=="go":
            lang=True
            print("go detected.Go modules ....")
            run_cmd(f"go mod init {FOLDER_NAME}")
            f.write("package main\n\nimport \"fmt\"\n\nfunc main() {\n\tfmt.Println(\"hello script_vault\")\n}\n")    

    choice=input("Do you want to initialize this project y/n :").lower().strip()
    if choice == "y":
        run_cmd("git init")

    if lang==True:
     print("="*6,"S","="*5,"C","="*5,"R","="*5,"I","="*5,"P","="*5,"T","="*6)
     print(f"[*] project {FOLDER_NAME} created successfully")
     print( f"[*] main file {FILE_NAME}")
     print("="*9,"V","="*9,"A","="*9,"L","="*9,"T","="*9)

else:
 if not lang:
   scriptV_issue_url="https://github.com/migz-0day/script_vault/issues/new"
   issue_url=f"{scriptV_issue_url}?title=New+Project+Type+Request:+{FILE_EXT}+in+create_project.py&body=Hi+i+tried+creating+a+project+with+extension+{FILE_EXT}+but+it+is+not+supported+yet."

   print(f"\n[!] sorry extension '{FILE_EXT}' is not supported yet.")
   print(f" Please open an issue to request it here:\n{issue_url}\n")
   
   #force_choice=input(f"If you still want to continue use --force")

if __name__=="__main__":
 updates()
 main()


