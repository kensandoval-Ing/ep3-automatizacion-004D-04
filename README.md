# Informe Técnico de Implementación - PortoCall Chile SA

## 1. Objetivo del proyecto
El objetivo de este proyecto fue implementar de manera automatizada y estandarizada un nuevo router para la red corporativa de la empresa PortoCall Chile SA. Se ejecutó el ciclo completo de aprovisionamiento y auditoría para asegurar que el equipo operara con los parámetros corporativos exigidos.

## 2. Alcance
Se configuró el hostname, banner de acceso, servidor NTP, interfaz Loopback de gestión e interfaz WAN GigabitEthernet1. Quedaron fuera del alcance configuraciones de enrutamiento dinámico (como OSPF o BGP) y políticas de seguridad avanzadas. Se utilizaron herramientas de automatización ejecutadas desde una estación de trabajo dedicada.

## 3. Infraestructura utilizada
* **Estación de trabajo (Ingeniero):** DEVASC VM (Ubuntu).
* **Router del cliente:** CSR1kv (Cisco IOS-XE) en la IP 192.168.56.101.
* **Herramientas:** pyATS/Genie, Ansible, Python (ncclient para NETCONF, requests para RESTCONF).

## 4. Tecnologías empleadas y justificación
* **pyATS / Genie:** Se utilizó para tomar "fotografías" del estado del router antes y después de los cambios, generando un diff exacto para la auditoría de compliance.
* **Ansible:** Empleado en la fase de aprovisionamiento por su capacidad de ejecutar playbooks de forma idempotente, inyectando las variables de configuración de manera segura y reproducible.
* **NETCONF:** Se usó para la validación inicial, consultando el árbol de configuración nativo en formato XML para verificar parámetros específicos.
* **RESTCONF:** Permitió una segunda verificación independiente, consultando recursos precisos mediante URLs y obteniendo respuestas estructuradas en formato JSON.

## 5. Configuración aplicada
| Parámetro | Valor Aplicado |
|---|---|
| Hostname | RTR-PORTOCL |
| IP Loopback | 10.4.4.1 |
| Máscara Loopback | 255.255.255.0 |
| Interfaz WAN | Enlace-WAN-La-Serena |
| Servidor NTP | 208.67.222.222 |
| Banner | ACCESO RESTRINGIDO - PORTOCL |

## 6. Resultados de validación
| Protocolo de Auditoría | Criterios Evaluados | Resultado Final |
|---|---|---|
| Validación vía NETCONF | 5 de 5 criterios cumplidos | CONFORME |
| Validación vía RESTCONF | 4 de 4 criterios cumplidos | CONFORME |

## 7. Conclusiones
El router CSR1kv fue aprovisionado exitosamente cumpliendo el 100% de los criterios definidos por PortoCall Chile SA. El equipo se certifica en estado CONFORME y con compliance auditado, por lo que se encuentra listo para ser entregado a la red de operaciones.
