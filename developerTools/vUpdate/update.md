## node_update.py   
it simply just updates the package.json by adding the node version.its currently placed to default "node":"=>24.22.1".meaning it adds
```json
 "engines": {
    "node":">=24.22.1"
  },
```
at the end of the package.json.   
To change to desired node version you can change line 6 ```TARGET_NODE=">=24.22.1"``` to whatever version you want the TARGET_NODE you want.     
No third party dependencies required.
## installation
clone the repo
```bash
 git clone https://github.com/migz-0day/script_vault.git
 cd script_vault/developerTools/vUpdate
```
To get this specific file use
```bash
curl -O https://raw.githubusercontent.com/migz-0day/script_vault/developerTools/vUpdate/node_update.py
```