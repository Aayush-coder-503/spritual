import requests
from typing import Optional
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "004b8f6a-4ab4-4e79-bbcf-e822281fd951"
APPLICATION_TOKEN = "AstraCS:lzvpPvcLBKNjLaRpIEBInIzZ:8218a37a93f615a0eb8da037c0fa6705223af98f9b600886c90087cdf30679e3AstraCS:xbIaSnPrzfgBqEeYEoqWBuvj:d6d7e4fc1b3346237ff6ff87292241eba14b0681e04cafa083ea80bc971688f1"

def get_astro(name,dob,location,context):
        
    TWEAKS = {
  "TextInput-zkVyT": {"input_value": name},
  "TextInput-aE6MI": {"input_value": dob},
  "TextInput-RZNf7": {"input_value": location},
  "TextInput-R64jj": {"input_value": context},
    }
    return run_flow("",tweaks=TWEAKS,application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/astro"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()["outputs"][0]["outputs"][0]["results"]["message"]["text"]


def GPT_insight(name,dob,location,context):
    result = get_astro(name=name,dob=dob,location=location,context=context)
    return result