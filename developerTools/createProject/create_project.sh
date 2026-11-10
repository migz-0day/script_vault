#!/bin/bash

# Version 1.1.0 
# NEW: supports rust
# supported [ js,ts,go,py,rs ]

set -e
echo "=== make project === "
read -p "enter the projects folder name:" FOLDER_NAME
read -p "enter file name without extension: " FILE_NAME
read -p "enter file extension (js,ts,py,go,rs,cpp,mojo): " FILE_EXT

FILE_EXT="${FILE_EXT#.}"

if [ -d "$FOLDER_NAME" ]; then 
 echo "Error: Directory '$FOLDER_NAME' already exists."
 exit 1
fi

echo "ceating project folder '$FOLDER_NAME'..."
mkdir -p "$FOLDER_NAME"
cd "$FOLDER_NAME"

echo "writing enviroment files..."
touch .env
echo ".env" > .gitignore
echo "node_modules/" >> .gitignore
echo "venv/" >> .gitignore

FULL_FILE="${FILE_NAME}.${FILE_EXT}"
touch "$FULL_FILE"
echo "created $FULL_FILE"

if [ "$FILE_EXT" = "js" ] || ["$FILE_EXT" = "ts"]; then 
   echo " javaScript/typescrpt found .Initializing Node proj....."
   npm init -y > /dev/null
  
  if [ "$FILE_EXT" =  "ts" ]; then
   echo "adding dependancies...."
   npm install --save-dev typeScript @types/node > /dev/null
   npx tsc --init > /dev/null
  fi
fi

if [ "$FILE_EXT" =  "go" ]; then
   echo "go detected.go modules"
   go mod init > /dev/null
   echo -e "package main/n/nimport "fmt"/n/nfunc main() {/nfmt.Println("hello script_vault")/n}" >> "$FULL_FILE"
     
fi

if [ "$FILE_EXT" = "rs" ]; then
  echo "rust initializing... creating binary (application) '$FOLDER_NAME'"
  cargo new "$FOLDER_NAME"
  echo -e "fn main(){ println!("hello script_vault")}" >> "$FULL_FILE"
fi

read -p "do you want to initialize this as a git repo (y/n):" REPO_INIT
if [ "$REPO_INIT" = "y" ]; then
 git init > /dev/null
fi

echo "====================S====C====R====I====P====T======================"
echo             "Project '$FOLDER_NAME' created successfully "
echo              "Main file: $FULL_FILE"
echo "======================V====A====U=====L====T========================"

