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

########################################
### THIS FILE IS BEING LAUNCHED BY \OPT\PZSERVER.SH, WHICH IS BEING LAUNCHED BY SYSTEMCTL
########################################

# FOR THE LOGS
from pzserver_main import clean_logs,logger,log_file

########################################
### AVOID DOUBLE EXECUTION OF THIS SCRIPT ON THE CURRENT SYSTEM
########################################

# IF I IMPORT THIS FROM MAIN IT GETS THE PID AND NAME OF MAIN, SO I AM PUTTING IT HERE TOO
def get_pid_and_name():
    import os
    import sys
    return (os.getpid(), os.path.abspath(sys.argv[0]))

########################################
### FLAGS
########################################

command_flag = True
join_flag = True
left_flag = True

########################################
### MAIN
########################################

from pzserver_main import get_servicename
service_name=get_servicename()

global_association_table = []

def send_to_all(text):
    from pzserver_main import get_chats
    chat_ids=get_chats()
    for each in chat_ids:
        bot.send_message(each, text)

def alert_bot(keyword, line):
    try:
        import re
        if keyword == 'Zomboid Server is VAC Secure':
            send_to_all(service_name.capitalize()+" is now online.")
        elif keyword == 'command entered via server console (System.in): "quit"':
            send_to_all(service_name.capitalize()+" is going down...")
        elif command_flag and keyword == "command entered":
            if '"quit"' not in line and '"save"' not in line:
                send_to_all("A"+line[44:])
        elif join_flag and keyword == "BUpdateUserData":
            pattern_username = r"'(.*?)'"
            username = re.search(pattern_username, line).group(1)
            pattern_steamid = r"id=(\d+)"
            steamid = re.search(pattern_steamid, line).group(1)
            for each in global_association_table:
                if each[0] == steamid:
                    if each[2] == 1:
                        left = True
                found = True
            if left or not found:
                send_to_all("A player connected to the server: "+username)
            global_association_table.append([steamid, username, 0])
        elif left_flag and keyword == "CloseConnection: Finally disconnected":
            pattern_steamid = r"SteamID=(\d+)"
            steamid = re.search(pattern_steamid, line).group(1)
            username = False
            for each in global_association_table:
                if each[0] == steamid:
                    username = each[1]
            if not username:
                username = steamid
            send_to_all("A player left the server: "+username)
    except Exception as e:
        logger(e, "ERROR")

def monitor_log(filename='/opt/pzserver/pzserver.log', keywords=['Zomboid Server is VAC Secure','command entered via server console (System.in): "quit"',"CloseConnection: Finally disconnected","BUpdateUserData","command entered"]):
    import time
    try:
        with open(filename, 'r') as f:
            f.seek(0, 2)
            while True:
                current_position = f.tell()
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    f.seek(current_position)
                else:
                    for keyword in keywords: 
                        if keyword in line:
                            alert_bot(keyword, line)
    except Exception as e:
        logger(e, "ERROR")

if __name__ == '__main__':
    try:
        from pzserver_main import run_command,is_already_running,get_token
        pid, name = get_pid_and_name()
        if is_already_running(pid, name):
            print("Another instance of the script is already running.")
            sys.exit(1)
        import telebot
        bot = telebot.TeleBot(get_token())
        clean_logs()
        monitor_log()
    except Exception as e:
        logger(e, "ERROR")
