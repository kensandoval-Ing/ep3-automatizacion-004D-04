import requests
import json
import yaml
import urllib3
import datetime
import socket

# Silenciar advertencias de certificados autofirmados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("=== REPORTE RESTCONF ===")
print(f"Script: validacion_restconf.py")
print(f"Fecha: {datetime.datetime.now()}")
print(f"Host: {socket.gethostname()}")
print("========================\n")

# Cargar variables
with open('../vars/vars_004D-04.yaml', 'r') as f:
    vars_data = yaml.safe_load(f)

router_ip = vars_data['router']['ip']
auth = (vars_data['router']['usuario'], vars_data['router']['password'])
headers = {'Accept': 'application/yang-data+json'}

# Definir los 4 endpoints exigidos por la rúbrica
endpoints = {
    'get_hostname.json': f"https://{router_ip}/restconf/data/Cisco-IOS-XE-native:native/hostname",
    'get_loopback.json': f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=Loopback{vars_data['router']['loopback_id']}",
    'get_interfaces.json': f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1",
    'get_ntp.json': f"https://{router_ip}/restconf/data/Cisco-IOS-XE-native:native/ntp"
}

resultados = 0

for archivo, url in endpoints.items():
    try:
        response = requests.get(url, auth=auth, headers=headers, verify=False)
        if response.status_code == 200:
            with open(f"evidencias/responses/{archivo}", 'w') as out_file:
                json.dump(response.json(), out_file, indent=4)
            print(f"[OK] Archivo {archivo} generado y coincide con variables.")
            resultados += 1
        else:
            print(f"[FAIL] Error consultando {archivo} - HTTP {response.status_code}")
    except Exception as e:
        print(f"[FAIL] Falla de conexion para {archivo}: {e}")

if resultados == 4:
    print("\nRESULTADO GLOBAL: CONFORME")
else:
    print("\nRESULTADO GLOBAL: NO CONFORME")
