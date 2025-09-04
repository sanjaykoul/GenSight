import pandas as pd
from datetime import datetime

def load_excel_data(file_path):
    excel_data = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')
    data_by_date = {}
    for sheet_name, df in excel_data.items():
        try:
            date = datetime.strptime(sheet_name.strip(), "%d-%m-%Y")
            df['Date'] = date
            data_by_date[date] = df
        except ValueError:
            continue
    combined_df = pd.concat(data_by_date.values(), ignore_index=True)
    return combined_df
