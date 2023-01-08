#!/bin/zsh

pipenv run python BankBookEntryPushDB.py
exit
exit 0


# $ crontab -e
# SHELL=/bin/zsh
# PATH=/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
# 00 00 21 * * cd /Users/kawanishishoutarou/Documents/BankBookEntry/;zsh BankBookEntryPushDB.sh;exit 