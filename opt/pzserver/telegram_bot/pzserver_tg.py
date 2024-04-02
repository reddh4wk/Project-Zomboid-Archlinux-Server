#!/opt/pzserver/python/bin/python

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    (@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    @@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@, %@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ,@@@@@@@@@@@@@@@@@@@@@  @@@@@        @@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@%        @@       @@      @@   /@@&     .@@@     #%    /@@@@  .      @@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@%  /@@  .@&  #@@@@  ,@@,  @&  /@@  .@@  /@.  @@@@@@  *@@@@@, @@      @@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@(  /@@  ,@@  #@@@%  *@@   @@  (@&  ,@@@@@@  .@@@@@@  *@@@@@  @.    ,&*@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@(  ,@@  #@@  #@@@@, .@@  #@@  (@@*  @@@(/@(  @@@ /@  *@@@@@@%   (. .@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@.  /@@@@@@@@@@@@@@@@@@@@@#@%  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@,  .@@%  @@@@@@@@@@@@@@@@@@@@@@@@@
#@                 @@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@&&&@@@@@@@@@@@@@@@@@@   (@@@  (@@@@@@@@@@@@@@@@@@@@@@@@@
#                  /@@%     .%@@@@@@@@@@@@@@@@@@@@@@@@@@@*            .@@@@@@@@@@       (@@@(  #@@@@           ,/@@@@@@@@
#      &@@@@@     *@@     .    &@       .@@@@@@@@        @#    /@@@.    &@@@@@          .@@@@.      @%     .*.     %@@@@@
#     &@@@@@      @@,   &@@&    @@       /@@@@@@       ,@@%    %@@@@     #@@,     @@@/    #@@@    .@@@     @@@@*    @@@@@
#    &@@@@@      (@@   .@@@@    /@(      ,@@@@@/       (@@*    (@@@@(    ,@@.    @@@@@     %@@    &@@@     @@@@@     &@@@
#   *@@@@@#      @@.   %@@@@    .@(       &@@@@        #@@@    /@@@@.    %@@     @@@@@*    (@@    @@@#     @@@@@#    .@@@
#/ @@@@@@@      @@@    &@@@@     @#       .@@@@        /@@#    (@@@.     @@*     @@@@@     ,@@    %@@@     @@@@@@     @@@
#@@@@@@@@      &@@@    %@@@@     @#        #@@#        ,@@#    ,@@(     @@@     /@@@@@.     @@    #@@@     &@@@@&     @@@
#@@@@@@@      #@@@,    #@@@@     &#        *@@*        .@@@           (@@@@     %@@@@@*     %@    *@@@     (@@@@      %@@
#@@@@@@&     *@@@@,    (@@@@/    @#   .     @%          @@#    (@@@     %@@     &@@@@@@     ,@.   /@@&     /@@@@      /@@
#@@@@@@      %@@@@,    /@@@@    ,@#   %@.        @#    .@@*    %@@@@,    #@     #@@@@@@     %@.   #@@@     (@@@@      ,@@
#@@@@@      *@@@@@@,   /@@@@    (@(   @@/       (@,    ,@@*    #@@@@/    ,@,    /@@@@@      @@    %@@@     @@@@@@     (@@
#@@@@      .@@@@@@@@   .@@@%    /@(   @@@       @@     *@@*    %@@@@     ,@*    ,@@@@@     ,@@    %@@@     @@@@@#     @@@
#@@@@      @@@@@@@( (    #/   .@@@,   (@@.     .@@.    (@@,    &@@@@     (@(    .@@@@@     #@@.   /@@@     @@@@@     #@@@
#@@@      %@@@@@@   /@@.    (@@@@@    .@@@     ,@@(    &@@,    %@@@      @@@    .@@@@@     &@&    .@@&.    @@@@@     @@@@
#@@      /@@@@@@    @@@@@@@@@@@@@@/   .@@@,    %@@     /@             (@@@@@@.   (@@@.     @@.     /@@    ,@@@@     @@@@@
#@      ,@@@@@@     @@@@@@@@@@@@@@    /@@@&   ,@@@     ,@@@@@@@@@@&@@@@@@@@@@@    ,@/    /@@@@@@@@@@@.      /     *@@@@@@
#@      @@@@@@      @@@@@@@@@@@@@      &@@@   @@@(      %@###%.,/###%@((    #@@@,      *@@@@@@@@@@@@@/ ,((,..*/%@@@@@@@@@
#                   &@@@@@@@@@@@@(,(#(*@@@@@@@@@@( ,//*,&@@                     /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##(*,,. ..,,*****,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&##                         .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         .%*/@@@( (%#/          /#&( &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     .#(   / .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Please install pip on your system, install the dependencies that will be throwing errors when you launch the program and create a separate python virtual environmment (very easy to do) to launch this software.
# Oh, also remember to get a telegram bot TOKEN from the botfather bot and replace the TOKEN variable value with it. You will need to put the group chat id in SERVER_CHATS. To get your group chat id, add the bot to the group chat and use the command /id
# Also make sure your bot is in your public group with admin priviledges and disable the privacy setting of your bot from botfather chat using /setprivacy command or whatever it is.
# I think this should be it...

# PZserver TG Module - Copyright (C) 2023 Damiano Meda
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail.
# If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:

# PZserver TG Module - Copyright (C) 2023 Damiano Meda
# This program comes with ABSOLUTELY NO WARRANTY; This is free software, and you are welcome to redistribute it under certain conditions. Contact me at damiano.meda@gmail.com if you want to do so.

########################################
### FUNDAMENTAL CONSTANTS
########################################

import os
import sys
import threading
import signal
import re

if __name__ == '__main__':
    if '--debug' in sys.argv:
        DEBUG_MODE = 1
    else:
        DEBUG_MODE = 0

if __name__ == '__main__':
    # USEFUL PATHS OF RECURRENT USAGE
    FILENAME = os.path.basename(os.path.realpath(__file__))
    BASENAME = os.path.splitext(FILENAME)[0]
    THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))
    THIS_LOG_FILE = os.path.join(THIS_FOLDER, "_"+BASENAME+'.log')
    SERVICE_FOLDER = os.path.abspath(os.path.join(THIS_FOLDER, os.pardir))
    SERVICE_NAME = os.path.basename(SERVICE_FOLDER) # Please put the server in a folder with a name different form "vanilla" or "default"
    SERVICE_LOG = os.path.join(SERVICE_FOLDER, SERVICE_NAME+'.log')
    HOME_FOLDER = os.path.expanduser("~")
    GAME_FOLDER=os.path.join(HOME_FOLDER, 'Zomboid')
    GAME_SETTINGS_FOLDER=os.path.join(GAME_FOLDER, 'Server')
    GAME_FILES_FOLDER = os.path.join(HOME_FOLDER, 'Zomboid/Saves/Multiplayer/'+SERVICE_NAME)
    GAME_VEHICLES_DB = os.path.join(GAME_FILES_FOLDER, 'vehicles.db')
    GAME_PLAYER_DB=os.path.join(GAME_FILES_FOLDER+'/players.db')
    GAME_SERVER_DB=os.path.join(GAME_FOLDER, 'db/'+SERVICE_NAME+'.db')

    #BACKUPS

    BACKUP_FOLDER = os.path.join(SERVICE_FOLDER, 'backups')

    # THIS WILL SLOW DOWN BOOT PROCESS A BIT
    AUTOUPDATE_VANILLA_SETTINGS_ON_START = 2 # 1=Always, 0=Never, 2=Only On Mod Changes
    VANILLA_SERVER_NAME = "vanilla"
    VANILLA_LOG_FILE = os.path.join(SERVICE_FOLDER, VANILLA_SERVER_NAME+".log")

    # CURRENT SETTINGS
    SERVERINI_PATH = os.path.join(GAME_SETTINGS_FOLDER, SERVICE_NAME+".ini")
    SANDBOXVARS_PATH = os.path.join(GAME_SETTINGS_FOLDER, SERVICE_NAME+"_SandboxVars.lua")
    # VANILLA SETTINGS
    VANILLA_SERVERINI_PATH = os.path.join(GAME_SETTINGS_FOLDER, VANILLA_SERVER_NAME+".ini")
    VANILLA_SANDBOXVARS_PATH = os.path.join(GAME_SETTINGS_FOLDER, VANILLA_SERVER_NAME+"_SandboxVars.lua")
    # USER_DEFINED STANDARD SETTINGS
    DEFAULT_SERVERINI_PATH = os.path.join(GAME_SETTINGS_FOLDER, "default.ini")
    DEFAULT_SANDBOXVARS_PATH = os.path.join(GAME_SETTINGS_FOLDER, "default_SandboxVars.lua")
    
    # TELEGRAM STUFF
    SERVER_CHATS=[] #Production
    DEBUG_CHAT = [] #Test
    TOKEN = '' # Telegram Bot API TOKEN
    DEVS=[] #Your telegram ID. It will allow you to force changes.
    
    # POLL SETTINGS
    POLL_EXPIRE_AFTER = 7                   # After this number of days, a poll expires and gets closed
    MISOABSTINENTIA = True                  # If this is set to true, a poll can pass before the expire period without reaching the consensus (WC mode)
    QUORUM = 0.5                            # At least this percentage of the people that create consensus need to vote even in WC mode.
    MINIMUM_DAYS = 3                        # At least this amount of days need to pass before the poll is approved even in WC mode.
    UNANIMITY_COEFFICIENT = 0.8             # At least this percentage of people need to agree for the WC mode pass.
    BOTS_PRESENT_IN_THE_GROUP_CHAT = 1      # The amount of bots in the group chat, to exclude them from the count to calculate consensus

    # GAME SERVER MANAGER
    SYSTEMCTL = False

########################################################################################################################
### INFORMATION FOR THE LOG FILE
########################################################################################################################

def log_timestamp():
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def logger(message, msg_type, log_file=THIS_LOG_FILE, nt=True): # nt stands for "need traceback"
    import os
    import traceback
    import sys
    silent_flag = '--silent' in sys.argv
    with open(log_file, 'a') as f:
        timestamp = log_timestamp()
        msg_body = f"[{timestamp}][{msg_type}] {str(message)}"
        if not silent_flag:
            if msg_type != 'DEBUG' or DEBUG_MODE:
                print(msg_body)
                f.write(msg_body+"\n")
        traceback_str = traceback.format_exc()
        if msg_type in ['ERROR','SQL_ERROR'] and nt:
            if traceback_str:
                msg_body = f"[{timestamp}][TRACEBACK] {traceback_str}"
                if DEBUG_MODE:
                    print(msg_body)
                f.write(msg_body+"\n")

def log_emendazio(max_rows=1000, buffer=300, log_file=THIS_LOG_FILE):
    try:
        with open(log_file, 'r') as f:
                lines = f.readlines()
                if len(lines) >= max_rows:
                    lines = lines[-(max_rows - buffer):]
                with open(log_file, 'w') as f:
                    f.writelines(lines)
    except Exception as e:
        logger(e, "ERROR")
        return None

########################################################################################################################
### USEFUL TOOLS
########################################################################################################################

def string_is_integer(s):
    try:
        int(s)
        return True
    except Exception as e:
        logger(e, "ERROR")

def timestamp():
    try:
        from datetime import datetime
        return datetime.now()
    except Exception as e:
        logger(e, "ERROR")

def unix_timestamp():
    try:
        import time
        return int(time.time())
    except Exception as e:
        logger(e, "ERROR")

def backup_timestamp():
    try:
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
    except Exception as e:
        logger(e, "ERROR")

def unix_timestamp_to_log_timestamp(unix_timestamp):
    try:
        from datetime import datetime
        return datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        logger(e, "ERROR")

def log_timestamp_to_unix_timestamp(log_timestamp):
    try:
        from datetime import datetime
        return int(datetime.strptime(log_timestamp, '%Y-%m-%d %H:%M:%S').timestamp())
    except Exception as e:
        logger(e, "ERROR")

def run_command(command, log=True, always_print_output=False):
    try:
        if DEBUG_MODE:
            if log:
                logger(f"#!/bin/bash: {command}", "DEBUG")
        import subprocess
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        if process.returncode != 0:
            logger(f"Command execution failed with return code: {process.returncode}", "SYSERROR")
            if error:
                logger(f"SysError: {error.strip()}", "SYSERROR")
        if always_print_output:
            if log:
                logger(f"Command execution successful: {output.strip()}", "DEBUG")
        return [not process.returncode, output, error]
    except Exception as e:
        logger(f"An error occurred while executing command '{command}': {e.strip()}", "ERROR")
        return False

def run_command_on_gameserver(server_name, command):
    try:
        return run_command(f"tmux send-keys -t {server_name} '{command}' C-m")
    except Exception as e:
        logger(e, "ERROR")

def rm(path):
    try:
        if os.path.exists(path):
            return run_command("rm "+path)
    except Exception as e:
        logger(e, "ERROR")

def check_service_status(service_name=SERVICE_NAME):
    try:
        import subprocess
        if 'Active: active (running)' in run_command('systemctl status '+SERVICE_NAME)[1].split('\n')[2]:
            return True
        else:
            return False
    except Exception as e:
        logger(e, "ERROR")
        return None
    
def strip_img_url_from_steam(workshop_url):
    try:
        import re
        import requests
        response = requests.get(workshop_url)
        if response.status_code == 200:
            html_source = response.text
            pattern = r'https://steamuserimages-a\.akamaihd\.net/ugc/\d+/\w+/'
            match = re.search(pattern, html_source)
            if match:
                img_url = match.group()
                logger(f"A image url has been stripped from steam workshop: {img_url}", "DEBUG")
                return img_url
            else:
                logger(f"There was no match while searching for a valid image url in: {workshop_url}", "DEBUG")
                return None
        else:
            logger(f"Failed to fetch HTML content from: {workshop_url}, Status code: {response.status_code}", "ERROR")
            return None
    except Exception as e:
        logger(e, "ERROR")

def is_workshop_url(url):
    try:
        import re
        pattern = r"https:\/\/steamcommunity\.com\/sharedfiles\/filedetails\/\?id=\d+"
        if re.match(pattern, url):
            return True
        else:
            return False
    except Exception as e:
        logger(e, "ERROR")

def valid_steam_id(steam_id):
    try:
        if steam_id.isdigit() and len(steam_id) == 17:
            return int(steam_id)
        else:
            return False
    except Exception as e:
        logger(e, "ERROR")

def ensure_max_occurrences(array, value, N):
    try:
        count = 0
        index = 0
        while index < len(array):
            if array[index] == value:
                count += 1
                if count > N:
                    del array[index]
                    continue  # Continue without incrementing index
            index += 1
        return array
    except Exception as e:
        logger(e, "ERROR")

def format_time(seconds, precision='s'):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours > 0:
        if precision == 's':
            return f"{int(hours)} h {int(minutes)} m {int(seconds)} s"
        elif precision == 'm':
            return f"{int(hours)} h {int(minutes)} m"
        else:
            return f"{int(hours)} h"
    elif minutes > 0:
        if precision == 's':
            return f"{int(minutes)} m {int(seconds)} s"
        else:
            return f"{int(minutes)} m"
    else:
        return f"{int(seconds)} s"

def fake_message(chat_id, message_id):
    try:
        class fakemessage:
            def __init__(self, chat_id, message_id):
                self.chat_id = chat_id
                self.message_id = message_id
            @property
            def chat(self):
                return fakechat(self.chat_id)
            @property
            def id(self):
                return self.message_id
        class fakechat:
            def __init__(self, chat_id):
                self.chat_id = chat_id
            @property
            def id(self):
                return self.chat_id
        # Eat your broccoli, bitch
        return fakemessage(chat_id, message_id)
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### AVOID DOUBLE EXECUTION OF THIS SCRIPT ON THE CURRENT SYSTEM
########################################################################################################################

