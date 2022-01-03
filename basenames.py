def build_ngrok_basename(port):
    return f'ngrok_{port}.out'


def build_index_basename():
    return 'index.js'


def build_deploy_basename(port):
    return f'deploy_{port}.out'
