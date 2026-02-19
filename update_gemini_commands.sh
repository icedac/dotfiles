#!/bin/bash

# Script to convert .md commands to .toml for Gemini CLI
# Located in ~/dotfiles/update_gemini_commands.sh

COMMANDS_DIR="$HOME/dotfiles/ai-commands"

if [ ! -d "$COMMANDS_DIR" ]; then
    echo "Error: Directory $COMMANDS_DIR does not exist."
    exit 1
fi

echo "Converting .md files in $COMMANDS_DIR to .toml..."

python3 -c "
import os
import glob
import re
import json

target_dir = os.path.expanduser('$COMMANDS_DIR')
md_files = glob.glob(os.path.join(target_dir, '*.md'))

for md_path in md_files:
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        description = None
        prompt = content

        # Check for YAML-style frontmatter
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
        if match:
            frontmatter_raw = match.group(1)
            prompt = match.group(2)
            
            for line in frontmatter_raw.split('\n'):
                if line.strip().startswith('description:'):
                    description = line.split(':', 1)[1].strip()
                    break

        toml_path = md_path.rsplit('.', 1)[0] + '.toml'
        
        lines = []
        if description:
            lines.append(f'description = {json.dumps(description)}')
        
        lines.append(f'prompt = {json.dumps(prompt.strip())}')

        with open(toml_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
        
        print(f'✅ Converted: {os.path.basename(md_path)} -> {os.path.basename(toml_path)}')

    except Exception as e:
        print(f'❌ Failed to convert {os.path.basename(md_path)}: {e}')
"

echo "Conversion complete."
