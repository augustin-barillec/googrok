import signal
import subprocess
import os


def list_processes(contains=None):
    out = subprocess.check_output(['ps', '-af'], universal_newlines=True)
    lines = out.splitlines()
    if contains is not None:
        lines = [line for line in lines if contains in line]
    return lines


def kill_processes(contains=None):
    lines = list_processes(contains=contains)
    for line in lines:
        pid = int(line.split(None, 2)[1])
        os.kill(pid, signal.SIGKILL)
        print('KILLED: {}'.format(line))


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def delete_files(file_paths):
    for p in file_paths:
        delete_file(p)
