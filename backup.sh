#!/bin/bash
echo "backup starting ...."
mkdir -p backup
cp app.py backup/
echo "Backup done: $(date)" >> backup_log.txt
