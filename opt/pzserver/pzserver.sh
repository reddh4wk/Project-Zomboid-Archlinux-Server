#!/usr/bin/env bash

SOURCE=${BASH_SOURCE[0]}
while [ -L "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )
  SOURCE=$(readlink "$SOURCE")
  [[ $SOURCE != /* ]] && SOURCE=$DIR/$SOURCE # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR=$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )

LOG_FILE="$DIR/pzserver.log"
SERVICE_NAME=$(basename "$DIR")
SERVER_START_CMD="$DIR/start-server.sh -servername $SERVICE_NAME | tee $LOG_FILE"
TIMEOUT=60
PYTHON_VENV_BIN="$DIR/python/bin/python"

case "$1" in
  --see)
    tmux attach-session -t $SERVICE_NAME
    ;;
  --start)
    $PYTHON_VENV_BIN $DIR/telegram_bot/pzserver_tg.py >> $DIR/telegram_bot/pzserver_tg.log &
    tmux new-session -d -s $SERVICE_NAME "$SERVER_START_CMD"
    ;;
  --stop)
    tmux send-keys -t $SERVICE_NAME "save" C-m
    tmux send-keys -t $SERVICE_NAME "quit" C-m

    # Attendi fino a quando il processo pzserver termina o timeout
    timeout=0
    while [ $timeout -lt $TIMEOUT ]; do
      if tmux has-session -t $SERVICE_NAME 2>/dev/null; then
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
