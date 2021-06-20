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


def main_deploy(ports):
    clean.clean_deploy()
    for p in ports:
        deploy.deploy(p)


parser = argparse.ArgumentParser()
parser.add_argument('action', type=str)
parser.add_argument('--ports', nargs='+', type=int, required=True)
args = parser.parse_args()
assert len(args.ports) <= 10
assert args.action in ('ngrok', 'deploy', 'ngrok_deploy')

if args.action == 'ngrok':
    main_ngrok(args.ports)
elif args.action == 'deploy':
    main_deploy(args.ports)
elif args.action == 'ngrok_deploy':
    main_ngrok(args.ports)
    main_deploy(args.ports)
