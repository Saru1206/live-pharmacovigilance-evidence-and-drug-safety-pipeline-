import requests

url = "https://api.fda.gov/drug/event.json"

params = {
    "search": 'patient.drug.medicinalproduct:"ibuprofen"',
    "limit": 5
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)

data = response.json()

print("Number of records:", len(data.get("results", [])))

print("OpenFDA connection successful!")
print("Number of records:", len(data.get("results", [])))