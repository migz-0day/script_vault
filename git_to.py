import subprocess
import sys 

def run_cmd(command):
    result=subprocess.run(command, text=True, shell=True)
    if result.returncode != 0:
        print(f"\n command failed: {' '.join(command)}")
        sys.exit(1)

def main():
    print("=*"*25)
    print("=== checking git status ===")
    print("running (git status --short)")
    run_cmd(["git", "status", "--short"])
    
    status=subprocess.run(["git", "status", "--porcelain"],capture_output=True,text=True,shell=True)
    if not status.stdout.strip():
        print("\nworking tree clean.Nothing to commit")
        input("\npress enter to exit...")
        sys.exit(0)

    commit_msg=input("\n Enter commit message: ").strip()
    if not commit_msg:
        print("commit message can't be empty.Aborting ")
        input("\n press enter to exit...")
        sys.exit(1)

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

    print("\nsuccess all changes are synced to github.")
    input("\npress Enter to exit...")
    print("\n""*"*8)

if __name__=="__main__":
    main()

