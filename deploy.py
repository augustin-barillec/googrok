import subprocess
from basenames import build_deploy_basename


def deploy(port, project_id, region=None):
    deploy_basename = build_deploy_basename(port)
    command = f"""
    gcloud functions deploy proxy_{port} \
    --project {project_id} \
    --runtime nodejs10 \
    --allow-unauthenticated \
    --trigger-http \
    --memory=128 \
    --timeout=60s"""
    if region is not None:
        command += f' --region {region}'
    command += f' > {deploy_basename} 2>&1 &'
    subprocess.run(command, shell=True)