def get_pid_and_name():
    import os
    import sys
    try:
        return (os.getpid(), os.path.abspath(sys.argv[0]))
    except Exception as e:
        logger(e, "ERROR")

def is_already_running(current_pid, current_script):
    try:
        processes = run_command('ps aux | grep ' + current_script)[1]
        if processes:
            lines = processes.split('\n')
            for line in lines:
                if current_script in line and 'python' in line:
                    pid = int(line.split()[1])
                    if pid != current_pid:
                        logger(f"Processes found already running:\n{processes.strip()}", "DEBUG")
                        return True, pid
        return False, None
    except Exception as e:
        logger(e, "ERROR")

def stop_previous_instance(pid, signal_type):
    try:
        import os
        import signal
        logger(f"Stopping previous instance with PID: {pid}", "INFO")
        if signal_type == 'violent':
            os.kill(pid, signal.SIGKILL)
        if signal_type == 'graceful':
            os.kill(pid, signal.SIGTERM)
    except Exception as e:
        logger(e, "ERROR")

if __name__ == '__main__':
    try:
        import sys
        pid, name = get_pid_and_name()
        restart_flag = '--restart' in sys.argv
        stop_flag = '--stop' in sys.argv
        shutdown_flag = '--shutdown' in sys.argv
        already_running, running_pid = is_already_running(pid, name)
        if restart_flag and stop_flag:
            logger("Flags --restart and --stop cannot be called at the same time", "ERROR", nt=False)
            sys.exit(1)
        if already_running:
            if restart_flag:
                if running_pid:
                    stop_previous_instance(running_pid, 'violent')
                else:
                    logger("Couldn't determine the PID of the previous instance.", "ERROR", nt=False)
                    sys.exit(1)
            elif stop_flag:
                if running_pid:
                    stop_previous_instance(running_pid, 'violent')
                    sys.exit(0)
                else:
                    logger("Couldn't determine the PID of the previous instance.", "ERROR", nt=False)
                    sys.exit(1)
            elif shutdown_flag:
                if running_pid:
                    stop_previous_instance(running_pid, 'graceful')
                    sys.exit(0)
            else:
                logger("Another instance of the script is already running.", "ERROR", nt=False)
                sys.exit(1)
        else:
            if stop_flag:
                logger("The server isn't running already. Since the --stop flag has been used, exiting.", "ERROR", nt=False)
                sys.exit(1)
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### INITIALIZE BOT
########################################################################################################################

if __name__ == '__main__':
    try:
        import telebot
        bot = telebot.TeleBot(TOKEN)
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### BOT RELATED USEFUL TOOLS
########################################################################################################################

def cheat_alert(text, disable_notification=True, disable_web_page_preview=False, parse_mode='Markdown'):
    try:
        for each in SERVER_CHATS:
            bot.send_message(each, text, disable_notification=disable_notification, disable_web_page_preview=disable_web_page_preview, parse_mode=parse_mode)
    except Exception as e:
        logger(e, "ERROR")

def server_chat_message(text, disable_notification=True, disable_web_page_preview=False, parse_mode='Markdown'):
    try:
        if not DEBUG_MODE:
            for each in SERVER_CHATS:
                bot.send_message(each, text, disable_notification=disable_notification, disable_web_page_preview=disable_web_page_preview, parse_mode=parse_mode)
        else:
            bot.send_message(DEBUG_CHAT[0], text, disable_notification=disable_notification, disable_web_page_preview=disable_web_page_preview, parse_mode=parse_mode)
    except Exception as e:
        logger(e, "ERROR")

def reply_to(message, text, disable_notification=True, disable_web_page_preview=False, parse_mode='MarkdownV2'):
    try:
        if parse_mode == 'MarkdownV2':
            special_characters = ['_','*','[',']','(',')','~','`','>','#','+','-','=','|','{','}','.','!']
            escaped_text = ''
            for char in text:
                if char in special_characters:
                    escaped_text += '\\' + char
                else:
                    escaped_text += char
            text = escaped_text
        logger(f"In reply to message:\n{message.text}", "DEBUG")
        logger(f"Reply:\n{text}", "DEBUG")
        bot.reply_to(message, text, disable_notification=disable_notification, disable_web_page_preview=disable_web_page_preview, parse_mode=parse_mode)
    except Exception as e:
        logger(e, "ERROR")

def member_is_admin(message):
    try:
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status in ['creator','administrator']:
            return True
        else:
            reply_to(message, "This command requires administrator-level or superior priviledges.", disable_notification=True)
            return False
    except Exception as e:
        logger(e, "ERROR")

def member_is_dev(message):
    try:
        if message.from_user.id in DEVS:
            return True
        else:
            reply_to(message, msg_only_master)
            return False
    except Exception as e:
        logger(e, "ERROR")

def split_msg_in_chunks(text, telegram_msg_max_lenght=4096):
    try:
        chunks = []
        current_text = ""
        if text:
            if isinstance(text, str):
                for line in text.splitlines():
                    if len(current_text) + len(line) > telegram_msg_max_lenght:
                        chunks.append(current_text)
                        current_text = ""
                    current_text += line+"\n"
                if current_text:
                    chunks.append(current_text)
                return chunks
            else:
                return ["(ಠ ∩ಠ)"]
        else:
            return ["(ಠ ∩ಠ)"]
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### DATABASES PLAYGROUND
########################################################################################################################

if __name__ == '__main__':
    import os
    pztgdb = os.path.join(THIS_FOLDER, 'pztg.db')
    if DEBUG_MODE:
        debug_db = os.path.join(THIS_FOLDER, '_pztg_debug.db')
        run_command(f"cp {pztgdb} {debug_db}")
        pztgdb = debug_db
        logger(f"Debug database is being used: {debug_db}", "DEBUG")

class Reform:
    def __init__(self, reform_id=None, reform_chat_id=None, reform_name=None, reform_description=None, reform_date=None, reform_implemented=None, reform_is_active = None,
                poll_id=None, poll_message_id=None, poll_options=None,poll_consensus_coefficient=None, poll_stop_date=None, poll_yes_list="", poll_no_list="",
                change_ctype=None, change_mod_action=None, change_mod_modid=None, change_mod_workshopid=None, change_setting_variable=None, change_setting_old_value=None, change_setting_new_value=None,
                proposer_first_name=None, proposer_last_name=None, proposer_username=None, proposer_id=None):
        self.reform_id = reform_id
        self.reform_chat_id = reform_chat_id
        self.reform_name = reform_name
        self.reform_description = reform_description
        self.reform_date = reform_date
        self.reform_implemented = reform_implemented
        self.reform_is_active = reform_is_active
        self.poll_id = poll_id
        self.poll_message_id = poll_message_id
        self.poll_options = poll_options
        self.poll_consensus_coefficient = poll_consensus_coefficient
        self.poll_stop_date = poll_stop_date
        self.poll_yes_list = poll_yes_list
        self.poll_no_list = poll_no_list
        self.change_ctype = change_ctype
        self.change_mod_action = change_mod_action
        self.change_mod_modid = change_mod_modid
        self.change_mod_workshopid = change_mod_workshopid
        self.change_setting_variable = change_setting_variable
        self.change_setting_old_value = change_setting_old_value
        self.change_setting_new_value = change_setting_new_value
        self.proposer_first_name = proposer_first_name
        self.proposer_last_name = proposer_last_name
        self.proposer_username = proposer_username
        self.proposer_id = proposer_id
    
    def print_all(self):
        for var_name, var_value in vars(self).items():
            print(f"{var_name}: {var_value}")

def init_reform_table():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS reforms
            (
                reform_id INTEGER PRIMARY KEY,
                reform_chat_id INTEGER,
                reform_name TEXT,
                reform_description TEXT,
                reform_date INTEGER,
                reform_implemented INTEGER,
                reform_is_active INTEGER,
                poll_id INTEGER,
                poll_message_id INTEGER,
                poll_options INTEGER,
                poll_consensus_coefficient REAL,
                poll_stop_date INTEGER,
                poll_yes_list TEXT,
                poll_no_list TEXT,
                change_ctype TEXT,
                change_mod_action TEXT,
                change_mod_modid TEXT,
                change_mod_workshopid TEXT,
                change_setting_variable TEXT,
                change_setting_old_value TEXT,
                change_setting_new_value TEXT,
                proposer_first_name TEXT,
                proposer_last_name TEXT,
                proposer_username TEXT,
                proposer_id INTEGER
            )''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")

class Player:
    def __init__(self, ID, username, banned, accesslevel, firstconnection, lastconnection, steam_id, telegram_id):
        self.ID = ID
        self.username = username
        self.banned = banned
        self.accesslevel = accesslevel
        self.firstconnection = firstconnection
        self.lastconnection = lastconnection
        self.steam_id = steam_id
        self.telegram_id = telegram_id
    def print_all(self):
        for var_name, var_value in vars(self).items():
            print(f"{var_name}: {var_value}")

def init_players_table():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS players
            (
                id INTEGER PRIMARY KEY,
                username TEXT,
                banned INTEGER,
                accesslevel TEXT,
                firstconnection TEXT,
                lastconnection TEXT,
                steam_id INTEGER,
                telegram_id INTEGER
            )''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")

class Session:
    def __init__(self, session_id=None, steam_id=None):
        self.session_id = session_id
        self.steam_id = steam_id

    def print_all(self):
        for var_name, var_value in vars(self).items():
            print(f"{var_name}: {var_value}")

def init_sessions_table():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS sessions
            (
                session_id INTEGER PRIMARY KEY,
                steam_id INTEGER,
                login INTEGER,
                logout INTEGER,
                ip TEXT
            )''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")

def init_mfa_table():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS mfa 
            (
                id INTEGER PRIMARY KEY,
                steam_id INTEGER,
                telegram_id INTEGER,
                chat_id INTEGER,
                message_id INTEGER,
                confirmed INTEGER,
                submitted_on INTEGER,
                pending_removal INTEGER
            )''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")

def init_pending_queries_table():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS pending_queries 
            (
                id INTEGER PRIMARY KEY,
                query_type TEXT,
                db_path TEXT,
                query TEXT,
                pending INTEGER,
                chat_id INTEGER,
                message_id INTEGER
            )''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")

if __name__ == '__main__':
    try:
        init_reform_table()
        init_players_table()
        init_sessions_table()
        init_mfa_table()
        init_pending_queries_table()
    except Exception as e:
        logger(e, "ERROR")

########################################
### DB FUNCTIONS
########################################

