import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def generate_text(prompt):
    # Define the URL and API key
    url = "https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText"
    api_key = os.environ["PALMAPI"]

    if api_key is None:
        raise ValueError("API key not found in the PALMAPI environment variable.")

    # Define the request headers and data
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "prompt": {
            "text": prompt
        }
    }

    # Convert the data to a JSON string
    data_json = json.dumps(data)

    # Create the request
    response = requests.post(url, headers=headers, data=data_json, params={"key": api_key})

    # Check if the request was successful
    if response.status_code == 200:
        output_text = response.json()['candidates'][0]['output']
        return {"output": output_text}
    else:
        return {"error": f"Request failed with status code {response.status_code}", "response_text": response.text}