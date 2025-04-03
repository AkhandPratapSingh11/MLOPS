import requests

# URL of the raw CSV file
url = "https://raw.githubusercontent.com/vikashishere/YT-MLOPS-Complete-ML-Pipeline/main/experiments/spam.csv"

# File path where you want to save it
csv_filename = "spam.csv"

# Download and save the CSV file
response = requests.get(url)
if response.status_code == 200:
    with open(csv_filename, "wb") as file:
        file.write(response.content)
    print(f"CSV file downloaded successfully: {csv_filename}")
else:
    print(f"Failed to download CSV. HTTP Status Code: {response.status_code}")
