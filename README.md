# French-Translator
An on-the-fly french translator application.

### What does what?
frtoen.py takes French and outputs in English

frtoenfile.py takes a file that has French speech and outputs in English. (Note: this file does not work yet)

entofr.py takes English and outputs in French

entofrtext.py takes English text input and outputs in French

## How to install?
1. Run the command `git clone https://github.com/jack-debug/French-Translator.git` (if on Windows, use the software Git Bash to run this command)
2. Go to your terminal and try `cd French-Translator`
3. Run the command `pip install -r requirements.txt `

3a. On Mac, you need to install portaudio before pyaudio. Install homebrew with `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`. Then run `brew install portaudio` and retry installing pyaudio with `pip install pyaudio`

3b. On Windows, pyaudio may not install correctly. To fix, try `pip install pipwin` then `pipwin install pyaudio`.

4. Run the command `python entofr.py` (entofr.py can be swapped with any other script in this repository)
5. Enjoy :)