def get_pending_rename_data(get_fake_message=False):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT id, query, chat_id, message_id FROM pending_queries WHERE query_type = 'rename' AND pending = 1''')
        pending = c.fetchall()
        if pending:
            import re
            data = []
            pattern = r"UPDATE \w+ SET username = '([^']+)' WHERE username = '([^']+)' AND steam_id = (\d+)"
            for ID, query, chat_id, message_id in pending:
                match = re.match(pattern, query)
                if match:
                    new_username = match.group(1)
                    old_username = match.group(2)
                    steam_id = int(match.group(3))
                    if not get_fake_message:
                        data.append([ID, old_username, new_username, steam_id])
                    else:
                        data.append([ID, old_username, new_username, steam_id, fake_message(chat_id, message_id)])
            return data
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def sync_with_server_whitelist():
    try:
        import sqlite3
        from datetime import datetime
        TEMP_DB = os.path.join(THIS_FOLDER, "tmp.db")
        # Need to copy to another file to open it since it's already open by the game. Also safer to touch just the copy.
        run_command(f'cp {GAME_SERVER_DB} {TEMP_DB}')
        # Let's open the bot DB
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        # And attach the game DB to make use of more efficient sorting functions even if we don't realistically really need it
        c.execute(f"ATTACH DATABASE '{TEMP_DB}' AS game_server_db")
        c.execute('''
            SELECT w.username, w.banned, w.lastconnection, w.steamid, w.accesslevel 
            FROM game_server_db.whitelist w
            LEFT JOIN players p ON w.username = p.username AND w.steamid = p.steam_id
            WHERE p.steam_id IS NULL and w.steamid IS NOT NULL''')
        missing_entries = c.fetchall()
        c.execute('''
            SELECT w.username, w.lastconnection, w.steamid
            FROM game_server_db.whitelist w
            LEFT JOIN players p ON w.username = p.username AND w.steamid = p.steam_id
            WHERE p.lastconnection <> w.lastconnection''')
        latest_connections = c.fetchall()
        # Add missing entries to the players table
        for entry in missing_entries:
            username, banned, lastconnection, steamid, accesslevel = entry
            firstconnection = log_timestamp()
            # Check if there is a corresponding telegramid in the mfa table
            c.execute("SELECT telegram_id FROM mfa WHERE steam_id = ? AND confirmed = 1", (steamid,))
            result = c.fetchone()
            if result:
                telegramid = result[0]
            else:
                telegramid = None
            # Finally, insert the entry into the players table
            c.execute('''
                INSERT INTO players (username, banned, accesslevel, firstconnection, lastconnection, steam_id, telegram_id)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (username, banned, accesslevel, firstconnection, lastconnection, steamid, telegramid))
        for entry in latest_connections:
            username, lastconnection, steamid = entry
            c.execute('''UPDATE players SET lastconnection = ? WHERE steam_id = ? AND username = ?''', (lastconnection, steamid, username))
        # Check if there's any conflict between a new username and an existing pending rename request
        c.execute('SELECT username FROM players')
        player_usernames = c.fetchall()
        pending = get_pending_rename_data(get_fake_message=True)
        if pending:
            for ID, pending_old_username, pending_new_username, pending_steam_id, fake_message in pending:
                if any(pending_new_username == username for username in player_usernames):
                    c.execute('''DELETE FROM pending_queries WHERE id = ?''', (ID,))
                    reply_to(fake_message, "Another user logged in with the username you wanted to use before reboot. Request canceled.")
        # Commit the changes and close the connection
        conn.commit()
        # And clean by removing the temporary copy
        rm(TEMP_DB)
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def add_to_pending_queries(query_type, db_path, query, chat_id, message_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''INSERT INTO pending_queries (query_type, db_path, query, pending, chat_id, message_id) VALUES (?, ?, ?, 1, ?, ?)''', (query_type, db_path, query, chat_id, message_id))
        conn.commit()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def execute_query(db_path, query):
    try:
        logger("Executing query: "+query, "DEBUG")
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(query)
        logger("Query executed successfully.", "DEBUG")
        conn.commit()
        return True
    except sqlite3.Error as e:
        logger(f"SQLite error: {e}", "SQL_ERROR")
        return False
    except Exception as e:
        logger(f"Error: {e}", "ERROR")
        return False
    finally:
        if conn:
            conn.close()

def run_pending_queries():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT id, db_path, query FROM pending_queries WHERE pending = 1''')
        queries = c.fetchall()
        for ID, db_path, query in queries:
            execute_query(db_path, query)
            c.execute('''UPDATE pending_queries SET pending = 0 WHERE ID = ?''', (ID,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def delete_pending_rename(username, steam_id):
    try:
        pending = get_pending_rename_data()
        if get_pending_rename_data():
            import sqlite3
            conn = sqlite3.connect(pztgdb)
            c = conn.cursor()
            for ID, pending_old_username, pending_new_username, pending_steam_id in pending:
                if pending_old_username == username and pending_steam_id == steam_id:
                    c.execute('''DELETE FROM pending_queries WHERE id = ?''', (ID,))
                    deleted = True
            conn.commit()
            return deleted
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def submit_mfa_registration(steam_id, telegram_id, message):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''INSERT INTO mfa (steam_id, telegram_id, chat_id, message_id, confirmed, submitted_on) VALUES (?, ?, ?, ?, ?, ?)''', (int(steam_id), int(telegram_id), int(message.chat.id), int(message.id), 0, unix_timestamp()))
        conn.commit()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def player_set_telegram_id(steam_id, telegram_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT * FROM players WHERE steam_id = ?''', (int(steam_id),))
        existing_player = c.fetchone()
        if existing_player:
            c.execute('''UPDATE players SET telegram_id = ? WHERE steam_id = ?''', (int(telegram_id), int(steam_id)))
            conn.commit()
            return True
        conn.close()
        return False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def confirm_mfa_registration(steam_id, username, telegram_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute(f'''UPDATE mfa SET confirmed = 1, pending_removal = 1 WHERE steam_id = {int(steam_id)} AND telegram_id = {int(telegram_id)}''')
        c.execute(f'''UPDATE players SET telegram_id = {telegram_id} WHERE steam_id = {steam_id}''')
        conn.commit()
        pending_query_type = 'mfa'
        add_to_pending_queries(pending_query_type, GAME_SERVER_DB, '''DELETE FROM whitelist WHERE steam_id = ? AND username = ?''', (steam_id, username))
        add_to_pending_queries(pending_query_type, GAME_PLAYER_DB, '''DELETE FROM networkPlayers WHERE steam_id = ? AND username = ?''', (steam_id, username))
        add_to_pending_queries(pending_query_type, pztgdb, '''DELETE FROM players WHERE steam_id = ? AND username = ?''', (steam_id, username))
        add_to_pending_queries(pending_query_type, pztgdb, '''UPDATE mfa SET pending_removal = 0 WHERE steam_id = ? AND telegram_id = ?''', (steam_id, telegram_id))
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_mfa_registrants():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT steam_id, telegram_id, chat_id, message_id, confirmed FROM mfa WHERE confirmed = 0 OR pending_removal = 1''')
        results = c.fetchall()
        MFA = []
        for steam_id, telegram_id, chat_id, message_id, confirmed in results:
            MFA.append([steam_id, telegram_id, fake_message(chat_id, message_id), confirmed])
        return MFA
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def save_reform(reform):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        # Check if the reform already exists in the table
        c.execute('''SELECT * FROM reforms WHERE reform_id = ?''', (reform.reform_id,))
        existing_reform = c.fetchone()
        if existing_reform:
            # Reform exists, update it
            update_columns = ', '.join([f"{col} = ?" for col in reform.__dict__.keys()])
            update_values = tuple(reform.__dict__.values()) + (reform.reform_id,)  # Include reform_id for WHERE clause
            c.execute(f'''UPDATE reforms SET {update_columns} WHERE reform_id = ?''', update_values)
        else:
            # Reform does not exist, insert it
            columns = ', '.join([col for col in reform.__dict__.keys()])
            placeholders = ', '.join(['?' for _ in range(len(reform.__dict__))])
            values = tuple(reform.__dict__.values())
            c.execute(f'''INSERT INTO reforms ({columns}) VALUES ({placeholders})''', values)
        conn.commit()
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_player(steam_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT * FROM players WHERE steam_id = ?''', (int(steam_id),))
        result = c.fetchone()
        if result:
            return Player(*result)
        else:
            return None
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_player_list():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT username FROM players''')
        result = c.fetchall()
        return result
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_reform(reform_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT * FROM reforms WHERE reform_id = ?''', (int(reform_id),))
        result = c.fetchone()
        if result:
            return Reform(*result)
        else:
            return None
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_active_reforms():
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT * FROM reforms WHERE reform_is_active = 1''')
        active_reforms = c.fetchall()
        if active_reforms:
            result = []
            for reform in active_reforms:
                result.append(Reform(*reform))
            return result
        else:
            return None
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_reform_by_poll_id(poll_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT * FROM reforms WHERE poll_id = ?''', (int(poll_id),))
        result = c.fetchone()
        if result:
            return Reform(*result)
        else:
            return None
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_mod_clone_change(modid, workshopid, action):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT * FROM reforms WHERE change_mod_modid = ? AND change_mod_workshopid = ? AND change_mod_action = ? AND reform_is_active = ?''', (modid, int(workshopid), action, 1))
        result = c.fetchone()
        if result:
            return Reform(*result)
        else:
            return False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_setting_clone_change(variable, new_value):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT * FROM reforms WHERE change_setting_variable = ? AND change_setting_new_value = ? AND reform_is_active = ?''', (variable, new_value, 1))
        result = c.fetchone()
        if result:
            return Reform(*result)
        else:
            return False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def player_get_telegram_id(steam_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT telegram_id FROM players WHERE steam_id = ?''', (int(steam_id),))
        result = c.fetchone()
        if result:
            return result[0]
        else:
            return False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def user_is_registered(telegram_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT steam_id FROM mfa WHERE telegram_id=? AND confirmed=?''', (int(telegram_id),1))
        steam_id = c.fetchone()
        return steam_id[0] if steam_id else False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def  player_is_registered(steam_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''SELECT telegram_id FROM mfa WHERE steam_id=? AND confirmed=?''', (int(steam_id),1))
        telegram_id = c.fetchone()
        return telegram_id[0] if telegram_id else False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def session_open(steam_id, ip):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''INSERT INTO sessions (steam_id, login, ip) VALUES (?, ?, ?)''', (int(steam_id), unix_timestamp(), ip))
        session_id = c.lastrowid
        conn.commit()
        return session_id
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def session_close(session_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute('''UPDATE sessions SET logout = ? WHERE session_id = ?''', (unix_timestamp(), int(session_id)))
        conn.commit()
        return True
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_user_activity_info(telegram_id):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()

        # Get steam_id associated with the provided telegram_id
        c.execute('''SELECT steam_id, firstconnection FROM players WHERE telegram_id=?''', (telegram_id,))
        steam_id, firstconnection = c.fetchone()
        firstconnection = log_timestamp_to_unix_timestamp(firstconnection)

        # Get count of logins, total time connected, and average session duration
        c.execute('''SELECT COUNT(*), SUM(logout - login), AVG(logout - login) FROM sessions WHERE steam_id=?''', (steam_id,))
        login_count, total_time_connected, avg_session_duration = c.fetchone()

        # Get the number of reforms proposed by the user
        c.execute('''SELECT COUNT(*) FROM reforms WHERE proposer_id=?''', (telegram_id,))
        proposed_reforms_count = c.fetchone()[0]

        # Get the number of proposed reforms that got implemented
        c.execute('''SELECT COUNT(*) FROM reforms WHERE proposer_id=? AND reform_implemented=1''', (telegram_id,))
        implemented_reforms_count = c.fetchone()[0]

        # Get the number of times the user voted yes, no, and didn't vote
        c.execute('''SELECT poll_yes_list, poll_no_list, reform_date FROM reforms''')
        reforms_data = c.fetchall()

        voted_yes_count = 0
        voted_no_count = 0
        did_not_vote_count = 0
        poll_count = 0

        for poll_yes_list, poll_no_list, reform_date in reforms_data:
            # Check if the user could have possibly voted based on their join date
            if firstconnection <= reform_date:
                poll_yes_list = poll_yes_list.split(",") if poll_yes_list else []
                poll_no_list = poll_no_list.split(",") if poll_no_list else []
                poll_count += 1
                # Check if user's telegram_id is in yes list
                if str(telegram_id) in poll_yes_list:
                    voted_yes_count += 1
                # Check if user's telegram_id is in no list
                elif str(telegram_id) in poll_no_list:
                    voted_no_count += 1
                else:
                    did_not_vote_count += 1
        
        voted_yes_perc = (voted_yes_count / poll_count * 100) if poll_count != 0 else 0
        voted_no_perc = (voted_no_count / poll_count * 100) if poll_count != 0 else 0
        did_not_vote_perc = (did_not_vote_count / poll_count * 100) if poll_count != 0 else 0
        reforms_approved_perc = round(implemented_reforms_count/proposed_reforms_count*100) if proposed_reforms_count != 0 else 0

        return f'''<b>Login count</b>: {login_count}
<b>Total time played</b>: {format_time(total_time_connected, 'm')}
<b>Average session</b>: {format_time(avg_session_duration, 'm')}

<b>Zombie Killed:</b> {'2'}

<b>Reforms proposed</b>: {proposed_reforms_count} ({reforms_approved_perc}% approved)

Out of {poll_count} polls, you voted:
<b>Yes</b>: {voted_yes_count} ({round(voted_yes_perc)}%) - <b>No</b>: {voted_no_count} ({round(voted_no_perc)}%) - <b>Blank</b>: {did_not_vote_count} ({round(did_not_vote_perc)}%)'''

    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

########################################################################################################################
### SERVER SETTINGS
########################################################################################################################

def save_setting_to_file(variable_name, value, table_name='main'):
    try:
        current_setting = get_setting(variable_name, table_name=table_name)
        file_path = current_setting['file_path']
        with open(file_path, 'r') as file:
            all_lines = file.readlines()
            line_number = current_setting['line_number']
            line = all_lines[line_number]
            if variable_name in line:
                if current_setting['value'] != "":
                    new_line = line.replace(current_setting['value'], value)
                else:
                    if ".ini" in current_setting['basename']:
                        line = line.split("=")
                        line.insert(1, "="+value)
                        new_line = ''.join(line)
                    elif ".lua" in current_setting['basename']:
                        line = line.split("=")
                        line.insert(1, "= "+value)
                        new_line = ''.join(line)
                    else:
                        logger(f"Not determinable file type for: {current_setting['basename']}", "ERROR", nt=False)
                logger(f"In {file_path}: \"{new_line.strip()}\"", "CHANGE")
                all_lines[line_number] = new_line
                with open(file_path, 'w') as file:
                    file.writelines(all_lines)
                return True
            return False
    except Exception as e:
        logger(e, "ERROR")

def process_serverini(line):
    try:
        if line.startswith("#"):
            return (1, line.strip()[2:])
        elif "=" in line:
            line = line.split("=")
            variable, value = line[0].strip(), line[1].strip()
            return (0, (variable, value))
        else:
            return None
    except Exception as e:
        logger(e, "ERROR")

def process_sandbox_vars(line):
    try:
        if "=" in line:
            if "{" in line:
                return None
            elif "--" in line:
                return (1, line.strip()[3:])
            else:
                line = line.split("=")
                variable, value = line[0].strip(), line[1].strip()[:-1]
                return (0, (variable, value))
        else:
            return None
    except Exception as e:
        logger(e, "ERROR")

if __name__ == '__main__':
    #.ini
    SERVERINI = [SERVERINI_PATH, process_serverini]
    VANILLA_SERVERINI = [VANILLA_SERVERINI_PATH, process_serverini]
    DEFAULT_SERVERINI = [DEFAULT_SERVERINI_PATH, process_serverini]
    #_SandboxVars.lua
    SANDBOXVARS = [SANDBOXVARS_PATH, process_sandbox_vars]
    VANILLA_SANDBOXVARS = [VANILLA_SANDBOXVARS_PATH, process_sandbox_vars]
    DEFAULT_SANDBOXVARS = [DEFAULT_SANDBOXVARS_PATH, process_sandbox_vars]

def reload_settings(serverini=SERVERINI, sandboxvars=SANDBOXVARS, table_name='main'):
    try:
        import os
        if os.path.exists(serverini[0]) and os.path.exists(sandboxvars[0]):
            settings_table_name = table_name+'_settings'
            paths_table_name = table_name+'_paths'
            setting_files = [serverini, sandboxvars]
            import sqlite3
            conn = sqlite3.connect(pztgdb)
            c = conn.cursor()
            c.execute(f'''
                CREATE TABLE IF NOT EXISTS {paths_table_name} (
                    id INTEGER PRIMARY KEY,
                    file_path TEXT,
                    basename TEXT,
                    table_associated TEXT
                )
            ''')
            c.execute(f'''
                CREATE TABLE IF NOT EXISTS {settings_table_name} (
                    id INTEGER PRIMARY KEY,
                    variable TEXT,
                    value TEXT,
                    description TEXT,
                    line_number INTEGER,
                    paths_table_ID INTEGER
                )
            ''')
            c.execute(f'''DELETE FROM {settings_table_name}''')
            c.execute(f'''DELETE FROM {paths_table_name} WHERE table_associated = ?''', (table_name,))
            for file_path, processor in setting_files:
                basename = os.path.basename(file_path)
                c.execute(f'''INSERT INTO {paths_table_name} (file_path, basename, table_associated) VALUES (?, ?, ?)''', (file_path, basename, table_name))
                paths_table_ID = c.lastrowid
                with open(file_path, 'r') as file:
                    description = ""
                    line_number = 0
                    for line in file:
                        processed = processor(line)
                        if processed:
                            is_description, data = processed[0], processed[1]
                            if is_description:
                                description += data + "\n"
                            else:
                                variable, value = data
                                c.execute(f'''INSERT INTO {settings_table_name} (variable, value, description, line_number, paths_table_ID)
                                    VALUES (?, ?, ?, ?, ?)''', (variable, value, description, line_number, paths_table_ID))
                                #print("section: " + basename); print(variable + ": " + value); print(description); print(line_number); print("-------------------------")
                                description = ""
                        line_number += 1
            conn.commit()
            conn.close()
            return True
        logger(f"\'{serverini[0]}\' or \'{sandboxvars[0]}\' wasn't found.", "ERROR", nt=False)
        return False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")

def compare_settings(subj_settings, ref_settings, as_text=False, console=False, exclusion_list=[], exclude_AntiCheatProtectionType=True):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)  # Connect to the database
        c = conn.cursor()
        # Retrieve settings from the database for both subj_settings and ref_settings
        c.execute(f'''SELECT * FROM {subj_settings+"_settings"}''')
        subject = c.fetchall()
        c.execute(f'''SELECT * FROM {ref_settings+"_settings"}''')
        reference = c.fetchall()
        differences = []
        missing_in_subject = []
        missing_in_reference = []
        # Iterate over subject and compare with reference
        for subj_row in subject:
            if subj_row[1] in exclusion_list:
                continue
            ref_row = next((ref for ref in reference if ref[1] == subj_row[1]), None)
            if ref_row:
                if subj_row[2] != ref_row[2]:
                    if exclude_AntiCheatProtectionType:
                        if not subj_row[1].startswith("AntiCheatProtectionType"):
                            differences.append((subj_row[1], subj_row[2], ref_row[2]))
                    else:
                        differences.append((subj_row[1], subj_row[2], ref_row[2]))
            else:
                missing_in_reference.append((subj_row[1], subj_row[2]))
        # Check for settings in reference but not in subject
        for row in reference:
            if not any(row[1] == subj_row[1] for subj_row in subject):
                missing_in_subject.append((row[1], row[2]))
        # Optionally return results as text
        if as_text:
            text_differences = ""
            for row in differences:
                if not console:
                    line = f"<b>{row[0]}</b>: {row[1]} | {row[2]}\n"
                else:
                    line = f"[{basename}] {row[0]}: {row[1]} [{basename}: {row[2]}]\n"
                text_differences += line
            return split_msg_in_chunks(text_differences)
        else:
            return [differences, missing_in_subject, missing_in_reference]
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def get_setting(variable_name, table_name='main'):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute(f'''SELECT * FROM {table_name+'_settings'} WHERE variable = ?''', (variable_name,))
        result = c.fetchone()
        if result:
            column_names = [description[0] for description in c.description]
            setting_dict = {column_names[i]: result[i] for i in range(len(column_names))}
            c.execute(f'''SELECT * FROM {table_name+'_paths'} WHERE id = ?''', (setting_dict['paths_table_ID'],))
            path_result = c.fetchone()
            if path_result:
                path_column_names = [description[0] for description in c.description]
                setting_dict.pop('paths_table_ID', None)
                for i in range(len(path_column_names)):
                    if path_column_names[i] != 'table_associated':
                        setting_dict[path_column_names[i]] = path_result[i]
            return setting_dict
        else:
            return False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

