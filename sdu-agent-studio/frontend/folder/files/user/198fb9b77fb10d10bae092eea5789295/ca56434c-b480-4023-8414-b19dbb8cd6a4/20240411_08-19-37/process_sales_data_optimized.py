# filename: process_sales_data_optimized.py  
import os  
import pandas as pd  
from dotenv import load_dotenv  
import requests  
import time  
import logging  
  
# Setup logging  
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  
  
def load_api_credentials():  
    load_dotenv()  
    api_key = os.getenv("GROQ_API_KEY")  
    #api_url = os.getenv("GROQ_API_URL")  # Dynamically load the API URL  
    return api_key, api_url  
  
def process_csv_file(file_path):  
    try:  
        return pd.read_csv(file_path)  
    except Exception as e:  
        logging.error(f"Error reading {file_path}: {e}")  
        return pd.DataFrame()  # Return an empty DataFrame on error  
  
def make_api_call(api_key, api_url, data):  
    try:  
        headers = {"Authorization": f"Bearer {api_key}"}  
        response = requests.post(api_url, json=data, headers=headers)  
        response.raise_for_status()  # This will raise an error for 4XX and 5XX responses  
        return response.json()  
    except requests.exceptions.RequestException as e:  
        logging.error(f"API call failed: {e}")  
        return None  
  
def process_directory(directory_path, api_key, api_url):  
    for file_name in os.listdir(directory_path):  
        if file_name.endswith('.csv'):  
            file_path = os.path.join(directory_path, file_name)  
            sales_data = process_csv_file(file_path)  
              
            # Example: Process each row. Consider batching if supported by the API.  
            for index, row in sales_data.iterrows():  
                response = make_api_call(api_key, api_url, row.to_dict())  
                if response:  
                    logging.info(f"API call successful for row {index}")  
                time.sleep(1)  # Simple delay to avoid hitting rate limits  
  
def main():  
    directory_path = input("Enter the directory path of CSV files: ")  
    api_key, api_url = load_api_credentials()  
      
    if not api_key or not api_url:  
        logging.error("API key or URL not found. Please check your .env file.")  
        return  
      
    process_directory(directory_path, api_key, api_url)  
  
if __name__ == "__main__":  
    main()  