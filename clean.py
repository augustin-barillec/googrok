import glob
from utils import kill_processes, delete_file, delete_files
from basenames import build_ngrok_basename, build_index_basename, \
    build_deploy_basename


def kill_ngrok():
    kill_processes(contains='ngrok http')


def kill_deploy():
    kill_processes(contains='functions deploy')


def delete_ngrok_outfiles():
    basenames = glob.glob(build_ngrok_basename('*'))
    delete_files(basenames)


def delete_index_file():
    basename = build_index_basename()
    delete_file(basename)


def delete_deploy_outfiles():
    basenames = glob.glob(build_deploy_basename('*'))
    delete_files(basenames)


def clean_ngrok():
    kill_ngrok()
    delete_ngrok_outfiles()
    delete_index_file()


def clean_deploy():
    kill_deploy()
    delete_deploy_outfiles()


def clean_ngrok_deploy():
    clean_ngrok()
    clean_deploy()
