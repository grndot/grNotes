#!/bin/bash

# Author: grn

echo "What is your bot-token?"
read TOKEN
echo "Input your admin IDs (separete by comma):"
read ADMINS
echo "Input your database username:"
read DB_USERNAME
echo "Input your database password:"
read DB_PASSWORD
echo "Input your database name:"
read DB_NAME
echo "Input your database host (ip):"
read DB_HOST
echo "Input your database port:"
read DB_PORT


echo "
NAME=grNotes
BOT_TOKEN=$TOKEN
ADMINS=$ADMINS
USE_REDIS=False

DB_USER=$DB_USERNAME
DB_PASS=$DB_PASSWORD
DB_NAME=$DB_NAME
DB_HOST=$DB_HOST
DB_PORT=$DB_PORT

I18N_DOMAIN="mybot"
" > .env

ArchInstaller() {
    sudo pacman -Sy postgresql python
}
DebInstaller() {
    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo apt install software-properties-common -y
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt-get update
    sudo apt-get -y install postgresql python3.10
}

SysName=$(lsb_release -a | grep "ID"| awk '{print $3}')

if [ "$SysName" = "Arch" ] || [ "$SysName" = "ManjaroLinux" ];
then
    ArchInstaller
elif [ "$SysName" = "Debian" ] || [ "$SysName" = "Ubuntu" ];
then
    DebInstaller
else
    echo "Please, install python3 and postgresql manually!"
fi
