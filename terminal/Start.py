import webbrowser
import subprocess

# Define the websites to open in Firefox
firefox_websites = [
    "https://mail.google.com/",
    "https://calendar.google.com/",
    "https://ticktick.com/webapp/#q/all/tasks",
    "https://login.salesforce.com/",
]

# Define the websites to open in Brave
brave_websites = [
    "https://chat.openai.com/",
    "https://proton.me/mail",
    "https://github.com/",
]

# Define the paths to the browsers
# The paths provided below are common paths, but they might be different on your system
firefox_path = "/usr/bin/firefox"
brave_path = "/usr/bin/brave-browser"

# Open each website in Firefox
for website in firefox_websites:
    webbrowser.get(firefox_path).open_new_tab(website)

# Open each website in Brave
for website in brave_websites:
    webbrowser.get(brave_path).open_new_tab(website)

# Open a terminal and run neofetch
terminal_command = ["gnome-terminal", "--", "neofetch"]
subprocess.Popen(terminal_command)