import requests

url = "https://api.opendental.com/api/v1/patients"

headers = {
    "Authorization": "ODFHIR NFF6i0KrXrxDkZHt/VzkmZEaUWOjnQX2z",
    "Content-Type": "application/json"
}

last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
birthdate = input("Enter birthdate (YYYY-MM-DD): ")
address = input("Enter address: ")

data = {
    "Lname": last_name,
    "Fname": first_name,
    "Birthdate": birthdate,
    "Address": address
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    # The record was successfully created
    print("Record created")
else:
    # Handle the error
    print("Request failed with status code:", response.status_code)
