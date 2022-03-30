 1970  git clone https://github.com/BishopFox/GitGot.git && cd GitGot/
 1971  sudo apt-get install python3-dev libfuzzy-dev ssdeep
 1972  pip3 install -r requirements.txt
 1973  export GITHUB_ACCESS_TOKEN=<REDACTED>
 1974  python3 gitgot.py --gist -q 'firefox "main.js" filename:"js"' -r ../gitgot_saved_state.json
