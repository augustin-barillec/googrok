def build_ngrok_basename(port):
    return 'ngrok_{port}.out'.format(port=port)


def build_index_basename():
    return 'index.js'


def build_deploy_basename(port):
    return 'deploy_{port}.out'.format(port=port)