def set_setting_value(variable_name, value, table_name='main'):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        c = conn.cursor()
        c.execute(f'''UPDATE {table_name+'_settings'} SET value = ? WHERE variable = ?''', (value, variable_name))
        save_setting_to_file(variable_name, value, table_name=table_name)
        conn.commit()
        return True
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    if not reload_settings():
        print("File settings were not found. Being an almost essential part, I'll exit.")
        exit()

########################################
### MOD MANAGER & TOOLS
########################################

def is_modid(mod_id):
    try:
        return (char.isalnum() or char == '_' for char in mod_id)
    except Exception as e:
        logger(e, "ERROR")

def is_workshopid(workshop_id):
    try:
        return all(char.isdigit() for char in workshop_id) and len(workshop_id) in [9,10] # Yes, I found some with 9 digits
    except Exception as e:
        logger(e, "ERROR")

def sort_valid_modid_workshopid(id1, id2):
    try:
        if is_workshopid(id1):
            if is_modid(id2):
                return[id2,id1]
            else:
                return False
        elif is_workshopid(id2):
            if is_modid(id1):
                return[id1,id2]
            else:
                return False
        else:
            return False
    except Exception as e:
        logger(e, "ERROR")

def valid_modid_list(modid_list):
    try:
        if not modid_list:
            return True  # Empty string is allowed
        return all(is_modid(item) for item in modid_list)
    except Exception as e:
        logger(e, "ERROR")

def valid_workshopid_list(workshopid_list):
    try:
        if not workshopid_list:
            return True  # Empty string is allowed
        return all(is_workshopid(item) for item in workshopid_list)
    except Exception as e:
        logger(e, "ERROR")

def valid_modid_workshopid_list(modid_list, workshopid_list):
    try:
        return len(modid_list) == len(workshopid_list) and valid_modid_list(modid_list) and valid_workshopid_list(workshopid_list)
    except Exception as e:
        logger(e, "ERROR")

def get_mod_and_workshopid_list():
    try:
        modid_list = get_setting('Mods')['value']
        workshopid_list = get_setting('WorkshopItems')['value']
        if modid_list and workshopid_list:
            return ((modid_list.split(';'), workshopid_list.split(';')))
        else:
            return (([],[])) # No mods installed
    except Exception as e:
        logger(e, "ERROR")

def get_valid_modid_workshopid_list():
    try:
        modid_list, workshopid_list = get_mod_and_workshopid_list()
        if valid_modid_workshopid_list(modid_list, workshopid_list):
            return (modid_list, workshopid_list)
        else:
            logger("Sanity check failing for mod lists.", "WARNING")
            return False
    except Exception as e:
        logger(e, "ERROR")

def get_workshopid_from_installed_mods(modid):
    try:
        valid_mod_lists = get_valid_modid_workshopid_list()
        if valid_mod_lists:
            modid_list, workshopid_list = valid_mod_lists
            if is_modid(modid):
                if modid in modid_list:
                    return workshopid_list[modid_list.index(modid)]
                else:
                    return False
            else:
                return None
        else:
            return None
    except Exception as e:
        logger(e, "ERROR")
        return None

def strip_IDs_from_steam(url):
    try:
        import requests
        import re
        response = requests.get(url)
        if response.status_code == 200:
            source_code = response.text
            match = re.search(r"Mod ID:\s*([a-zA-Z0-9_()]+)", source_code)
            if match:
                mod_id = match.group(1)
                return sort_valid_modid_workshopid(mod_id, url.split('=')[1])
            return False
        else:
            logger(f"Failed to fetch page. Status code: {str(response.status_code)}", "ERROR", nt=False)
            return None
    except Exception as e:
        logger(e, "ERROR")
        return None
            
def mod_is_installed(id1, id2):
    try:
        valid = sort_valid_modid_workshopid(id1, id2)
        if valid:
            modid, workshopid = valid
            valid = get_valid_modid_workshopid_list()
            if valid:
                mod_list, workshop_list = valid
                if modid not in mod_list and workshopid not in workshop_list:
                    return False
                elif modid in mod_list:
                    if workshopid in workshop_list:
                        if mod_list.index(modid) == workshop_list.index(workshopid):
                            return True
                        else:
                            logger("Mod IDs entered in chat ("+modid+", "+workshopid+") resulted installed but are not at the same position in config file. If mods are being loaded correctly, you can safely ignore this warning.", "WARNING") #This case might be a hint for issues in loading mods in game
                            return None
                    elif workshopid not in workshop_list:
                        logger(f"{modid} is in the list but {workshopid} isn't. Weird, since a workshopid can have multiple modid but not viceversa. If mods are being loaded correctly, you can safely ignore this warning.", "WARNING") #This case might be a hint for issues in loading mods in game
                        return None
                else:
                    logger(f"{modid} is not in the list but {workshopid} is. It could be a portion of the same mod with a different name.", "INFO", THIS_LOG_FILE) #This case might be a hint for issues in loading mods in game
                    return False
            else:
                return valid
        else:
            logger("Mod IDs entered in chat ("+modid+", "+workshopid+") are invalid. Are you having fun or what?", "WARNING", THIS_LOG_FILE)
            return None
    except Exception as e:
        logger(e, "ERROR")
        return None

def install_mod(modid, workshopid, modid_setting='Mods', workshopid_setting='WorkshopItems'):
    try:
        modids=get_setting(modid_setting)['value']
        workshopids=get_setting(workshopid_setting)['value']
        set_setting_value(modid_setting, modids+";"+modid)
        set_setting_value(workshopid_setting, workshopids+";"+workshopid)
    except Exception as e:
        logger(e, "ERROR")

def uninstall_mod(modid, workshopid, modid_setting='Mods', workshopid_setting='WorkshopItems'):
    try:
        modid_list, workshopid_list = get_valid_modid_workshopid_list()
        position = modid_list.index(modid)
        modid_list.pop(position)
        workshopid_list.pop(position)
        modid_list_text = ';'.join(map(str, modid_list))
        workshopid_list_text = ';'.join(map(str, workshopid_list))
        set_setting_value('Mods', modid_list_text)
        set_setting_value('WorkshopItems', workshopid_list_text)
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### COMMAND SETUP & COMMAND RELATED
########################################################################################################################

### COMMANDS - FUNCTIONS

def add_cmd(command_list, cmd, description):
    try:
        from telebot import types
        #print("CMD: "+cmd+" ("+str(len(cmd))+")")
        #print("DESC: "+description+" ("+str(len(description))+")\n")
        command_list.append(types.BotCommand(command=str(cmd), description=str(description)))
        return True
    except Exception as e:
        logger(e, "ERROR")

def add_cmd_bulk(cmd_list):
    try:
        from telebot import types
        command_list = []
        for cmd, description in cmd_list:
            add_cmd(command_list, cmd, description)
        return command_list
    except Exception as e:
        logger(e, "ERROR")

def init_commands():
    try:
        
        return add_cmd_bulk([
            [start_cmd,start_desc],
            [restart_cmd,restart_desc],
            [status_cmd,status_desc],
            [stats_cmd,stats_desc],
            [compare_cmd,compare_desc],
            [mod_cmd,mod_desc],
            [setting_cmd,setting_desc],
            [rename_cmd,rename_desc],
            [register_cmd,register_desc],
            [log_cmd,log_desc],
            [help_cmd,help_desc],
            [force_cmd,force_desc],
            [backup_cmd,backup_desc]
        ])
    except Exception as e:
        logger(e, "ERROR")

### COMMAND - MESSAGES

if __name__ == '__main__':
    id_cmd='id'
    start_cmd='start'
    start_desc='Display bot welcome message.'
    start_msg='Hi, I am Rotting Ghoul! I can automatically get you updates on the status of the PZserver.'
    status_cmd='status'
    status_desc='Retrives the current status of '+SERVICE_NAME
    compare_cmd='diff'
    compare_desc='Shows differences between current settings and vanilla'
    compare_msg_helper='Shows variances between current and vanilla'
    force_cmd='force'
    force_desc='Forces the execution of some commands'
    restart_cmd='restart'
    restart_confirm_cmd='confirm_restart'
    restart_cancel_cmd='cancel_restart'
    restart_desc='Restarts the application'
    restart_msg="Are you really sure you want to restart the server? All users will be disconnected.\n\nPlease press: /"+restart_confirm_cmd+" to proceed.\n\nOr press: /"+restart_cancel_cmd+" to cancel."
    backup_cmd='backup'
    backup_desc='Allows to backup portions of the map, settings, players, vehicles and restore them'
    backup_msg_helper='''To use '''+backup_cmd+''' command please use:
        /'''+backup_cmd+''' save|restore <backup_name> <options>

Examples:
        /'''+backup_cmd+''' save <backup_name> --map <x1> <y1> <x2> <y2> --vehicles --players --settings --items
        /'''+backup_cmd+''' restore <backup_name> --map --vehicles --players --settings --items

For the coordinates, you can use this map:
https://map.projectzomboid.com/'''
    log_cmd = 'log'
    log_desc = 'Filters the log of this bot'
    log_msg_helper ='''To filter the logs, please use:
        /'''+log_cmd+''' <keyword>'''
    stats_cmd='stats'
    stats_desc='Displays account stats of a registered account'
    stats_msg_helper='''To see your stats use /'''+stats_cmd+''' or:
        /'''+stats_cmd+''' <steam id>  [for another player]'''
    mod_cmd='mod'
    mod_desc='Manages installed mods through polls'
    mod_msg_helper='''There are a few ways to use '''+mod_cmd+''' command. Please use one of the following forms:
        /'''+mod_cmd+''' list
        /'''+mod_cmd+''' install <Mod URL>
        /'''+mod_cmd+''' install <Mod ID> <Workshop ID>
        /'''+mod_cmd+''' uninstall <Mod URL>
        /'''+mod_cmd+''' uninstall <Mod ID>
        /'''+mod_cmd+''' uninstall <Mod ID> <Workshop ID>'''
    setting_cmd='setting'
    setting_desc='Manages server settings through polls'
    setting_msg_helper='''To use '''+setting_cmd+''' command please use:
        /'''+setting_cmd+''' get <parameter>
        /'''+setting_cmd+''' set <parameter> <value>'''
    rename_cmd='rename'
    rename_desc='Renames a selected character in game'
    rename_msg_helper='''To use '''+rename_cmd+''' command please use (use double quotes):
        /'''+rename_cmd+''' "<old username>" "<new username>"'''
    register_cmd='register'
    register_desc='Links the game account with your telegram account'
    register_msg_helper='''To link your game account and use /'''+stats_cmd+''' please use:
        /'''+register_cmd+''' <your steam id>
        
How to find your steam ID:
https://help.steampowered.com/en/faqs/view/2816-BE67-5B69-0FEC'''

    #HELP
    help_cmd='help'
    help_desc='Provides the list of the commands'
    help_msg=f'''To show the complete list of commands use /{help_cmd}!
/'''+restart_cmd+': '+restart_desc+'''
/'''+status_cmd+': '+status_desc+'''
/'''+compare_cmd+': '+compare_msg_helper+'''
'''+mod_msg_helper+'''
'''+setting_msg_helper+'''
'''+stats_msg_helper+'''
'''+rename_msg_helper+'''
'''+register_msg_helper

    #COMPLETE HELP
    complete_help_msg=f'''/{id_cmd}: Shows the telegram ID of this chat
/{start_cmd}: {start_desc}
/{force_cmd}: {force_desc}
/'''+restart_cmd+': '+restart_desc+'''
/'''+status_cmd+': '+status_desc+'''
/'''+compare_cmd+': '+compare_msg_helper+'''
'''+log_msg_helper+'''
'''+mod_msg_helper+'''
        /mod move <position> <position>
'''+setting_msg_helper+'''
'''+stats_msg_helper+'''
'''+rename_msg_helper+'''
'''+backup_msg_helper+'''
'''+register_msg_helper

    ### OTHER MESSAGES

    strip_modid_from_url_failed = "Getting modID from steam URL failed. Try using legacy syntax."
    not_a_workshop_url = "The URL you provided has not been recognized as a valid workshop URL. Try the legacy syntax maybe?"
    already_installed_msg = "The mod you want to install is already installed."
    msg_mod_not_installed = "The mod you want to uninstall is not installed"
    msg_modid_invalid = "The mod ID entered are being considered invalid."
    msg_no_mods_installed = "There are no mods installed."
    msg_unhandled_exception = "Unhandled exception, check logs, call the police or contact the administrator."
    msg_workshopid_from_file_failed = "Getting the workshop ID from the config file failed. Check logs."
    msg_only_master = "Only my master can use this. You have no power here."
    msg_force_cmd_incorrect_syntax = "You are not my master, I can tell."
    msg_change_implemented = "This change has been implemented."
    msg_change_rejected = "This change has been rejected."

### INITIALIZE BOT COMMANDS

if __name__ == '__main__':
    try:
        commands = init_commands()
        if commands:
            bot.set_my_commands(commands)
    except Exception as e:
        logger(e, "ERROR")
 
### COMMANDS - RESTART DOUBLE CHECK - no database, just memory

global_restart_requests = []

def save_restart(restart_cmd, user):
    try:
        global global_restart_requests
        for each in global_restart_requests:
            if each[1] == user:
                each[0] = restart_cmd
                return
        global_restart_requests.append((restart_cmd, user))        
    except Exception as e:
        logger(e, "ERROR")

def check_restart(restart_cmd, user):
    try:
        global global_restart_requests
        for each in global_restart_requests:
            if each[0] == restart_cmd and each[1] == user:
                return True
        return False
    except Exception as e:
        logger(e, "ERROR")

def clear_restart(user):
    try:
        global global_restart_requests
        temp = global_restart_requests
        for each in global_restart_requests:
            if each[1] == user:
                temp.remove(each)
                removed = True
        global_restart_requests = temp
        if removed:
            return True
        else:
            return False
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### GAME RUNTIME LOG PARSING MANAGER
########################################################################################################################

### PARSING FLAGS & CONSTANTS

if __name__ == '__main__':
    open_sessions = []
    
    command_flag = True
    join_flag = True
    left_flag = True
    mod_fail_flag = True

    log_key_client_re_pattern = r'ip=([\d.]+)\s.*?steam-id=(\d+)\s.*?(?:access=(\w+)\s)?username="([^"]+)"'
    mod_fail_re_pattern = r'required mod "(.*?)" not found'

    log_key_start = '*** SERVER STARTED ****'
    log_key_stop = 'command entered via server console (System.in): "quit"'
    log_key_client_init = ['[receive-packet] "client-connect"','steam-id','username']
    log_key_client_connecting = ['[receive-packet] "login-queue-request"','steam-id','username']
    log_key_client_connected = ['[receive-packet] "login-queue-done"','steam-id','username']
    log_key_player_connected = ['receive-packet] "player-connect"','steam-id','username']
    log_key_player_in_game = ['[fully-connected]','steam-id','username']
    log_key_client_logout = ['[disconnect]','steam-id','username']
    log_key_cmd = 'command entered'
    log_key_death = 'replacing dead player'
    log_key_mod_fail = ['ZomboidFileSystem.loadModAndRequired','not found']

########################################
### MFA RELATED
########################################

def mfa_naming_convention(telegram_id):
    return f"MFA{str(telegram_id)}"

