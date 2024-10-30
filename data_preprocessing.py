import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
import os

# Function to preprocess HIV clinical data
def preprocess_clinical_data(file_path):
    print(f"Loading clinical data from: {file_path}")
    
    # Load the dataset
    clinical_data = pd.read_csv(file_path)

    # Print the initial info for debugging
    print("Initial clinical data info:")
    print(clinical_data.info())

    # Handling missing values for Treatment_Response
    imputer = SimpleImputer(strategy='most_frequent')
    clinical_data['Treatment_Response'] = imputer.fit_transform(clinical_data[['Treatment_Response']])

    # Handling missing values for Viral_Load and CD4_Count
    imputer = SimpleImputer(strategy='mean')
    clinical_data['Viral_Load'] = imputer.fit_transform(clinical_data[['Viral_Load']])
    clinical_data['CD4_Count'] = imputer.fit_transform(clinical_data[['CD4_Count']])

    # Normalize continuous features (Viral Load, CD4 Count)
    scaler = StandardScaler()
    clinical_data[['Viral_Load', 'CD4_Count']] = scaler.fit_transform(clinical_data[['Viral_Load', 'CD4_Count']])

    # Encode categorical variables (Adherence_Level: numeric -> categories)
    # Assuming Adherence_Level is categorical, if it's numeric, you can skip this part
    label_encoder = LabelEncoder()
    clinical_data['Treatment_Response'] = label_encoder.fit_transform(clinical_data['Treatment_Response'])

    # Save the preprocessed clinical data
    output_path = 'preprocessed_files/preprocessed_clinical_data.csv'
    clinical_data.to_csv(output_path, index=False)
    print(f"Preprocessed clinical data saved to: {output_path}")

    return clinical_data

# Main execution
if __name__ == "__main__":
    # Ensure the necessary directories exist
    os.makedirs('preprocessed_files', exist_ok=True)

    # File paths
    clinical_data_path = 'data/hiv_clinical_data.csv'

    # Preprocess the data
    preprocess_clinical_data(clinical_data_path)
