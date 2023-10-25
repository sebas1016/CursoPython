from apiclient import discovery #Crea interfaz para interactuar con la api de google
from httplib2 import Http #Usuario para realizar las consultas a la API de google
from oauth2client.service_account import (
    ServiceAccountCredentials) #Logeo sin afectar las cuentas
import json

SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'PYQT6\Formularios-google\credentials.json',
    SCOPES
    )

http = creds.authorize(Http())

form_service = discovery.build(
    'forms',
    'v1',
    http=http,
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False
)

NEW_FORM = {
    "info": {
        "title": "Mi formulario",
    }
}

NEW_QUESTION = {
    "requests":[{
        "createItem": {
            "item": {
                "title": "¿Cúal es la capital de colombia?",
                "questionItem":{
                    "question":{
                        "required": True,
                        "choiceQuestion":{
                            "type": "RADIO",
                            "options": [
                                {"value": "Medellín"},
                                {"value": "sindey"},
                                {"value": "Bogota"},
                                {"value": "La paz"}
                            ],
                            "shuffle": True
                        }
                    }
                },
            },
            "location": {
                "index": 0
            }
        }
    }]
}

result = form_service.forms().create(
    body = NEW_FORM).execute()

question_setting = form_service.forms(
    ).batchUpdate(
        formId=result["formId"],
        body=NEW_QUESTION
    ).execute()

get_result = form_service.forms().get(
    formId=result["formId"]
).execute()

print(json.dumps(get_result,indent=4))