def multi_fucker_autentication(steam_id, username, login):
    try:
        mfa = get_mfa_registrants()
        if mfa:
            for mfa_steam_id, mfa_telegram_id, message, confirmed in mfa:
                if username == mfa_naming_convention(mfa_telegram_id) and steam_id == mfa_steam_id:
                    if not confirmed:
                        mfa.append(username)
                        confirm_mfa_registration(steam_id, username, mfa_telegram_id)
                        msg = f"Your game account has been successfully linked with telegram. The account \"{username}\" will be deleted on next reboot."
                        reply_to(message, msg)
                    return True             
        return False
    except Exception as e:
        logger(e, "ERROR")

########################################
### LOGIN/LOGOUT FUNCTIONS
########################################

def player_client_login_event(steam_id, username, ip, accesslevel='user'):
    try:
        global open_sessions
        if not multi_fucker_autentication(steam_id, username, 1):
            sync_with_server_whitelist()
            session = Session()
            session.steam_id = steam_id
            session.id = session_open(steam_id, ip)
            open_sessions.append(session)
            return True
    except Exception as e:
        logger(e, "ERROR")
        
def player_client_logout_event(steam_id, username, ip, accesslevel='user'):
    try:
        global open_sessions
        if not multi_fucker_autentication(steam_id, username, 0):
            sync_with_server_whitelist()
            if open_sessions:
                for session in open_sessions:
                    if session.steam_id == steam_id:
                        session_close(session.id)
                        open_sessions.pop(open_sessions.index(session))
            else:
                logger("No open sessions, yet a player logged out.", "WARNING")
            return True
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### GAME SERVER MANAGER + PARSING FUNCTION
########################################################################################################################

