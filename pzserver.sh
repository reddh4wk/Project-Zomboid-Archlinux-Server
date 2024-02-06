#!/bin/bash

SESSION_NAME="pzserver"
SERVER_START_CMD="/opt/pzserver/start-server.sh --servername '[PvPvE] The Testing Grounds'"
TIMEOUT=60

case "$1" in
  --see)
    tmux attach-session -t $SESSION_NAME
    ;;
  --start)
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
