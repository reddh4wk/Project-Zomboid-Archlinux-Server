# Project Zomboid Server on Linux

Looking for a graceful shutdown and a way to check easily logs and the shell running your application server? You're in the right place!

These files I prepared can run on any distribution that uses systemd as service manager. This set up lets you gracefully shut down the server without having to worry about the progresses not being saved. Just send the kill signal to your machine and let the service manager take care of the rest with the help of the script. Additionally, you can also log in on the server and use the --see option to be able to peak at what's happening on the server and interact with the application.

I am currently running the server on a virtualized archlinux running on hyperv on the machine I use to play. So my friends can join even when I'm not playing it.

### How to set things up
First of all take a look at this guide: https://pzwiki.net/wiki/Dedicated_server

Anyway on archlinux based distribution you will need to:

- Create /opt/pzserver
- Create the user that will use the application
- Make that user the owner of /opt/pzserver
- Enable multilib repository
- Install steamcmd from AUR
- Then just launch steamcmd and from that prompt launch:

```
> force_install_dir /opt/pzserver
> login anonymous
> app_update 380870 validate
> quit
```
- Create /etc/systemd/system/default.target.wants/pzserver.service (you can use the one in this repository)
- Enable the service file jsut created:

```
> systemtcl enable pzserver
```

- Create /opt/pzserver/pzserver.sh (in this repository) and make it executable
- Create a symbolic link to /usr/bin so that it's easier to launch for anyone

```
> ln -s /opt/pzserver/pzserver.sh /usr/bin/pzserver
```
The first time launch the server manually using its own sh. It requires a password to set up. This will happen for each user you launch it fro, it is not system-wide.

I may have missed some steps since I'm writing based on my memory. Sorry. But all the big steps are here.

# Conversion from sandbox preset to server settings

Oh, I also leave you a Powershell script I made to copy the settings from the Sandbox presets you can create in-game to the (nicer) .lua format the server uses. I am assuming you are playing from windows.
This way it will be easy for you to create whatever setting through the GUI in-game and then export the file on the server.

# Telegram Bot

I also made a telegram bot to control things like, when the server is up, when a player logs in, and to allow the possibility to restart the application from telegram. You will need to install a python virtual environment in /opt/pzserver/python and make sure to install all the dependencies through /opt/pzserver/python/bin/pip if something's missing. And create a API token with BotFather and put it in the configuration in /opt/pzserver/telegram_bot/pzserver_main.py
