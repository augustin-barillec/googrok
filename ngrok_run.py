import subprocess
from basenames import build_ngrok_basename


def run(port):
    ngrok_basename = build_ngrok_basename(port)
    command = f'./ngrok http {port} --log=stdout > {ngrok_basename} 2>&1 &'
    subprocess.run(command, shell=True)
