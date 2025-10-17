#!/bin/bash

# This file runs the llm + doom exe

# Please ensure that you have placed a .env with your openai api key into
# restful-doom/src/py


SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
DOOM_EXE_PATH="Your built DOOM executable here"
IWAD_PATH="Your DOOM WAD here"


listenerCmd="python"
listenerArg=( "$SCRIPT_DIR/src/py/listener.py")

doomCmd="$DOOM_EXE_PATH"
doomArg=("-apiport" "6666" "-iwad" "$IWAD_PATH" "-server" "-screensize" "11")

$listenerCmd "${listenerArg[@]}" &

$doomCmd "${doomArg[@]}" &
