import requests
import openpyxl

# Define the OpenDental API endpoint
endpoint = "https://api.opendental.com/api/v1/patients"

# Set the API headers, including the authorization header
headers = {
    "Authorization": "ODFHIR NFF6i0KrXrxDkZHt/VzkmZEaUWOjnQX2z"
}

# Make the API request to retrieve patient data
response = requests.get(endpoint, headers=headers)

# Check if the API request was successful
if response.status_code == 200:
    # Parse the patient data from the API response
    patient_data = response.json()

    # Create a new Excel workbook
    workbook = openpyxl.Workbook()

    # Create a new worksheet
    worksheet = workbook.active

    # Write the header row to the worksheet
    worksheet.append(["Patient ID", "Patient Name", "Patient Date of Birth", "Patient Address"])

    # Loop through each patient in the patient data
    for patient in patient_data:
        # Write the patient data to the worksheet
        worksheet.append([patient["PatNum"], patient["FName"], patient["Birthdate"], patient["Address"]])

    # Save the Excel workbook to disk
    workbook.save("patient_records.xlsx")
else:
    # Handle the error
    print("Error retrieving patient data:", response.text)
