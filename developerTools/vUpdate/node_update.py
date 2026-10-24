#!/bin/bash
import os
import json

SEARCH_DIR="."
TARGET_NODE=">=24.22.1"

def package_json(file_p):
    try:
      with open(file_p,"r",encoding="utf-8") as f:
         data=json.load(f)

      if "engines" not in data:
         data["engines"]={}

      if data['engines'].get('node') ==TARGET_NODE:
            print(f"[skip] Already updated :{file_p}")
            return

      data['engines']['node']=TARGET_NODE

      with open(file_p,'w',encoding='utf-8') as f:
          json.dump(data,f,indent=2)
          f.write('\n')
      print(f"[sucess] updated: {file_p}")

    except Exception as err:
     print(f"[ERROR] could not get {file_p}:{err}")

def scan_apt(root_dir):
   for root,dirs,files in os.walk(root_dir):
      if "node_modules" in dirs:
            dirs.remove('node_modules')

      if "package.json" in files:
          full_p=os.path.join(root,"package.json")
          package_json(full_p)
if __name__=="__main__":
   scan_apt(SEARCH_DIR)
