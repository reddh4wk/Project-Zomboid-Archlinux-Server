# Project Zomboid Server with Telegram Integration

Looking for a graceful shutdown and a way to check easily logs and the shell running your application server? You're in the right place!
Would you like a voting system to vote with your friends for the mods to install and the settings to change on the server? You're in the right place!
These amd other features are present in this project.

These files I prepared can run on any distribution that uses systemd as service manager. This set up lets you gracefully shut down the server without having to worry about the progresses not being saved. Just send the kill signal to your machine and let the service manager take care of the rest with the help of the script. Additionally, you can also log in on the server and use the --see option to be able to peak at what's happening on the server and interact with the application.

I am currently running the server on a virtualized archlinux running on hyperv on the machine I use to play. So my friends can join even when I'm not playing it.

### How to set server up
First of all take a look at this guide: https://pzwiki.net/wiki/Dedicated_server

Anyway on a base archlinux installation you will need to:

- Create a user called "pzserver" that will be used to run the application
- Copy the files from this repo to your server in the correspondent folders
- Make pzserver is the owner of /opt/pzserver using:

```
chown -R pzserver:pzserver /opt/pzserver
```
- Enable multilib repository
- Install steamcmd from AUR
- Then just launch steamcmd and from the application prompt launch:

```
force_install_dir /opt/pzserver
login anonymous
app_update 380870 validate
quit
```
- Enable the service file /etc/systemd/system/default.target.wants/pzserver.service you copied from this repo using:

```
systemtcl enable pzserver
```
- Make /opt/pzserver/pzserver.sh executable:

```
chmod +x /opt/pzserver/pzserver.sh
```
- Create a symbolic link to /usr/bin for pzserver.sh

```
ln -s /opt/pzserver/pzserver.sh /usr/bin/pzserver
```
- Install Python and pip on the system
- Create a virtual environment in /opt/pzserver/python using:

```
python -m venv /opt/pzserver/python
```
To install additional modules through pip for this virtual env, use:

```
/opt/pzserver/python/bin/pip
```
The first time launch the server manually from the pzserver user using its own .sh because it requires a password to set up:

```
/opt/pzserver/start-server.sh
```
I may have missed some steps since I'm writing based on my memory. Sorry. But all the big steps are here.

### Set up the Telegram Bot

Last but not least for sure comes the telegram bot, that took some time to write. I know professional python devs will complain about it being one big file and without comments. I know.

- Now, first of all create a API token with BotFather on Telegram and put it in the configuration in /opt/pzserver/telegram_bot/pzserver_tg.py, in the TOKEN variable.
- You will need to put the group chat id in SERVER_CHATS. To get your group chat id, add the bot to the group chat and, in that group chat, use the command /id 
- You may also need to disable the privacy setting of your bot from botfather chat using /setprivacy command
- Make sure to install all the dependencies through /opt/pzserver/python/bin/pip. You will see error thrown with the name of the dependencies when you launch it. If not, try launching it like this:

```
pkill pzserver_tg.py && > /opt/pzserver/telegram_bot/pzserver_tg.log && /opt/pzserver/python/bin/python /opt/pzserver/telegram_bot/pzserver_tg.py & tail -f /opt/pzserver/telegram_bot/pzserver_tg.log
```
I think this should be it... :D

# Conversion from sandbox preset to server settings

Oh, I also leave you a Powershell script I made to copy the settings from the Sandbox presets you can create in-game to the (nicer) .lua format the server uses. I am assuming you are playing from windows.
This way it will be easy for you to create whatever setting through the GUI in-game and then export the file on the server.
