import requests

url = "https://api.opendental.com/api/v1/patients"

headers = {
    "Authorization": "ODFHIR NFF6i0KrXrxDkZHt/VzkmZEaUWOjnQX2z",
    "Content-Type": "application/json"
}

PatNum = input("Enter patient number: ")

response = requests.get(url.format(PatNum=PatNum), headers=headers)

if response.status_code == 200:
    # The record was successfully retrieved
    patient_list = response.json()
    if len(patient_list) > 0:
        patient = patient_list[0]
        print("First Name:", patient["FName"])
        print("Last Name:", patient["LName"])
        print("Address:", patient["Address"])
    else:
        print("No patient found with that number.")
else:
    # Handle the error
    print("Request failed with status code:", response.status_code)