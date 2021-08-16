import argparse
import clean
import ngrok_run
import ngrok_infos
import deploy


def main_ngrok(ports):
    clean.clean_ngrok()
    for p in ports:
        ngrok_run.run(p)
    port_to_url = ngrok_infos.get_port_to_url(ports)
    ngrok_infos.create_index_js(port_to_url)


def main_deploy(project_id, ports, region):
    clean.clean_deploy()
    for p in ports:
        deploy.deploy(project_id, p, region)


parser = argparse.ArgumentParser()
parser.add_argument('action', type=str)
parser.add_argument('--ports', nargs='+', type=int, required=True)
parser.add_argument('--project_id', type=str)
parser.add_argument('--region')
args = parser.parse_args()
assert len(args.ports) <= 10
assert args.action in ('ngrok', 'deploy', 'ngrok_deploy')
if 'deploy' in args.action:
    assert args.project_id is not None

if args.action == 'ngrok':
    main_ngrok(args.ports)
elif args.action == 'deploy':
    main_deploy(args.project_id, args.ports, args.region)
elif args.action == 'ngrok_deploy':
    main_ngrok(args.ports)
    main_deploy(args.project_id, args.ports, args.region)
