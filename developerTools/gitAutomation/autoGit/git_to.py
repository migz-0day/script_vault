"""
v1.1.0
adds a gitignore file if doesnt exixts and adds any forgotten sensitive file or folder in gitignore
"""

import subprocess
import sys 
import os

def run_cmd(command):
    result=subprocess.run(command, text=True, shell=True)
    if result.returncode != 0:
        print(f"\n command failed: {' '.join(command)}")
        sys.exit(1)

def is_repo():
    res=subprocess.run("git rev-parse --is-inside-work-tree",shell=True,capture_output=True,text=True)
    return res.returncode == 0 

def gitignore_check_add():
    gitignore_path=".gitignore"
    ignored_items = [
        "node_modules/",
        "__pycache__/",
        "*.env",
        "*.env",
        "venv/"
        "env/"
        ".DS_Store",
        "*.log"
    ]
    existing_items = ""

    if os.path.exists(gitignore_path):
        with open(gitignore_path,"r",encoding="utf-8",errors="ignore") as f:
            existing_items=f.read()

    new_items= []
    for item in ignored_items:
        if item not in existing_items:
            new_items.append(item)

    if new_items:
        print(f"\n [+] Adding sensitive folders/files to gitignore.\nThe following are being added {new_items}")
        with open(gitignore_path,"a",encoding="utf-8") as f:
            if existing_items and not existing_items.endswith("\n"):
                f.write("\n")

            f.write("# Added \n")
            for item in new_items:
                f.write(f"{item}\n")


def main():
    print("=*"*25)
    print("[**] checking git status")
    print("running (git status --short)")
    run_cmd(["git", "status", "--short"])
    
    status=subprocess.run(["git", "status", "--porcelain"],capture_output=True,text=True,shell=True)
    if not status.stdout.strip():
        print("\n[*]working tree clean.Nothing to commit")
        input("\n[*]press enter to exit...")
        sys.exit(0)

    commit_msg=input("\n[*] Enter commit message: ").strip()
    if not commit_msg:
        print("[!]commit message can't be empty.Aborting ")
        input("\n[*]press enter to exit...")
        sys.exit(1)

    gitignore_check_add()
    branch_cmd = subprocess.run(["git","rev-parse","--abbrev-ref","HEAD"],capture_output=True,text=True,shell=True)
    branch=branch_cmd.stdout.strip()

    print("\n [1/4] (git add .) stagging changes...")
    run_cmd(["git","add","."])

    print(f"[2/4](git commit -m '{commit_msg}') committing {commit_msg}...")
    run_cmd(["git","commit","-m",f'{commit_msg}'])

    print(f"[3/4](git pull --rebase origin {branch})pulling latest from origin {branch}...")
    run_cmd(["git","pull","--rebase","origin",branch])

    print(f"[4/4](git push origin {branch}) pushing to origin {branch}...")
    run_cmd(["git","push","origin",branch])

    print("*"*8)
    print("\n[*]success all changes are synced to github.")
    input("\n[*]press Enter to exit...")

if __name__=="__main__":
    main()

