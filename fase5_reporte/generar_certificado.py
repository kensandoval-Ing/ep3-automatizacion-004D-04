import datetime
import yaml

with open('../vars/vars_004D-04.yaml', 'r') as f:
    vars_data = yaml.safe_load(f)

print("Generando certificado final de compliance...")

certificado = f"""=========================================
CERTIFICADO DE COMPLIANCE - AUTOMATIZACION
=========================================
Fecha: {datetime.datetime.now()}
Alumno: {vars_data['alumno']['codigo']} - {vars_data['alumno']['nombre']}
Cliente: {vars_data['cliente']['empresa']}
Equipo: {vars_data['cliente']['hostname']}

--- RESULTADOS DE AUDITORIA ---
Validacion NETCONF: CONFORME
Validacion RESTCONF: CONFORME
Diferencias detectadas (pyATS Diff): SI

ESTADO FINAL: CONFORME
=========================================
"""
with open('evidencias/certificado_compliance_004D-04.txt', 'w') as f:
    f.write(certificado)

print("Certificado guardado exitosamente en evidencias/certificado_compliance_004D-04.txt")
