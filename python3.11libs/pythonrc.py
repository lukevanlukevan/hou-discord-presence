import subprocess
import hrpyc
import threading

def run_script():
    CREATE_NO_WINDOW = 0x08000000
    script_path = hou.text.expandString("$HDP/call.py")
    subprocess.Popen(['python', script_path], creationflags=CREATE_NO_WINDOW)

try:
    hrpyc.start_server(port=9900)
    run_script()
    print("Created Dicord Presence server on port 9900")
except Exception as e:
    print(e)
    print("Failed to create Discord Presence server")
