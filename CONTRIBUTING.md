## contributing to script_vault
This project welcomes scripts,bug fixes,documentation improvements,tests and ideas.
The goal is to build useful and reliable scripts that people can learn from and use.
## Tables of contents
* ![ways to contribute](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#ways-to-contribute)
* ![Before starting](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#before-you-start)
* ![Development workflow](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#development-workflow)
* ![Adding new script](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#adding-a-new-script)
* ![script requirements](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#script-requirements)
* ![Commit message](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#commit-message)
* ![Pull requests](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#pull-requests)
* ![Code of conduct](https://github.com/migz-0day/script_vault/blob/master/CONTRIBUTING.md#code-of-conduct)

## ways to contribute
you can contribute by:
  * Adding a useful script
  * fixing bugs in existing scripts.
  * improving readability and performance.
  * Adding tests.
  * Reporting bugs or suggesting new features or scripts.

## Before you start
1.check whether a similar script already exists(if it uses a different language from what you used its acceptable)  
2.Read the documentation for the script and category you want to work on.  
3.Check existing issues for related bugs or feature requests.  
4.For large changes,open an issue firs to discuss your proposal.  
## Development workflow
1.Fork the repo.
2.clone your fork:
   ```bash
    git clone https://github.com/migz-0day/script_vault.git
    cd script_vault
 ```
3.create a branch
  ```bash
   git switch -c add-your-script
```
4.Add improve script.
5.Test your changes locally.
6.Commit your changes:
```bash
  git add .
  git commit -m "add: your script" 
```
7.push your brunch
 ```bash
  git push -u origin add your script
```
8.Open a pull request against the original script_forge repository.
## Adding a new script
Place you script in appropriate category.  
example
```
scripts/
└── automation/
    └── fileOrganizer/
            ├── file_organizer.py
            |── requirements.txt (extermal python packages)
            |── file_organizer.sh
            |── file_organizer.go
            |── go.mod
            └── README.md

```
Each script should have its own documentation when it needs individual usage instruction when it needs individual usage instructions,dependencies or configurations.
Avoid submitting duplicate scripts unless they provide meaningful alternative.  

## script requirements
Every script should
 * Have clear purpose
 * include appropriate documentation
 * state its dependencies and supported platforms.
 * Include usage instructions and examples.
 * Handle errors.
 * Avoid unnecessary permissions.
 * Avoid exposure of credentials,tokens,passwords and other sensitive information.
 * Explain potentially destructive operations.
 * Follow guidelines
Where appropriate,include tests and a sample output
# commit message 
use short,descriptive commit messages.
Examples
  * Add:look up utility
  * Fix ...py path handling
  * Improve ..script documentation   
    (add,fix,hotfix,refactor,chore,docs)
# pull requests
Before opening pull requests
* Ensure your script is in the correct directory.
* verify document matches actual script.
* Remove temporary files and how you tested it
## code of conduct
All contributors are expected to participate respectfully 













