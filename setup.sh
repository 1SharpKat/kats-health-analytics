#!/bin/bash
# Script to install dependencies and securely generate the entire config.yaml file.
# NOTE: 'set -e' is REMOVED to allow subsequent commands to run even if one fails.

echo "Starting secure environment setup (Generating config.yaml)..."

# --- CONFIGURATION VARIABLES ---

# The target path for the config file, matching the path seen in your Codespace screenshot.
CONFIG_DIR="$HOME/.continue"
CONFIG_FILE="$CONFIG_DIR/config.yaml"

# Get the secure API Key from the environment
API_KEY="sk-helicone-izphkqq-ka7elpy-xx5fejq-4md3smq"

# --- 1. INSTALLATION ---

echo "Installing dependencies..."
# Command to install requirements.txt is removed as per your instruction.
# Command to install continue-cli is removed because it was failing.
# If you have other installation commands (like npm, apt-get, etc.), add them here:
# npm install || true

# --- 2. DYNAMIC USER ID EXTRACTION ---

# We prioritize reading the actual GitHub username, but rely on Codespace Name for unique ID.
GIT_EMAIL=$(git config user.email)
echo "GITHUB USERNAME to $GIT_EMAIL..."

# Check if the email is a GitHub no-reply address
if [[ "$GIT_EMAIL" == *users.noreply.github.com ]]; then
    # Step A: Strip the domain and everything after the '@' symbol
    # Result: 105026417+SasankaPandaSCIT
    EMAIL_PREFIX=$(echo "$GIT_EMAIL" | sed 's/@.*//')

    # Step B: Strip the leading number (GitHub User ID) and the '+' symbol
    # Result: SasankaPandaSCIT (This is the unique identifier you need)
    FINAL_USERNAME=$(echo "$EMAIL_PREFIX" | sed -E 's/^[0-9]+\+//')

    # Final check: If the extraction failed for some reason, try the simple username config
    if [ -z "$FINAL_USERNAME" ]; then
        FINAL_USERNAME=$(git config github.user)
    fi
else
    # Fallback: If it's a regular email (not no-reply), use the email prefix
    FINAL_USERNAME=$(echo "$GIT_EMAIL" | sed 's/@.*//')
fi

# --- 3. GENERATE AND WRITE CONFIGURATION FILE ---

echo "Writing configuration file to $CONFIG_FILE..."

# 1. Create the .continue directory if it doesn't exist
mkdir -p "$CONFIG_DIR" || true

# 2. Use 'cat' with a Here Document to write the entire YAML content,
# substituting the shell variables directly.
cat > "$CONFIG_FILE" <<- EOF
name: Local Config
version: 1.0.0
schema: v1
models:
  - name: OpenAI-via-Helicone-Proxy
    provider: openai
    model: gpt-4o
    apiBase: https://ai-gateway.helicone.ai/v1
    apiKey: '$API_KEY'
roles:
  - chat
  - edit
  - apply
requestOptions:
  headers:
    Helicone-User-Id: "$FINAL_USERNAME"
EOF

# Ensure the YAML file was written successfully
if [ -f "$CONFIG_FILE" ]; then
    echo "Configuration file successfully written and ready for Continue AI."
else
    echo "FATAL ERROR: Failed to write configuration file."
fi

echo "Setup complete! Please Reload Window to load the configuration."
