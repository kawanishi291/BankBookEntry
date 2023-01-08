#!/bin/zsh

pipenv run python BankBookEntryBackupDB.py
exit
exit 0


# $ crontab -e
# SHELL=/bin/zsh
# PATH=/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
# 00 00 05 * * cd /Users/kawanishishoutarou/Documents/BankBookEntry/;zsh BankBookEntryBackupDB.sh;exit 