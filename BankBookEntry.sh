#!/bin/zsh

pipenv run python BankBookEntry.py
exit
exit 0


# $ crontab -e
# SHELL=/bin/zsh
# PATH=/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
# 00 00 02 * * cd /Users/kawanishishoutarou/Documents/BankBookEntry/;zsh BankBookEntry.sh;exit 