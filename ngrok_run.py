import subprocess
from basenames import build_ngrok_basename


def run(port):
    ngrok_basename = build_ngrok_basename(port)
    template = './ngrok http {} --log=stdout > {} 2>&1 &'
    command = template.format(port, ngrok_basename)
    subprocess.run(command, shell=True)
