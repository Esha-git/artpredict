import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# 1. Define the scope and credentials file path
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("update_form.json", scope)

# 2. Authenticate with Google Sheets API
client = gspread.authorize(credentials)

# 3. Open the Google Sheet by name
sheet = client.open("Contact Information (Responses)")  # Make sure to use your actual Google Sheet name

# 4. Select the specific worksheet (tab) where form responses are stored
worksheet = sheet.worksheet("Form Responses 1")  # This is usually the default worksheet created by Google Form

# 5. Get all data from the worksheet
form_data = worksheet.get_all_records()

# 6. Convert the data to a DataFrame (optional but useful for easier manipulation)
df = pd.DataFrame(form_data)

# 7. Save this data into a CSV (or update your existing CSV 'new_patient_data.csv')
df.to_csv('data/new_patient_data.csv', index=False)

# 8. (Optional) Print the retrieved data
print(df)
