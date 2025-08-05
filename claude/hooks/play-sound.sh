#!/bin/bash

PROJECT_DIR=$1

# Check if project directory was provided
if [ -z "$PROJECT_DIR" ]; then
    exit 0
fi

# Check for sound files in project directory
if [ -f "$PROJECT_DIR/hooks/done.wav" ]; then
    SOUND_FILE="$PROJECT_DIR/hooks/done.wav"
elif [ -f "$PROJECT_DIR/hooks/done.mp3" ]; then
    SOUND_FILE="$PROJECT_DIR/hooks/done.mp3"
else
    # No sound file found, exit silently
    exit 0
fi

# Play sound based on OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    afplay "$SOUND_FILE" 2>/dev/null &
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v aplay &> /dev/null; then
        # aplay typically only supports WAV files
        if [[ "$SOUND_FILE" == *.wav ]]; then
            aplay "$SOUND_FILE" 2>/dev/null &
        elif command -v mpg123 &> /dev/null && [[ "$SOUND_FILE" == *.mp3 ]]; then
            mpg123 -q "$SOUND_FILE" 2>/dev/null &
        fi
    elif command -v paplay &> /dev/null && [[ "$SOUND_FILE" == *.wav ]]; then
        paplay "$SOUND_FILE" 2>/dev/null &
    elif command -v mpg123 &> /dev/null && [[ "$SOUND_FILE" == *.mp3 ]]; then
        mpg123 -q "$SOUND_FILE" 2>/dev/null &
    fi
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows
    powershell -c "(New-Object Media.SoundPlayer '$SOUND_FILE').PlaySync()" 2>/dev/null &
fi