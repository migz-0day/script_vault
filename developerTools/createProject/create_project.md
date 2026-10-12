## project_make
a bash script to automatically generate structured project directories with .env ,.gitignore ,git initialization 
.Now it has python script with same functions and features as the bash Script .
## features 
* Name for folder name, main file name and file extension  
* creates .env and adds it to .gitignore.
* Initializes git
* generates package.json and installs TypeScript types.This is only if the extension is js or ts
* Linux (or Git bash / WSL on Windows)
* git
* node and npm (for js and ts)

## installation and usage
1.Clone the repo
```bash
git clone https://github.com/migz-0day/script_vault.git
cd script_vault/DeveloperTools/create_project
```

2.make it exaecutable
```bash
chmod +x create-project.sh
```
3.Run the script
```bash
./create-project.sh
```
4.to make it accessible globally on your system
```bash
sudo cp create-project.sh /usr/local/bin/create-project
```

## for python script
## 1.Clone the repo
```bash
git clone https://github.com/migz-0day/script_vault.git
cd script_vault
```
## To run
```bash
python scripts/devTools/create_project.py
```
## On teminal
```
notepad $PROFILE
```
```bash
function (universal name on how to call it){ python "c:\path\of\file\creat_project.py" @args }
```



