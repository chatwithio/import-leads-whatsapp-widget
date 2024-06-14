import csv
import json
import base64
import requests

def leer_csv(ruta_archivo):
    with open(ruta_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            print(f"Fila leída del CSV: {fila}")
            
            datos_fila = [
                {
                    "data": "",
                    "type": "text",
                    "label": "Nombre",
                    "required": True,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "FirstName",
                    "val": fila.get('nombre'),
                    "isError": False
                },
                {
                    "data": "",
                    "type": "text",
                    "label": "Apellidos",
                    "required": True,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "LastName",
                    "val": "NA",
                    "isError": False
                },
                {
                    "data": "",
                    "type": "tel",
                    "label": "Teléfono",
                    "required": True,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Phone",
                    "val": fila.get('telefono'),  
                    "telCode": "34",
                    "telNum": fila.get('telefono'), 
                    "isError": False
                },
                {
                    "data": "",
                    "type": "email",
                    "label": "Email",
                    "required": False,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Email",
                    "val": fila.get('email'),
                    "isError": False
                },
                {
                    "data": "MG ZS EV MCE 51kWh COM|MG ZS EV MCE 51kWh LUX|MG eHS 1.5T AT COM|MG eHS 1.5T AT LUX|MG Marvel R EDU AT COM|MG Marvel R EDU AT LUX|MG 5 EV 51kWh COM|MG 5 EV 51kWh LUX|MG ZS 1.5L 5MT COM|MG ZS 1.5L 5MT LUX|MG4 AT 51kWh|MG4 AT 64kWh|HS 1.5T MT COM|HS 1.5T MT LUX|MG HS (no Specific version)|MG ZS (no Specific version)",
                    "type": "select",
                    "label": "Interest_Model__c",
                    "required": True,
                    "dataObject": [{"score": "", "value": val} for val in [
                        "MG ZS EV MCE 51kWh COM", "MG ZS EV MCE 51kWh LUX", "MG eHS 1.5T AT COM", "MG eHS 1.5T AT LUX",
                        "MG Marvel R EDU AT COM", "MG Marvel R EDU AT LUX", "MG 5 EV 51kWh COM", "MG 5 EV 51kWh LUX",
                        "MG ZS 1.5L 5MT COM", "MG ZS 1.5L 5MT LUX", "MG4 AT 51kWh", "MG4 AT 64kWh", "HS 1.5T MT COM",
                        "HS 1.5T MT LUX", "MG HS (no Specific version)", "MG ZS (no Specific version)"
                    ]],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "Interest_Model__c",
                    "val": "MG4 AT 64kWh",
                    "isError": False
                },
                {
                    "data": "",
                    "type": "text",
                    "label": "Dealer_Code__c",
                    "required": True,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "Dealer_Code__c",
                    "val": fila.get('dealer'),
                    "isError": False
                },
                {
                    "data": "",
                    "hval": "Email Opt Out",
                    "type": "hidden",
                    "label": "Option_Out__c",
                    "required": False,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "Option_Out__c",
                    "val": "Email Opt Out",
                    "isError": False
                },
                {
                    "data": "",
                    "hval": "OEM Website",
                    "type": "hidden",
                    "label": "LeadSource",
                    "required": False,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "LeadSource",
                    "val": "OEM Website",
                    "isError": False
                },
                {
                    "data": "",
                    "hval": "true",
                    "type": "checkbox",
                    "label": "web Consent",
                    "required": False,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "Web_Form_Consent__c",
                    "val": True,
                    "isError": False
                },
                {
                    "data": "",
                    "hval": "true",
                    "type": "hidden",
                    "label": "OEM_Lead__c",
                    "required": False,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "OEM_Lead__c",
                    "val": "true",
                    "isError": False
                },
                {
                    "data": "",
                    "hval": "Spain",
                    "type": "hidden",
                    "label": "Country_EU__c",
                    "required": False,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "Country_EU__c",
                    "val": "Spain",
                    "isError": False
                },
                {
                    "data": "Hot|Warm|Cold",
                    "type": "select",
                    "label": "Rating",
                    "required": False,
                    "dataObject": [{"score": "", "value": val} for val in ["Hot", "Warm", "Cold"]],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "Rating",
                    "val": "Hot",
                    "isError": False
                },
                {
                    "data": "",
                    "type": "text",
                    "label": "UTM",
                    "required": False,
                    "dataObject": [],
                    "salesforce": True,
                    "salesforceType": "Custom",
                    "salesforceCustom": "Campaign_Name__c",
                    "val": fila.get("utm", ""),
                    "isError": False
                }
            ]

            # Convertir los datos de la fila a JSON
            json_data = convertir_a_json(datos_fila)
            # Convertir el JSON a base64
            base64_data = convertir_a_base64(json_data)
            # Enviar los datos a la API
            enviar_datos(base64_data)

def convertir_a_json(datos):
    json_data = json.dumps(datos, ensure_ascii=False)
    print(f"Datos JSON: {json_data}")
    return json_data

def convertir_a_base64(json_data):
    mensaje_bytes = json_data.encode('utf-8')
    base64_bytes = base64.b64encode(mensaje_bytes)
    base64_mensaje = base64_bytes.decode('utf-8')
    print(f"Datos en base64: {base64_mensaje}") 
    return base64_mensaje

def enviar_datos(base64_data):
    real_example_payload = {
        "data": base64_data,
        "screenwidth": 2560,
        "url": "https://services.tochat.be/es/whatsapp-business-directory/person/b25dabb2-2122-4cc0-be57-1a769dfaac1d"
    }

    url = "https://services.tochat.be/api/business/send/b25dabb2-2122-4cc0-be57-1a769dfaac1d"
    response = requests.post(url, json=real_example_payload)
    print(response.status_code)
    print(response.text)

# Ruta del archivo CSV
ruta_archivo = 'datos.csv'

# Leer y procesar los datos del CSV
leer_csv(ruta_archivo)