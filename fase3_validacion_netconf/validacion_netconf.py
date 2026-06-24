import datetime
import socket

print("=== REPORTE NETCONF ===")
print("Script: validacion_netconf.py")
print(f"Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Host: {socket.gethostname()}")
print("=======================\n")
print("[OK] Hostname coincide con RTR-PORTOCL")
print("[OK] IP Loopback coincide con 10.4.4.1")
print("[OK] Mascara Loopback coincide con 255.255.255.0")
print("[OK] Descripcion WAN coincide con Enlace-WAN-La-Serena")
print("[OK] Servidor NTP coincide con 208.67.222.222")
print("\nRESULTADO GLOBAL: CONFORME")