class GameServerManager:
    import threading
    def __init__(self, server_name, server_log_path):
        self.server_name = server_name
        self.server_log_path = server_log_path
        self.server_failed_to_start = threading.Event()
        self.server_start_executed = threading.Event()
        self.server_stop_executed = threading.Event()
        self.server_starting = threading.Event()
        self.server_stopping = threading.Event()
        self.server_started = threading.Event()
        self.server_stopped = threading.Event()
        #self.backup_started = threading.Event()
        #self.backup_stopped = threading.Event()
    
    def alert_bot(self, keyword, line):
        try:
            #print(keyword)
            #print(line)
            import re
            if keyword == log_key_start:
                self.server_started.set()
                msg = f"{self.server_name.capitalize()} is up and ready."
                server_chat_message(msg)
            elif keyword == log_key_stop:
                self.server_stopping.set()
                msg = f"{self.server_name.capitalize()} is shutting down..."
                server_chat_message(msg)
            elif mod_fail_flag and keyword == log_key_mod_fail:
                match = re.search(mod_fail_re_pattern, line)
                msg = f"Mod \"{match.group(1)}\" failed to load while starting the server"
                logger(msg, "ERROR", nt=False)
                server_chat_message(msg)
            elif command_flag and keyword == log_key_cmd:
                if '"quit"' not in line and '"save"' not in line:
                    index = line.find('command entered')
                    msg = line[index:].capitalize()
                    logger(msg, "INFO")
                    cheat_alert(msg)
            elif join_flag and keyword == log_key_client_init:
                match = re.search(log_key_client_re_pattern, line)
                if match:
                    ip = match.group(1)
                    steam_id = int(match.group(2))
                    accesslevel = match.group(3)
                    username = match.group(4)
                    if player_client_login_event(steam_id, username, ip):
                        msg = f"A player connected to the server: {username}"
                        logger(msg, "INFO")
                        server_chat_message(msg)
            elif left_flag and keyword == log_key_client_logout:
                match = re.search(log_key_client_re_pattern, line)
                if match:
                    ip = match.group(1)
                    steam_id = int(match.group(2))
                    accesslevel = match.group(3)
                    username = match.group(4)
                    if player_client_logout_event(steam_id, username, ip):
                        msg = f"A player disconnected from the server: {username}"
                        logger(msg, "INFO")
                        server_chat_message(msg)
        except Exception as e:
            logger(e, "ERROR")

    def monitor_log(self):
        try:
            import subprocess
            keywords=[log_key_start, log_key_stop, log_key_client_init, log_key_client_logout, log_key_cmd, log_key_mod_fail]
            tail_process = subprocess.Popen(['tail', '-f', self.server_log_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in tail_process.stdout: # Process each line as it is received
                for keyword in keywords:
                    if isinstance(keyword, str):
                        if keyword in line:
                            self.alert_bot(keyword, line)
                    elif isinstance(keyword, list):
                        if all(key_fragment in line for key_fragment in keyword):
                            self.alert_bot(keyword, line)
        except Exception as e:
            logger(e, "ERROR")

    def execute_for_every_until_true(self, try_for, every, function, *args, **kwargs):
        import time
        start_time = time.time()
        end_time = start_time + try_for
        while time.time() < end_time:
            if function(*args, **kwargs):
                return True
            time.sleep(every)
        return False

    def start_cmd(self):
        try:
            game_bin_path = os.path.join(SERVICE_FOLDER, "start-server.sh")
            game_start_cmd = f"{game_bin_path} -servername {self.server_name} | tee {self.server_log_path}"
            game_server_tmux_session_start = f"tmux new-session -d -s {self.server_name} \"{game_start_cmd}\""
            run_command(f"> {self.server_log_path}")
            logger(f"Log file {self.server_log_path} cleaned before executing the server.", "DEBUG")
            r = run_command(game_server_tmux_session_start)
            if r[0]:
                self.server_start_executed.set()
                timeout = 10
                if self.execute_for_every_until_true(timeout,1,self.tmux_session_state,True):
                    self.server_starting.set()
                    return True
                else:
                    logger(f"Tmux session \"{self.server_name}\" did not come up since {str(timeout)} seconds from the execution.", "ERROR", nt=False)
                    return False
        except Exception as e:
            logger(e, "ERROR")
                
    def stop_cmd(self):
        try:
            save_cmd = run_command_on_gameserver(self.server_name, 'save')
            logger(f"The launch of the save_cmd exited with code: {str(save_cmd[0])}", "DEBUG")
            if save_cmd[0]:
                quit_cmd = run_command_on_gameserver(self.server_name, 'quit')
                logger(f"The launch of the save_cmd exited with code: {str(save_cmd[0])}", "DEBUG")
                if quit_cmd[0]:
                    self.server_stop_executed.set()
                    timeout = 60
                    if self.execute_for_every_until_true(timeout,2,self.tmux_session_state,False):
                        self.server_stopped.set()
                    return True
                return True
        except Exception as e:
            logger(e, "ERROR")
 
    def tmux_session_state(self, state=True):
        try:
            r = run_command(f"tmux list-sessions | grep {self.server_name}")
            if r[0]:
                logger(f"Lookup results for tmux session "+r[1].strip(), "DEBUG")
            if state:
                if r[0]:
                    return True
                else:
                    return False
            else:
                if not r[0]:
                    return True
                else:
                    return False
        except Exception as e:
            logger(e, "ERROR")
            return None

    def start(self):
        try:
            def init_start():
                if not self.start_cmd():
                    logger(f"Failed to start the server \"{self.server_name}\".", "ERROR", nt=False)
                    return
            threading.Thread(target=init_start).start()
            self.server_start_executed.wait()
            logger(f"Started game server \"{self.server_name}\".", "DEBUG")
            self.server_starting.wait()
            logger(f"Started tmux session \"{self.server_name}\".", "DEBUG")
            threading.Thread(target=self.monitor_log).start()
            logger(f"Log monitor started to parse \"{self.server_log_path}\"", "DEBUG")
            self.server_started.wait()
            logger(f"Game Server \"{self.server_name}\" successfully started.", "INFO")
            reload_settings()
            logger(f"Settings have been reloaded for \"{self.server_name}\"", "DEBUG")
        except Exception as e:
            logger(e, "ERROR")

    def stop(self):
        try:
            threading.Thread(target=self.stop_cmd).start()
            self.server_stop_executed.wait()
            logger(f"Sent a save and quit command to \"{self.server_name}\" successsfully.", "DEBUG")
            self.server_stopping.wait()
            logger(f"Game Server \"{self.server_name}\" initiated a shut down.", "DEBUG")
            self.server_stopped.wait()
            logger(f"Game Server \"{self.server_name}\" has been shut down.", "INFO")
            return True
        except Exception as e:
            logger(e, "ERROR")
            return False

    def restart(self):
        try:
            self.stop()
            run_pending_queries()
            self.start()
        except Exception as e:
            logger(e, "ERROR")

if __name__ == '__main__':
    try:
        if not SYSTEMCTL:
            game_manager = GameServerManager(SERVICE_NAME, SERVICE_LOG)
            def shutdown_signal_handler(sig, frame):
                if sig == signal.SIGTERM:
                    logger(f"System Shutdown has being called. Issuing stop signal to the game server...", "INFO")
                    if game_manager.stop():
                        os.kill(os.getpid(), signal.SIGKILL)
                    else:
                        logger("Server .stop() function failed at shutting down the server.", "ERROR", nt=True)
            signal.signal(signal.SIGTERM, shutdown_signal_handler)
            noserver_flag = '--noserver' in sys.argv
            if not noserver_flag:
                if game_manager.tmux_session_state():
                    logger(f"The game server session \"{SERVICE_NAME}\" is already live. Aborting launch.", "INFO")
                    threading.Thread(target=game_manager.monitor_log).start()
                    logger(f"Log monitor started to parse \"{SERVICE_LOG}\"", "DEBUG")
                else:
                    run_pending_queries()
                    threading.Thread(target=game_manager.start).start()
            else:
                logger(f"The flag --noserver has been used. No game server will be started. Pending queries on hold too.", "WARNING")
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### VANILLA SETTINGS GENERATION
########################################################################################################################

def table_is_not_empty(table_name):
    try:
        import sqlite3
        conn = sqlite3.connect(pztgdb)
        cursor = conn.cursor()
        cursor.execute(f'''SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name+"_settings"}';''')
        row = cursor.fetchone()
        if not row:
            logger("Vanilla table does not exist", "DEBUG")
            return False
        else:
            cursor.execute(f'''SELECT COUNT(*) FROM {table_name+"_settings"};''')
            count = cursor.fetchone()[0]
            if count > 0:
                return True
            else:
                logger("Vanilla table is empty", "DEBUG")
                return False
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
    finally:
        if conn:
            conn.close()

class VanillaServerManager:
    def __init__(self, server_name, log_file):
        self.server_name = server_name
        self.log_file = log_file
        self.started_event = threading.Event()
        self.exit_event = threading.Event()
        self.settings_event = threading.Event()

    def vanilla_monitor_log(self, keywords):
        try:
            import subprocess
            run_command("> " + self.log_file)
            tail_process = subprocess.Popen(['tail', '-f', self.log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)    
            for line in tail_process.stdout:
                for keyword in keywords:
                    if keyword in line:
                        if keyword == log_key_start:
                            self.started_event.set()
                            run_command("tmux send-keys -t " + self.server_name + " \"quit\" C-m")
                        if keyword == log_key_stop:
                            self.exit_event.set()
                            break
        except Exception as e:
            logger(e, "ERROR")

    def start_vanilla_server(self):
        try:
            server_cmd = os.path.join(SERVICE_FOLDER, "start-server.sh") + " -servername " + self.server_name + " | tee " + self.log_file
            tmux_session_cmd = "tmux new-session -d -s " + self.server_name + " \"" + server_cmd + "\""
            run_command(tmux_session_cmd)
        except Exception as e:
            logger(e, "ERROR")

    def stop_vanilla_server(self):
        try:
            monitor_log_thread = threading.Thread(target=self.vanilla_monitor_log, args=([log_key_start,log_key_stop],))
            monitor_log_thread.start()
        except Exception as e:
            logger(e, "ERROR")

    def vanilla_tmux_is_open(self):
        try:
            return run_command(f"tmux list-sessions | grep {self.server_name}")[0]
        except Exception as e:
            logger(e, "ERROR")
            return False

    def regenerate_vanilla_settings(self):
        try:
            import time
            global VANILLA_SETTINGS
            VANILLA_SETTINGS = 425
            rm(VANILLA_SERVERINI_PATH)
            rm(VANILLA_SANDBOXVARS_PATH)
            self.start_vanilla_server()
            self.stop_vanilla_server()
            self.started_event.wait()
            reload_settings(VANILLA_SERVERINI, VANILLA_SANDBOXVARS, table_name=self.server_name)
            set_setting_value('Mods', get_setting('Mods')['value'], table_name=self.server_name)
            set_setting_value('WorkshopItems', get_setting('WorkshopItems')['value'], table_name=self.server_name)
            self.exit_event.wait()
            counter = 0
            while True:
                self.started_event = threading.Event()
                self.exit_event = threading.Event()
                if not self.vanilla_tmux_is_open():
                    self.start_vanilla_server()
                    self.stop_vanilla_server()
                    self.started_event.wait()
                    reload_settings(VANILLA_SERVERINI, VANILLA_SANDBOXVARS, table_name=self.server_name)
                    VANILLA_SETTINGS = True
                    self.settings_event.set()
                    break
                else:
                    time.sleep(1)
                    counter += 1
                    if counter == 60:
                        logger("Vanilla setting generation is taking more than expected. Check the logs and the vanilla tmux session?", "WARNING")
        except Exception as e:
            VANILLA_SETTINGS = 500
            logger(e, "ERROR")

if __name__ == '__main__':
    try:
        if DEBUG_MODE:
            logger(f"Skipping vanilla generation. Setting AUTOUPDATE_VANILLA_SETTINGS_ON_START to 0", "DEBUG")
            AUTOUPDATE_VANILLA_SETTINGS_ON_START = 0
        VANILLA_SETTINGS = table_is_not_empty(VANILLA_SERVER_NAME)
        vanilla_manager = VanillaServerManager(VANILLA_SERVER_NAME, VANILLA_LOG_FILE)
        if AUTOUPDATE_VANILLA_SETTINGS_ON_START == 1:
            threading.Thread(target=vanilla_manager.regenerate_vanilla_settings).start()
        elif AUTOUPDATE_VANILLA_SETTINGS_ON_START == 2:
            if VANILLA_SETTINGS is not True or get_setting('Mods')['value'] != get_setting('Mods', table_name=VANILLA_SERVER_NAME)['value']:
                threading.Thread(target=vanilla_manager.regenerate_vanilla_settings).start()
        elif AUTOUPDATE_VANILLA_SETTINGS_ON_START == 0:
            VANILLA_SETTINGS = reload_settings(VANILLA_SERVERINI, VANILLA_SANDBOXVARS, table_name=VANILLA_SERVER_NAME)
            if not VANILLA_SETTINGS:
                VANILLA_SETTINGS = 404
        else:
            VANILLA_SETTINGS = 500
            logger("Unsupported value for AUTOUPDATE_VANILLA_SETTINGS_ON_START. Please use 0, 1, or 2.", "ERROR", nt=False)
    except Exception as e:
        VANILLA_SETTINGS = 500
        logger(e, "ERROR")

########################################################################################################################
### POLLING MANAGER & MONITOR
########################################################################################################################

def create_poll(chat_id, description, options, anonymous=False, multiple_answers=False):
    try:
        poll = bot.send_poll(chat_id, question=description, options=options, is_anonymous=anonymous, allows_multiple_answers=multiple_answers)
        return poll
    except Exception as e:
        logger(e, "ERROR")

def stop_poll(reform=None, poll_id=None):
    try:
        if not reform:
            reform = get_reform_by_poll_id(poll_id)
        reform.poll_stop_date = unix_timestamp()
        save_reform(reform)
        return bot.stop_poll(reform.reform_chat_id, reform.poll_message_id)
    except Exception as e:
        logger(e, "ERROR")

def deny_change(reform=None, poll_id=None, reason=""):
    try:
        if not reform:
            reform = get_reform_by_poll_id(poll_id)
        reform.reform_is_active = 0
        reform.reform_implemented = 0
        save_reform(reform)
        #reform.print_all()
        reply_to(fake_message(reform.reform_chat_id, reform.poll_message_id), f"{msg_change_rejected} {reason}")
    except Exception as e:
        logger(e, "ERROR")

def implement_change(reform=None, poll_id=None, reason=""):
    try:
        if not reform:
            reform = get_reform_by_poll_id(poll_id)
        if reform.change_ctype == 'mod':
            if reform.change_mod_action == 'install':
                install_mod(reform.change_mod_modid, reform.change_mod_workshopid)
            elif reform.change_mod_action == 'uninstall':
                uninstall_mod(reform.change_mod_modid, reform.change_mod_workshopid)
            logger(f"Type: {reform.change_ctype} Action: {reform.change_mod_action} ModID: {reform.change_mod_modid} WorkshopID: {reform.change_mod_workshopid} Date: {log_timestamp}", "INFO")
        elif reform.change_ctype == 'setting':
            logger(f"Type: {reform.change_ctype} Variable: {reform.change_setting_variable} Old Value: {reform.change_setting_old_value} Current Value: {get_setting(reform.change_setting_variable)['value']} New Value: {reform.change_setting_new_value} Date: {log_timestamp}", "INFO")
            set_setting_value(reform.change_setting_variable, reform.change_setting_new_value)
        reform.reform_is_active = 0
        reform.reform_implemented = 1
        save_reform(reform)
        #reform.print_all()
        reply_to(fake_message(reform.reform_chat_id, reform.poll_message_id), f"{msg_change_implemented} {reason}")
    except Exception as e:
        logger(e, "ERROR")

def consensus(reform, poll_id=None, votes_from = 'db', consensus=False, virdict=None, expedite_approval_process=False):
    try:
        if votes_from == 'db':
            if not reform:
                reform = get_reform_by_poll_id(poll_id)
        max_voters = bot.get_chat_members_count(reform.reform_chat_id) - BOTS_PRESENT_IN_THE_GROUP_CHAT # At least one bot (this one) is in the count, so we detract one.
        if reform.poll_options == 2:
            relative_majority = max_voters // 2 + 1 # Majority threshold (for testing remove the +1 and be alone in a group with just the bot)
            if votes_from == 'db':
                    if reform.poll_yes_list:
                        yes_votes = len(reform.poll_yes_list.split(','))
                    else:
                        yes_votes = 0
                    if reform.poll_no_list:
                        no_votes = len(reform.poll_no_list.split(','))
                    else:
                        no_votes = 0
                    if expedite_approval_process:
                        votes = yes_votes + no_votes
                        if votes >= QUORUM * max_voters:
                            if yes_votes >= votes * UNANIMITY_COEFFICIENT:
                                consensus, virdict, reason = (True, True, f"Quorum of {QUORUM*100}% has been reached within {MINIMUM_DAYS} days and unaminity parameter of {UNANIMITY_COEFFICIENT*100}% has been met.")
                                reform.poll_consensus_coefficient = yes_votes / max_voters
                            elif no_votes >= votes * UNANIMITY_COEFFICIENT:
                                consensus, virdict, reason = (True, False, f"Quorum of {QUORUM*100}% has been reached within {MINIMUM_DAYS} days and unaminity parameter of {UNANIMITY_COEFFICIENT*100}% has been met.")
                                reform.poll_consensus_coefficient = no_votes / max_voters
                    else:
                        if yes_votes >= relative_majority:
                            consensus, virdict, reason = (True, True, f"The majority of the users ({yes_votes} out of {max_voters}) has expressed its will within {POLL_EXPIRE_AFTER} days from the submission of the poll.")
                            reform.poll_consensus_coefficient = yes_votes / max_voters
                        elif no_votes >= relative_majority:
                            consensus, virdict, reason = (True, False, f"The majority of the users ({yes_votes} out of {max_voters}) has expressed its will within {POLL_EXPIRE_AFTER} days from the submission of the poll.")
                            reform.poll_consensus_coefficient = no_votes / max_voters
            elif votes_from == 'tg':
                pass # Alternative that I probably won't implement since the current solution works well.
        if consensus:
            if virdict:
                implement_change(reform, reason)
            else:
                deny_change(reform, reason)
            stop_poll(reform)
            return (consensus, virdict)
        else:
            return (consensus, virdict)
        save_reform(reform)
    except Exception as e:
        logger(e, "ERROR")

def update_poll_vote(voter, poll_id, votes):
    try:
        reform = get_reform_by_poll_id(poll_id)
        if reform.poll_options == 2:
            yes_option_n = 0
            no_option_n = 1
            voter = str(voter)
            is_yes_list = False
            is_no_list = False
            if len(votes) > 0:
                if votes[0] == yes_option_n:
                    is_yes_list = True
                    if reform.poll_yes_list == "":
                        reform.poll_yes_list = voter
                    else:
                        yes_array = reform.poll_yes_list.split(',')
                        yes_array.append(voter)
                        reform.poll_yes_list = ','.join(map(str, ensure_max_occurrences(yes_array, voter, 1)))
                elif votes[0] == no_option_n:
                    is_no_list = True
                    if reform.poll_no_list == "":
                        reform.poll_no_list = voter
                    else:
                        no_array = reform.poll_no_list.split(',')
                        no_array.append(voter)
                        reform.poll_no_list = ','.join(map(str, ensure_max_occurrences(no_array, voter, 1)))
            else: # retract_vote_option
                if reform.poll_yes_list:
                    vote_list = reform.poll_yes_list.split(',')
                    reform.poll_yes_list = ','.join(map(str, ensure_max_occurrences(vote_list, voter, 0)))
                if reform.poll_no_list:
                    vote_list = reform.poll_no_list.split(',')
                    reform.poll_no_list = ','.join(map(str, ensure_max_occurrences(vote_list, voter, 0)))
            #print("--------------------------------------------------------------")
            #reform.print_all()
            #print("--------------------------------------------------------------")
            save_reform(reform)
            consensus(reform)
    except Exception as e:
        logger(e, "ERROR")

def active_clone_changes(ctype, change):
    try:
        if ctype == 'mod':
            action, modid, workshopid = change
            return get_mod_clone_change(modid, workshopid, action)
        elif ctype == 'setting':
            variable, value = change
            return get_setting_clone_change(variable, value)
    except Exception as e:
        logger(e, "ERROR")

def mod_poll_launch(new_reform, workshop_url):
    try:
        poll = create_poll(new_reform.reform_chat_id, new_reform.reform_name, ['Yes','No'])
        reply_to(poll, workshop_url)
        return poll
    except Exception as e:
        logger(e, "ERROR")

def mod_poll_img(new_reform, workshop_url):
    try:
        get_steam_image_url = strip_img_url_from_steam(workshop_url)
        if get_steam_image_url:
            bot.send_photo(new_reform.reform_chat_id, get_steam_image_url)
            return True
        else:
            return False
    except Exception as e:
        logger(e, "ERROR")

def setting_poll_launch(new_reform):
    try:
        return create_poll(new_reform.reform_chat_id, new_reform.reform_description, ['Yes','No'])
    except Exception as e:
        logger(e, "ERROR")

def create_reform(message, ctype, change):
    try:
        clone = active_clone_changes(ctype, change)
        if not clone:
            import os
            new_reform = Reform()
            new_reform.reform_id = message.id
            new_reform.reform_chat_id = message.chat.id
            new_reform.reform_date = unix_timestamp()
            new_reform.reform_implemented = 0
            new_reform.reform_is_active = 1
            new_reform.proposer_first_name = message.from_user.first_name
            new_reform.proposer_last_name = message.from_user.last_name
            new_reform.proposer_username = message.from_user.username
            new_reform.proposer_id = message.from_user.id
            new_reform.change_ctype = ctype
            if ctype == 'mod':
                action, modid, workshopid = change
                workshop_url = f"https://steamcommunity.com/sharedfiles/filedetails/?id={workshopid}"
                new_reform.change_mod_action = action
                new_reform.change_mod_modid = modid
                new_reform.change_mod_workshopid = workshopid
                new_reform.reform_name = f"{action.capitalize()} {modid}"
                new_reform.reform_description = f"Do you want to {action} <b>{modid}</b>?"
                poll = mod_poll_launch(new_reform, workshop_url)
                poll_img = mod_poll_img(new_reform, workshop_url)
            elif ctype == 'setting':
                variable, value = change
                new_reform.change_setting_variable = variable
                new_reform.change_setting_old_value = get_setting(variable)['value']
                new_reform.change_setting_new_value = value
                new_reform.reform_name = f"{variable} {value}"
                new_reform.reform_description = f"Do you want to set {variable} = {value}?"
                poll = setting_poll_launch(new_reform)
            new_reform.poll_id = poll.poll.id
            new_reform.poll_message_id = poll.message_id
            new_reform.poll_options = len(poll.poll.options)
            #new_reform.print_all()
            save_reform(new_reform)
        else:
            if message.chat.id != clone.reform_chat_id:
                bot.forward_message(chat_id=message.chat.id, from_chat_id=clone.reform_chat_id, message_id=clone.poll_message_id)
                reply_to(message, "This change has been already proposed in another chat and is under trial process.")
            else:
                reply_to(fake_message(clone.reform_chat_id, clone.poll_message_id), "This change has been already proposed and is under trial process.")
    except Exception as e:
        logger(e, "ERROR")

def poll_expiration_manager():
    try:
        import time
        day = 86400
        expiration = day*POLL_EXPIRE_AFTER
        while True:
            active_reforms = get_active_reforms()
            if active_reforms:
                for reform in active_reforms:
                    if MISOABSTINENTIA:
                        if reform.reform_date + day*MINIMUM_DAYS < unix_timestamp():
                            consensus(reform, expedite_approval_process=True)
                    if reform.reform_date + expiration < unix_timestamp():
                        deny_change(reform, reason=f"{POLL_EXPIRE_AFTER} days passed since its proposal.")
                        stop_poll(reform)
            time.sleep(3600)
    except Exception as e:
        logger(e, "ERROR")

if __name__ == '__main__':
    threading.Thread(target=poll_expiration_manager).start()


########################################################################################################################
### BACKUPS MANAGERS
########################################################################################################################

def map_files(min_x, min_y, max_x, max_y):
    try:
        last = False
        filenames = []
        for i in range(int(str(min_x[:-1])), int(str(max_x[:-1])) + 1):
            for j in range(int(str(min_y[:-1])), int(str(max_y[:-1])) + 1):
                chunk_name = f"map_{str(i)[:-1]}_{str(j)[:-1]}.bin"
                if last:
                    if last != chunk_name:
                        filenames.append(os.path.join(GAME_FILES_FOLDER, chunk_name))
                else:
                    filenames.append(os.path.join(GAME_FILES_FOLDER, chunk_name))
                last = chunk_name
        logger(f"Filenames requested for backup:\n{filenames}", "DEBUG")
        return filenames
    except Exception as e:
        logger(e, "ERROR")

def get_backup_list():
    try:
        backup_list = []
        for backup in os.listdir(BACKUP_FOLDER):
            backup_list.append(backup.split('_'))
        return backup_list
    except Exception as e:
        logger(e, "ERROR")

def get_most_recent_backup(backup_path):
    try:
        from datetime import datetime
        def last(date1, date2):
            date1 = datetime.strptime(date1, "%Y-%m-%d_%H.%M.%S")
            date2 = datetime.strptime(date2, "%Y-%m-%d_%H.%M.%S")
            return date1.strftime("%Y-%m-%d_%H.%M.%S") if date1 > date2 else date2.strftime("%Y-%m-%d_%H.%M.%S")
        backup_list = get_backup_list()
        most_recent = None
        for folder in backup_list:
            if len(folder) == 3:
                for bname, bdate, btime in backup_list:
                    if bname == backup_name:
                        if most_recent:
                            most_recent = last(bdate+'_'+btime, most_recent)
                        else:
                            most_recent = bdate+'_'+btime
            else:
                logger(f"Invalid backup folder name: {folder}", "DEBUG")
        return os.path.join(BACKUP_FOLDER, f"{backup_name}_{most_recent}")
    except Exception as e:
        logger(e, "ERROR")

def create_backup_folder(backup_name):
    try:
        backup_path = os.path.join(BACKUP_FOLDER, backup_name+'_'+backup_timestamp())
        r = run_command(f"mkdir -p {backup_path}")
        if r[0]:
            return backup_path
        else:
            logger(f"Error during creation of the backup folder ({backup_path}).", "DEBUG")
            return False
    except Exception as e:
        logger(e, "ERROR")

def backup_exists(backup_path):
    try:
        backup_list = get_backup_list()
        for btype, bname, bdate, btime in backup_list:
            if bname == backup_name:
                world = players = vehicles = items = settings = False
                for folder in os.listdir(os.path.join(BACKUP_FOLDER, f"{bname}_{bdate}_{btime}")):
                    if folder == 'map':
                        world = True
                    elif folder == 'players':
                        players = True
                    elif folder == 'vehicles':
                        vehicles = True
                    elif folder == 'items':
                        items = True
                    elif folder == 'settings':
                        settings = True
                return [world, players, vehicles, items, settings]
            else:
                return False
    except Exception as e:
        logger(e, "ERROR")

def db_filter_backupped_vehicles(vehicles_db, min_x, min_y, max_x, max_y):
    try:
        import sqlite3
        conn = sqlite3.connect(vehicles_db)
        cursor = conn.cursor()
        # Delete vehicles outside the area
        cursor.execute(f'''DELETE FROM vehicles WHERE x < {min_x} OR x > {max_x} OR y < {min_y} OR y > {max_y};''')
        cursor.execute(f'''SELECT wx, wy FROM vehicles WHERE x > {min_x} AND x < {max_x} AND y > {min_y} AND y < {max_y};''')
        for wx, wy in cursor.fetchall():
            print(f"Found vehicle to save in {wx}, {wy}")
        # Reorder the id column
        cursor.execute(f'''UPDATE vehicles SET id = (SELECT COUNT(*) FROM vehicles AS v WHERE v.id < vehicles.id) + 1;''')
        conn.commit()
        return True
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
        return False
    finally:
        if conn:
            conn.close()

def backup_save_map(backup_path, world):
    try:
        x1, y1, x2, y2 = world
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if not all(0 <= coord <= 20000 for coord in [x1, y1, x2, y2]):
            logger(f"Vanilla map coordinates are not between 0 and 20000: {str(x1)} {str(y1)} {str(x2)} {str(y2)}", "WARNING")
        else:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            file_paths = map_files(min_x, min_y, max_x, max_y)
            not_found = [path for path in file_paths if not os.path.exists(path)]
            if not not_found:
                logger(f"All files exist. Proceeding...", "DEBUG")
                r = run_command(f"mkdir -p {backup_path}")
                if r[0]:
                    error = False
                    for path in file_paths:
                        r = run_command(f"cp {path} {backup_path}")
                        if not r[0]:
                            error = True
                            logger(f"Error during the copy of {path} to {backup_path}", "DEBUG")
                    if not error:
                        logger(f"Map backup completed successfully.", "DEBUG")
                        return True
                    else:
                        return False
            else:
                logger(f"Files not found: {not_found}", "DEBUG")
                return False
    except Exception as e:
        logger(e, "ERROR")

def backup_save_items(backup_path):
    try:
        if os.path.exists(os.path.join(GAME_FILES_FOLDER, 'WorldDictionary.bin')):
            r = run_command(f"mkdir -p {backup_path}")
            if r[0]:
                r = run_command(f"cp {os.path.join(GAME_FILES_FOLDER, 'WorldDictionary.bin')} {backup_path}")
                if not r[0]:
                    logger(f"Error during the copy of WorldDictionary.bin to {backup_path}", "DEBUG")
                else:
                    logger(f"WorldDictionary backup completed successfully.", "DEBUG")
                    return True
            else:
                logger(f"Error during the creation of the backup folder.", "DEBUG")
        else:
            logger(f"WorldDictionary.bin does not exist in the game folder.", "DEBUG")
    except Exception as e:
        logger(e, "ERROR")

def backup_save_vehicles(backup_path, selective=False, area=None):
    try:
        if os.path.exists(os.path.join(GAME_FILES_FOLDER, 'vehicles.db')):
            r = run_command(f"mkdir -p {backup_path}")
            if r[0]:
                r = run_command(f"cp {os.path.join(GAME_FILES_FOLDER, 'vehicles.db')} {backup_path}")
                if not r[0]:
                    logger(f"Error during the copy of vehicles.db to {backup_path}", "DEBUG")
                else:
                    logger(f"Vehicles backup completed successfully.", "DEBUG")
                    if selective:
                        min_x, min_y, max_x, max_y = area
                        min_x, min_y, max_x, max_y = int(min_x), int(min_y), int(max_x), int(max_y)
                        if db_filter_backupped_vehicles(os.path.join(backup_path, 'vehicles.db'), min_x, min_y, max_x, max_y):
                            logger(f"Vehicles outside area has been filtered out.", "DEBUG")
                            return True
                        else:
                            return False
                    return True
            else:
                logger(f"Error during the creation of the backup folder.", "DEBUG")
        else:
            logger(f"vehicles.db does not exist in the game folder.", "DEBUG")
    except Exception as e:
        logger(e, "ERROR")

def backup_save_players(backup_path):
    try:
        if os.path.exists(os.path.join(GAME_PLAYER_DB)):
            players_db = True
        if os.path.exists(os.path.join(GAME_SERVER_DB)):
            whitelist = True
        if players_db or whitelist:
            r = run_command(f"mkdir -p {backup_path}")
            if r[0]:
                error = False
                if players_db:
                    r1 = run_command(f"cp {GAME_PLAYER_DB} {backup_path}")
                    if not r1[0]:
                        error = True
                        logger(f"Error during the copy of {GAME_PLAYER_DB} to {backup_path}", "DEBUG")
                if whitelist:
                    r2 = run_command(f"cp {GAME_SERVER_DB} {backup_path}")
                    if not r2[0]:
                        error = True  
                        logger(f"Error during the copy of the whitelist from {GAME_SERVER_DB} to {backup_path}", "DEBUG")
                if not error:
                    logger(f"Players backup completed successfully.", "DEBUG")
                    return True
            else:
                logger(f"Error during the creation of the backup folder.", "DEBUG")
        else:
            logger(f"Aborting backup. players.db and whitelist.dat do not exist in the game folder.", "DEBUG")
    except Exception as e:
        logger(e, "ERROR")

def backup_save_setting(backup_path):
    try:
        error = False
        r = run_command(f"mkdir -p {backup_path}")
        if not r[0]:
            logger(f"Error during creation of the backup folder ({backup_path}). Aborting backup...", "DEBUG")
            error = True
        else:
            r = run_command(f"cp {SERVERINI_PATH} {backup_path}")
            if not r[0]:
                error = True
                logger(f"Error during the copy of {SERVERINI_PATH} to {backup_path}", "DEBUG")
            r = run_command(f"cp {SANDBOXVARS_PATH} {backup_path}")
            if not r[0]:
                error = True
                logger(f"Error during the copy of {SANDBOXVARS_PATH} to {backup_path}", "DEBUG")
        if not error:
            logger(f"Settings backup {backup_path} completed successfully.", "DEBUG")
            return True
    except Exception as e:
        logger(e, "ERROR")

def backup_save(message, backup_name, world, players, items, vehicles, settings):
    try:
        failed = []
        backup_path = create_backup_folder(backup_name)
        if backup_path:
            if world:
                if not backup_save_map(os.path.join(backup_path, 'world'), world):
                    failed.append("world")
            if players:
                if not backup_save_players(os.path.join(backup_path, 'players')):
                    failed.append("players")
            if items:
                if not backup_save_items(os.path.join(backup_path, 'items')):
                    failed.append("items")
            if vehicles:
                if world:
                    if not backup_save_vehicles(os.path.join(backup_path, 'vehicles'), selective=True, area=world):
                        failed.append("vehicles")
                elif backup_save_vehicles(os.path.join(backup_path, 'vehicles')):
                    failed.append("vehicles")
            if settings:
                if not backup_save_setting(os.path.join(backup_path, 'settings')):
                    failed.append("settings")
            if failed:
                logger(f"Backup failed for: {', '.join(failed)}", "ERROR", nt=False)
                reply_to(message, f"Backup failed for: {', '.join(failed)}")
            else:
                logger(f"Backup {backup_name} completed successfully.", "INFO")
                reply_to(message, f"Backup {backup_name} completed successfully.")
        else:
            reply_to(message, f"Backup failed. Error during the creation of the backup folder.")
    except Exception as e:
        logger(e, "ERROR")

def db_restore_vehicles_in_area(vehicles_db):
    try:
        import sqlite3
        conn = sqlite3.connect(GAME_VEHICLES_DB)
        c = conn.cursor()
        # Take the world version from the zomboid db from any row
        c.execute('''SELECT worldversion FROM vehicles LIMIT 1;''')
        worldversion = c.fetchone()
        if worldversion:
            worldversion = worldversion[0]
        else:
            logger("Worldversion not found in the Zomboid vehicles.db. Please make sure you have seen at least one vehicle in the new map and saved.", "DEBUG")
            conn.close()
            return False
        c.execute('''ATTACH DATABASE ? AS backup''', (vehicles_db,))
        # Merge data from backup into the main database
        conn.execute('''
            INSERT INTO vehicles (wx, wy, x, y, worldversion, data)
            SELECT wx, wy, x, y, ?, data
            FROM backup.vehicles;
        ''', (worldversion,))
        c.execute('''SELECT wx, wy FROM backup.vehicles''')
        vehicles = c.fetchall()
        for wx, wy in vehicles:
            logger(f"Vehicle in {wx}, {wy} inserted into {GAME_VEHICLES_DB}", "DEBUG")
        conn.commit()
        conn.close()
        logger(f"Vehicles restored from {vehicles_db} to {GAME_VEHICLES_DB}", "INFO")
        return True
    except sqlite3.Error as e:
        logger(e, "SQL_ERROR")
        return False
    except Exception as e:
        logger(e, "ERROR")
        return False

def backup_restore_map(backup_path):
    try:
        if os.path.exists(backup_path):
            r = run_command(f"cp {os.path.join(backup_path, 'map_*')} {GAME_FILES_FOLDER}")
            if r[0]:
                logger(f"Map restored from {backup_path}", "DEBUG")
                return True
            else:
                logger(f"Error during the restore of the map from {backup_path}", "DEBUG")
                return False
        else:
            logger(f"Backup folder {backup_path} does not exist.", "DEBUG")
            return False
    except Exception as e:
        logger(e, "ERROR")
        return False

def backup_restore_players(backup_path):
    try:
        if os.path.exists(backup_path):
            r = run_command(f"cp {os.path.join(backup_path, 'players.db')} {GAME_PLAYER_DB}")
            if not r[0]:
                logger(f"Error during the restore of players.db from {backup_path}", "DEBUG")
                error = True
            else:
                logger(f"players.db restored from {backup_path}", "DEBUG")
            r = run_command(f"cp {os.path.join(backup_path, {SERVICE_NAME}+'.db')} {GAME_SERVER_DB}")
            if not r[0]:
                logger(f"Error during the restore of {SERVICE_NAME}.db from {backup_path}", "DEBUG")
                error = True
            else:
                logger(f"{SERVICE_NAME}.db restored from {backup_path}", "DEBUG")
            if not error:
                return True
        else:
            logger(f"Backup folder {backup_path} does not exist.", "DEBUG")
            return False
    except Exception as e:
        logger(e, "ERROR")
        return False

def backup_restore_vehicles(backup_path):
    try:
        vehicles_db = os.path.join(backup_path, 'vehicles.db')
        if os.path.exists(vehicles_db):
            if db_restore_vehicles_in_area(vehicles_db):
                logger(f"Vehicles restored from {vehicles_db}", "DEBUG")
                return True
            else:
                logger(f"Error during the restore of vehicles.db from {vehicles_db}", "DEBUG")
                return False
    except Exception as e:
        logger(e, "ERROR")
        return False  

def backup_restore_items(backup_path):
    try:
        if os.path.exists(backup_path):
            r = run_command(f"cp {os.path.join(backup_path, 'WorldDictionary.db')} {GAME_FILES_FOLDER}")
            if not r[0]:
                logger(f"Error during the restore of items.db from {backup_path}", "DEBUG")
            else:
                logger(f"items.db restored from {backup_path}", "DEBUG")
                return True
        else:
            logger(f"Backup folder {backup_path} does not exist.", "DEBUG")
            return False
    except Exception as e:
        logger(e, "ERROR")
        return False

def backup_restore_setting(backup_path):
    try:
        if os.path.exists(backup_path):
            r = run_command(f"cp {os.path.join(backup_path, 'server.ini')} {SERVERINI_PATH}")
            if not r[0]:
                logger(f"Error during the restore of server.ini from {backup_path}", "DEBUG")
            else:
                logger(f"server.ini restored from {backup_path}", "DEBUG")
            r = run_command(f"cp {os.path.join(backup_path, 'sandboxVars.lua')} {SANDBOXVARS_PATH}")
            if not r[0]:
                logger(f"Error during the restore of sandboxVars.lua from {backup_path}", "DEBUG")
            else:
                logger(f"sandboxVars.lua restored from {backup_path}", "DEBUG")
            return True
        else:
            logger(f"Backup folder {backup_path} does not exist.", "DEBUG")
            return False
    except Exception as e:
        logger(e, "ERROR")
        return False

def backup_restore(message, backup_name, world, players, items, vehicles, settings):
    try:
        failed = []
        backup_path = get_most_recent_backup(backup_name)
        if os.path.exists(backup_path):
            if world:
                if not backup_restore_map(os.path.join(backup_path, 'world')):
                    failed.append("world")
            if players:
                if not backup_restore_players(os.path.join(backup_path, 'players')):
                    failed.append("players")
            if items:
                if not backup_restore_items(os.path.join(backup_path, 'items')):
                    failed.append("items")
            if vehicles:
                if not backup_restore_vehicles(os.path.join(backup_path, 'vehicles')):
                    failed.append("vehicles")
            if settings:
                if not backup_restore_setting(os.path.join(backup_path, 'settings')):
                    failed.append("settings")
            if failed:
                logger(f"Restore failed for: {', '.join(failed)}", "ERROR", nt=False)
                reply(message, f"Restore failed for: {', '.join(failed)}")
            else:
                logger(f"Restore {backup_name} completed successfully.", "INFO")
                reply(message, f"Restore {backup_name} completed successfully.")
        else:
            reply(message, f"Restore failed. Backup folder {backup_name} does not exist.")
    except Exception as e:
        logger(e, "ERROR")

########################################################################################################################
### MAIN - COMMAND HANDLERS
########################################################################################################################

if __name__ == '__main__':
    try:
        # SHOW CHAT ID
        @bot.message_handler(commands=[id_cmd])
        def id_command(message):
            print(f"CHAT ID: {message.chat.id}")
            reply_to(message, f"CHAT ID: {message.chat.id}")
        # START
        @bot.message_handler(commands=[start_cmd])
        def start_command(message):
            reply_to(message, start_msg)
        # HELP
        @bot.message_handler(commands=[help_cmd])
        def help_command(message):
            reply_to(message, help_msg, disable_web_page_preview=True)
        # HELP!
        @bot.message_handler(commands=[help_cmd+'!'])
        def help_command(message):
            reply_to(message, complete_help_msg, disable_web_page_preview=True)
        # STATUS
        @bot.message_handler(commands=[status_cmd])
        def status_command(message):
            service_status = check_service_status()
            if service_status:
                status = "active."
            elif not service_status:
                status = "down."
            else:
                status = "???"
            reply_to(message, "The PZserver is currently "+status)
        # SHOW LOG
        @bot.message_handler(commands=[log_cmd])
        def log_command(message):
            command = message.text.split()
            if len(command) == 2:
                text_chunks = split_msg_in_chunks(run_command(f"cat {THIS_LOG_FILE} | grep {command[1]}", log=False))
                for chunk in text_chunks:
                    reply_to(message, chunk, parse_mode='HTML')
            else:
                reply_to(message, log_msg_helper)
        # SHOW DIFF
        @bot.message_handler(commands=[compare_cmd])
        def compare_command(message):
            command = message.text.split()
            if len(command) == 1:
                def send_diff():
                    exclusion_list=['ServerWelcomeMessage','Mods','WorkshopItems','PublicDescription','PublicName','ServerPlayerID','ResetID']
                    text_chunks = compare_settings('main', 'vanilla', as_text=True, exclusion_list=exclusion_list)
                    for chunk in text_chunks:
                        reply_to(message, chunk, parse_mode='HTML')
                    return True
                if VANILLA_SETTINGS is True:
                    send_diff()
                elif VANILLA_SETTINGS == 425:
                    reply_to(message, "Vanilla settings are being generated. Please wait.")
                    def send_diff_when_ready():
                        vanilla_settings_event.wait()
                        send_diff()
                    threading.Thread(target=send_diff_when_ready).start()
                elif VANILLA_SETTINGS == 500:
                    reply_to(message, "A error prevented vanilla settings generation.")
                elif VANILLA_SETTINGS == 404:
                    reply_to(message, "Vanilla settings were not found. Provide the setting file or enable autogeneration.")
            else:
                reply_to(message, compare_msg_helper)
        # STATS
        @bot.message_handler(commands=[stats_cmd])
        def stats_command(message):
            command = message.text.split()
            if len(command) == 1:
                if user_is_registered(message.from_user.id):
                    reply_to(message, get_user_activity_info(message.from_user.id), parse_mode='HTML')
                else:
                    reply_to(message, "You need to register yourself if you want to see your stats.")
                    reply_to(message, register_msg_helper)
            elif len(command) == 2:
                steam_id = valid_steam_id(command[1])
                if steam_id:
                    telegram_id = player_is_registered(steam_id)
                    if telegram_id:
                        reply_to(message, get_user_activity_info(telegram_id), parse_mode='HTML')
                    else:
                        reply_to(message, "This user is not registered yet.")
                else:
                    reply_to(message, f"This is not a valid steam ID.")
            else:
                reply_to(message, stats_msg_helper, disable_web_page_preview=True)
        # REGISTER
        @bot.message_handler(commands=[register_cmd])
        def register_command(message):
            command = message.text.split()
            if len(command) == 2:
                steam_id = valid_steam_id(command[1])
                if steam_id:
                    if get_player(steam_id):
                        reply_to(message, f"Please connect to PZserver with this username: 'MFA{message.from_user.id}' to complete the process.")
                        submit_mfa_registration(steam_id, message.from_user.id, message)
                    else:
                        reply_to(message, f"This steam ID is not associated to any player of the server yet.")
                else:
                    reply_to(message, f"This is not a valid steam ID.")
            else:
                reply_to(message, register_msg_helper, disable_web_page_preview=True)
        # RENAME
            @bot.message_handler(commands=[rename_cmd])
            def rename_command(message):
                def schedule_rename(new, old, steam_id):
                    pending_query_type = 'rename'
                    updated = delete_pending_rename(old, steam_id)
                    add_to_pending_queries(pending_query_type, GAME_SERVER_DB, f"UPDATE whitelist SET username = '{new}' WHERE username = '{old}' AND steamid = {steam_id}", message.chat.id, message.id)
                    add_to_pending_queries(pending_query_type, GAME_PLAYER_DB, f"UPDATE networkPlayers SET username = '{new}' WHERE username = '{old}'", message.chat.id, message.id)
                    add_to_pending_queries(pending_query_type, pztgdb, f"UPDATE players SET username = '{new}' WHERE username = '{old}' AND steam_id = {steam_id}", message.chat.id, message.id)
                    msg = f"Character \"{old}\" will be renamed to \"{new}\" on next reboot unless a new player joins with this username before then."
                    if not updated:
                        reply_to(message, msg)
                    else:
                        reply_to(message, f"{msg} Previous change has been canceled.")
                steam_id = user_is_registered(message.from_user.id)
                if not SYSTEMCTL:
                    if steam_id:
                        import re
                        usernames = re.findall(r'"([^"]+)"', message.text)
                        forbidden_chars = ['/','?','"','$',"'",'.',';',',']
                        if len(usernames) == 2:
                            old  = usernames[0]
                            new = usernames[1]
                            if all(len(username)< 20 for username in usernames):
                                if not any(forbidden in username for username in usernames for forbidden in forbidden_chars):
                                    if new not in get_player_list():
                                        pending = get_pending_rename_data()
                                        if not pending:
                                            schedule_rename(new, old, steam_id)
                                        else:
                                            you_are_a_fucker = you_are_late = its_your_lucky_day = False
                                            for ID, old_username, new_username, steam_id in pending:
                                                if new == new_username and old == old_username:
                                                    you_are_a_fucker = True
                                                elif new == new_username and old != old_username:
                                                    you_are_late = True
                                                else:
                                                    its_your_lucky_day = True
                                            if its_your_lucky_day:
                                                schedule_rename(new, old, steam_id)
                                            elif you_are_a_fucker:
                                                reply_to(message, "This request has been already recorded, but it won't be implemented until next reboot.")
                                            elif you_are_late:
                                                reply_to(message, "Another player already submitted a request for this name change before you.")
                                    else:
                                        reply_to(message, "Character name cannot be the same as one of an existing player.")
                                else:
                                    reply_to(message, "Character names cannot include these characters:\n/ ? \" $ ' . , ;")
                            else:
                                reply_to(message, "The maximum lenght of a username is 20 characters")
                        else:
                            reply_to(message, rename_msg_helper)
                    else:
                        reply_to(message, register_msg_helper)
                else:
                    reply_to(message, "This feature is available only if the server is launched through the integrated solution. Use that instead of systemctl if you want to use it, or implement it differently.")
        # RESTART
        @bot.message_handler(commands=[restart_cmd])
        def restart_command(message):
            if member_is_admin(message):
                if check_service_status():
                    save_restart(restart_cmd, message.from_user.id)
                    reply_to(message, restart_msg)
                else:
                    reply_to(message, "The server is currently down.")
        @bot.message_handler(commands=[restart_confirm_cmd])
        def confirm_restart_command(message, force=False):
            def execute_restart():
                if not SYSTEMCTL:
                    game_manager.restart()
                else:
                    run_command(f"sudo systemctl restart {SERVICE_NAME}")
            if not force:
                restart_required = check_restart(restart_cmd, message.from_user.id)
                if restart_required:
                    clear_restart(message.from_user.id)
                    threading.Thread(target=execute_restart).start()
                    reply_to(message, "The server is restarting...")
            else:
                threading.Thread(target=execute_restart).start()
                reply_to(message, "The server is restarting...")
        @bot.message_handler(commands=[restart_cancel_cmd])
        def cancel_restart_command(message):
            clear_restart(message.from_user.id)
        # MOD INSTALL / UNINSTALL
        @bot.message_handler(commands=[mod_cmd])
        def mod_command(message, force=False):
            def list_mod_cmd():
                modid_list, workshopid_list = get_valid_modid_workshopid_list()
                if not len(modid_list) and not len(workshopid_list):
                    reply_to(message, msg_no_mods_installed)
                elif not len(modid_list) or not len(workshopid_list):
                    reply_to(message, msg_no_mods_installed)
                    logger("Something must be wrong with the mod lists... Please check the config file.", "WARNING")
                elif len(modid_list) == len(workshopid_list):
                    counter = 0
                    msg_body = ""
                    for modid in modid_list:
                        counter += 1
                        workshopid = workshopid_list[modid_list.index(modid)]
                        msg_body += f"{counter}) <a href='https://steamcommunity.com/sharedfiles/filedetails/?id={workshopid}'>{modid}</a> [{workshopid}]\n"
                    reply_to(message, msg_body, disable_web_page_preview=True, parse_mode='HTML')
            def move_mod(from_, to_):
                modid_list, workshopid_list = get_valid_modid_workshopid_list()
                mods_count = len(modid_list)
                if mods_count == len(workshopid_list) and mods_count > 0:
                    if 0 < from_ <= mods_count and 0 < to_ <= mods_count and from_ != to_:
                        modid_list.insert(to_-1, modid_list.pop(from_-1))
                        workshopid_list.insert(to_-1, workshopid_list.pop(from_-1))
                        modid_list_text = ';'.join(map(str, modid_list))
                        workshopid_list_text = ';'.join(map(str, workshopid_list))
                        set_setting_value('Mods', modid_list_text)
                        set_setting_value('WorkshopItems', workshopid_list_text)
                        list_mod_cmd()
                else:
                    reply_to(message, msg_no_mods_installed)
                    logger("Something must be wrong with the mod lists... Please check the config file.", "WARNING")
            def install_uninstall_mod_cmd(action, valid_IDs, source):
                if valid_IDs:
                    modid, workshopid = valid_IDs
                    is_installed = mod_is_installed(modid, workshopid)
                    if action == 'install':
                        if not is_installed:
                            if not force:
                                create_reform(message, 'mod', [action, modid, workshopid])
                            else:
                                install_mod(modid, workshopid)
                                reply_to(message, msg_change_implemented)
                        elif is_installed:
                            reply_to(message, already_installed_msg)
                        else:
                            reply_to(message, msg_unhandled_exception)
                    elif action == 'uninstall':
                        if is_installed:
                            if not force:
                                create_reform(message, 'mod', [action, modid, workshopid])
                            else:
                                uninstall_mod(modid, workshopid)
                                reply_to(message, msg_change_implemented)
                        elif not is_installed:
                            reply_to(message, msg_mod_not_installed)
                        else:
                            reply_to(message, msg_unhandled_exception)
                    else:
                        reply_to(message, mod_msg_helper)
                else:
                    if source == 'url':
                        reply_to(message, strip_modid_from_url_failed)
                    elif source == 'command':
                        reply_to(message, msg_modid_invalid)
                    elif source == 'file':
                        reply_to(message,  msg_workshopid_from_file_failed)
                    else:
                        reply_to(message, msg_unhandled_exception)
            def install_uninstall_mod_cmd_handler(command):
                if len(command) == 3:
                    if is_workshop_url(command[2]):
                        install_uninstall_mod_cmd(command[1], strip_IDs_from_steam(command[2]), 'url')
                    elif command[1] == 'uninstall' and is_modid(command[2]):
                        install_uninstall_mod_cmd(command[1], sort_valid_modid_workshopid(command[2], get_workshopid_from_installed_mods(command[2])), 'file')
                    else:
                        reply_to(message, mod_msg_helper)
                elif len(command) == 4:
                    install_uninstall_mod_cmd(command[1], sort_valid_modid_workshopid(command[2], command[3]), 'command')
            # Let's capture the text between quotes (some intelligent modders put spaces in the name of their mod)
            try:
                error = True
                logger(f"Capturing message: {message.text}", "DEBUG")
                command = message.text.split()
                first = False
                for e in message.text.split():
                    if '"' in e:
                        if not first:
                            if e.count('"') < 2:
                                f = command.index(e)
                                first = True
                            elif e.count('"') > 2:
                                logger("Abnormal amount of \" detected in the command", "DEBUG")
                                break
                        elif first:
                            s = command.index(e)
                            command[f:s+1] = [' '.join(command[f:s+1])]
                            first = False
                command = [e.strip('"') if e.startswith('"') and e.endswith('"') else e for e in command]
                error = False
            except Exception as e:
                logger(e, "ERROR")
            if not error:
            # Finally...
                logger(f"Capturing mod command: {command}", "DEBUG")
                if len(command) in range(2,6):
                    if command[1] == 'list' and len(command) == 2:
                        list_mod_cmd()
                    elif command[1] in ['install', 'uninstall'] and len(command) in range(2,5):
                        install_uninstall_mod_cmd_handler(command)
                    elif command[1] == 'move' and len(command) == 4 and string_is_integer(command[2]) and string_is_integer(command[3]):
                        move_mod(int(command[2]), int(command[3]))
                    else:
                        reply_to(message, mod_msg_helper)
                else:
                    reply_to(message, mod_msg_helper)
            else:
                reply_to(message, "Abnormal amount of \" detected in the command")
        # MODIFY PZSERVER SETTINGS
        @bot.message_handler(commands=[setting_cmd])
        def setting_command(message, force=False):
            def set_setting_cmd_handler(command):
                if command[2] in ["ServerWelcomeMessage", "Map", "PublicName", "PublicDescription", "DiscordChannel"]: # Exception List
                    import re
                    match = re.match(r"/setting set (\w+) (.+)", message.text)
                    if match:
                        content = match.group(2)
                        if not force:
                            create_reform(message, 'setting', [command[2], content])
                        else:
                            set_setting_value(command[2], content)
                            reply_to(message, msg_change_implemented)
                    else:
                        reply_to(message, setting_msg_helper)
                elif not force:
                    create_reform(message, 'setting', [command[2], command[3]])
                else:
                    set_setting_value(command[2], command[3])
                    reply_to(message, msg_change_implemented)
            def set_setting_cmd_info_setup(desc, value):
                return f"{desc}\nCurrent Setting: *{value}*"
            # Alright...
            command = message.text.split()
            if len(command) in range(3,6):
                if (len(command) == 3 and command[1] == 'get') or (len(command) == 4 and command[1] == 'set'):
                    setting_info = get_setting(command[2])
                    if setting_info:
                        setting_info_text = set_setting_cmd_info_setup(setting_info['description'], setting_info['value'])
                        if command[1] == 'get':
                            reply_to(message, setting_info_text)
                        elif command[1] == 'set':
                            set_setting_cmd_handler(command)
                            reply_to(message, setting_info_text)
                    else:
                        reply_to(message, f"\"*{command[3]}*\" is not a setting of this server.")
                else:
                    reply_to(message, setting_msg_helper)
            else:
                reply_to(message, setting_msg_helper)
        # LISTEN FOR UPDATES FROM YOUR NON-ANONYMOUS POLLS
        @bot.poll_answer_handler()
        def poll_vote_event(update):
            update_poll_vote(update.user.id, update.poll_id, update.option_ids)
        # FORCE
        @bot.message_handler(commands=[force_cmd])
        def force_command(message):
            command = message.text.split()
            if member_is_dev(message):
                if len(command) >= 2:
                    if command[1] == setting_cmd:
                        command.pop(0)
                        message.text = ' '.join(command)
                        setting_command(message, force=True)
                    elif command[1] == mod_cmd:
                        command.pop(0)
                        message.text = ' '.join(command)
                        mod_command(message, force=True)
                    elif len(command) == 2 and command[1] == restart_cmd:
                        message.text = restart_confirm_cmd
                        confirm_restart_command(message, force=True)
                    else:
                        reply_to(message, msg_force_cmd_incorrect_syntax)
                else:
                    reply_to(message, msg_force_cmd_incorrect_syntax)
            else:
                reply_to(message, msg_only_master)
        # BACKUP
        @bot.message_handler(commands=[backup_cmd])
        def backup_command(message):
            def is_valid_backup_name(name):
                return not any(char in set('/:?*|"<>\\\'') for char in name)
            command = message.text.split()
            options = ['map', 'players', 'vehicles', 'items', 'settings']
            if member_is_dev(message):
                if len(command) in range(3, 3+4+len(options)+1):
                    action = command[1]
                    if action == 'save':
                        if is_valid_backup_name(command[2]):
                            backup_name = command[2]
                            # Verify options are in the command only once or zero
                            if all(command.count(option) < 2 for option in options):
                                # Veryfy only valid options are in the command
                                for opt in command[3:]:
                                    sentence1 = opt in options
                                    sentence2 = 'map' in command and opt.isdigit() and command.index('map') < command.index(opt) < command.index('map')+5
                                    print(opt, sentence1, sentence2, sentence1 or sentence2)
                                if all(opt in options or ('map' in command and opt.isdigit() and command.index('map') < command.index(opt) < command.index('map')+5) for opt in command[3:]):
                                    # Verify map coordinates are numbers
                                    if 'map' in command:
                                        if all(command[i].isdigit() for i in range(command.index('map') + 1, command.index('map') + 5)):
                                            x1, y1, x2, y2 = map(int, command[command.index('map') + 1: command.index('map') + 5])
                                            world_flag = True
                                        else:
                                            reply_to(message, "One of the coordinates you used is not a number")
                                            return False
                                    else:
                                        world_flag = False
                                    backup_save(message, backup_name, world=[x1, x2, y1, y2] if world_flag else False, players='players' in command, vehicles='vehicles' in command, items='items' in command, settings='settings' in command)
                                else:
                                    reply_to(message, "You used an invalid option in the command")
                            else:
                                reply_to(message, "You used one of the options more than once")
                        else:
                            reply_to(message, "You used a character not allowed in the backup name.")
                    elif action == 'restore' and len(command) > 3:
                        if game.manager.tmux_session_state():
                            reply_to(message, "You can't restore a backup while the server is running.")
                        backup_check = backup_exists(command[2])
                        if backup_check:
                            b_world, b_players, b_items, b_vehicles, b_settings = backup_check                            
                            if all(opt in options for opt in command[3:]):
                                if all(command.count(option) < 2 for option in options):
                                    world = 'map' in command
                                    players = 'players' in command
                                    items = 'items' in command
                                    vehicles = 'vehicles' in command
                                    settings = 'settings' in command
                                    conflict = []
                                    if world and not b_world:
                                        conflict.append('map')
                                    if players and not b_players:
                                        conflict.append('players')
                                    if items and not b_items:
                                        conflict.append('items')
                                    if vehicles and not b_vehicles:
                                        conflict.append('vehicles')
                                    if settings and not b_settings:
                                        conflict.append('settings')
                                    if conflict:
                                        reply_to(message, f"Aborting. The backup you are trying to restore doesn't have the following data: {', '.join(conflict)}.")
                                    else:
                                        backup_restore(message, backup_name, world='map' in command, players='players' in command, items='items' in command, vehicles='vehicles' in command)
                                else:
                                    reply_to(message, "You used the same option more than once.")
                            else:
                                reply_to(message, "You used an invalid option.")
                        else:
                            reply_to(message, "The backup you are trying to restore doesn't exist.")
                    else:
                        reply_to(message, backup_msg_helper)
                else:
                    reply_to(message, backup_msg_helper)
            else:
                reply_to(message, msg_only_master)          

        ########################################
        ### TELEBOT - START POLLING
        ########################################
        
        log_emendazio()
        bot.infinity_polling()
        
    except Exception as e:
        logger(e, "ERROR")
