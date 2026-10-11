## script_forge
**A collection of useful scripts,tools and automation utilities.** 
*The scripts are written in bash and python and currently they a total to 3. python(2),bash(1)*
## Languages
* Bash
* python
* Go
## contributing
contributions are welcomed:
You can contribute by:
*  submitting a new script.
*  Fixing bugs.
*  Adding documentation or usage examples.
*  Writting tests
* Suggesting new tools or categories.
## Before submitting a contribution:
 1.check whether a similar script exists (if it uses a different language(go,powershell)it's acceptable)  
 2.place your script in appropriate category if any.  
 3.Test your script and remove secrets or personal information.     
 
## security
scripts in this repo are for educational and practical purposes.They may affect files,systems,networks,or other resources depending on funtionality.
 * reveiw code before executing it.
 * use security tools on systems you own
contributors should explain any potentially destructive actions.  

## script Documentation
each script should include enough information for others to understand and use it.
 **should state:**
 * purpose
 * requirements and dependacies
 * supported operating system
 * usage and examples
 * configuration 
 * safety considerations
  ## license 
This project is distributed under the license included in the repo.See ![LICENSE](https://github.com/migz-0day/script_vault/blob/master/LICENSE) for the applicable terms.

## project_make
a bash script to automatically generate structured project directories with .env ,.gitignore ,git initialization 
.Now it has python script with same funtions and features as the bash Script .
## features 
-Name for folder name, main file name and file extension  
-creates .env and adds it to .gitignore.
-Initializes git
-generates package.json and installs TypeScript types.This is only if the extension is js or ts


-Linux (or Git bash / WSL on Windows)
-git
-node and npm (for js and ts)

## installation and usage
1.Clone the repo
```bash
git clone [https://github.com/migz-0day/project-make.git](https://github.com/migz-0day/project-make.git)
cd project-make
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
on teminal
```bash
notepad $PROFILE
```
```bash
function (universal name on how to call it){ python "c:\path\of\file\creat_project.py" @args }
```






