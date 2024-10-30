import pandas as pd

def fetch_patient_data(patient_id):
    clinical_data_path = 'data/hiv_clinical_data.csv'
    
    # Load clinical data with debug
    clinical_data = pd.read_csv(clinical_data_path)
    print("Loaded Clinical Data:\n", clinical_data.head())  # Debugging line to check the data

    # Ensure no trailing/leading spaces and convert to lowercase
    clinical_data['Patient_ID'] = clinical_data['Patient_ID'].str.strip().str.lower()
    patient_id = patient_id.strip().lower()
    
    # Filter for the patient with the matching ID
    patient_data = clinical_data[clinical_data['Patient_ID'] == patient_id]
    
    if not patient_data.empty:
        # Convert patient data to dictionary for frontend
        patient_info = patient_data[['Patient_ID', 'Viral_Load', 'CD4_Count', 'Adherence_Level', 'Treatment_Response']].iloc[0].to_dict()
    else:
        print(f"No data found for Patient ID: {patient_id}")  # Debugging line
        patient_info = {"Message": "No patient data found"}
        
    return patient_info
