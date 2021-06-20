import subprocess
from basenames import build_deploy_basename


def deploy(port):
    deploy_basename = build_deploy_basename(port)
    template = """
    gcloud functions deploy proxy_{} \
    --runtime nodejs10 \
    --allow-unauthenticated \
    --trigger-http \
    --memory=128 \
    --timeout=60s \
    > {} 2>&1 & 
    """
    command = template.format(port, deploy_basename)
    subprocess.run(command, shell=True)
