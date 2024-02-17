#!/bin/bash

LOG_FILE="/opt/pzserver/pzserver.log"
SESSION_NAME="pzserver"
SERVER_START_CMD="/opt/pzserver/start-server.sh --servername '[PvPvE] Menzian Fields' | tee $LOG_FILE"
TIMEOUT=60

case "$1" in
  --see)
    tmux attach-session -t $SESSION_NAME
    ;;
  --start)
    /opt/pzserver/python/bin/python /opt/pzserver/telegram_bot/pzserver_tg.py >> /opt/pzserver/telegram_bot/pzserver_tg.log &    
    tmux new-session -d -s $SESSION_NAME "$SERVER_START_CMD"
    ;;
  --stop)
    tmux send-keys -t $SESSION_NAME "save" C-m
    tmux send-keys -t $SESSION_NAME "quit" C-m

    # Attendi fino a quando il processo pzserver termina o timeout
    timeout=0
    while [ $timeout -lt $TIMEOUT ]; do
      if tmux has-session -t $SESSION_NAME 2>/dev/null; then
       	sleep 1 && ((timeout++))
      else
        break
      fi
    done
    if [ $timeout -eq $TIMEOUT ]; then
      echo "Server timeout exception"
    else
      echo "Server has been terminated."
    fi
    ;;
  *)
    echo "Usage: pzserver --see | --start | --stop"
    exit 1
    ;;
esac
