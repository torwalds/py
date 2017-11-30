import os
import subprocess
import sys

all_child = [os.path.join(os.path.dirname(__file__), i) for i in ('log.py', 'main.py')]
pipes = []


for child in all_child:
    command = [sys.executable, child]
    pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
    pipes.append(pipe)
    pipe.stdin.close()

while pipes:
    pipe = pipes.pop()
    pipe.wait()