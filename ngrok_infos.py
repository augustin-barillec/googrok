import time
import requests
from basenames import build_index_basename


def get_port_url(i):
    r = None
    while r is None or 'tunnels' not in r or len(r['tunnels']) < 2:
        try:
            r = requests.get(f'http://127.0.0.1:404{i}/api/tunnels').json()
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(2)
    r = r['tunnels'][1]
    port = int(r['config']['addr'].split('localhost:')[1])
    url = r['public_url'].split('//')[1]
    url = f'https://{url}'
    return port, url


def get_port_to_url(ports):
    port_url_list = [get_port_url(i) for i in range(len(ports))]
    res = dict(port_url_list)
    assert sorted(ports) == sorted(list(res.keys()))
    return res


def create_index_js(port_to_url):
    index_content = "const get_app = require('./get-app.js');\n"
    for p in sorted(port_to_url):
        url = port_to_url[p]
        index_content += f"exports.proxy_{p} = get_app.getApp('{url}')\n"
    index_basename = build_index_basename()
    with open(index_basename, "w") as text_file:
        text_file.write(index_content)
