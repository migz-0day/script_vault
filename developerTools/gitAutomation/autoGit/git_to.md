## git_to.py
latest version v1.1.0 check [changelog](changelog.md) to see whats new
### features
* automatically commits your new changes this is only when you run the command
   * the following commads run
```bash 
      git status --short 
      git status --porcelain
      git rev-parse --abbrev-ref HEAD
      git add .
      git commit -m 
      git pull --rebase origin branch
      git push origin branch      
```
* branch is a variable that holds the brunch you currently are in which is obtained via 
git rev-parse --ref HEAD.

## installation
clone the repo
```bash
 git clone https://github.com/migz-0day/script_vault.git
 cd script_vault/developerTools/gitAutomation/autoGit
```

for this file only
```bash
curl -O https://raw.githubusercontent.com/migz-0day/script_vault/master/developerTools/gitAutomation/autoGit/git_to.py

cd git_to.py
```