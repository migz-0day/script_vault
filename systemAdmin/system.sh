#!/bin/bash

REPORT="sys_report.txt"
REPORT_DATE=$(date '+%Y-%m-%d_%H-%-M%-%S')

echo "making system report... "
if ! touch "$REPORT";then
 echo "ERROR: cannot make file"
 exit 1
fi

echo "============================================================" > "$REPORT"
echo "                      system >>                     ">> "$REPORT"
echo "============================================================" >>"$REPORT"

echo " " >>"$REPORT"
echo "Date: $REPORT_DATE" >>"$REPORT"
echo "user: $(whoami)" >> "$REPORT"

echo "Hostname: $(hostname)">> "$REPORT"
echo "Linux information: " >> "$REPORT"

uname -a >>"$REPORT"

echo " " >>"$REPORT"
echo "========================================== CPU info ==========================" >>"$REPORT"
free -h >>"$REPORT"

echo " " >>"$REPORT"
echo "======================================== DISK USAGE ==========================" >>"$REPORT"
df -h >>"$REPORT"

echo "" >>"$REPORT"
echo "===================================== FILE ====================================">>"$REPORT"
file_count=$(find . -maxdepth 1 -type f | wc -l)
echo "total files : $file_count">> "$REPORT"
echo " ">>"$REPORT"
echo "File paths:" >>"$REPORT"

if ! find . -type f >> "$REPORT" 2>> "$REPORT"; then
	echo "[!] watning some files have not been listed" >>"$REPORT"
fi

if [ -f "$REPORT" ] && [ -r "$REPORT" ];then
        echo "report created successfully $REPORT"
        echo "report size:" 
                du -h "$REPORT"
else
  echo "ERROR report was not created"
        exit 1
fi


