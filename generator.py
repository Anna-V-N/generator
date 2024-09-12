import random
from openpyxl import Workbook
from datetime import datetime, timedelta

def generate_large_xlsx(file_name, num_records):
    start_date = datetime(2023, 1, 1)  #srart date
    end_date = datetime(2024, 12, 31)  #end date

    #creating Excel file
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["ID", "Date", "Value"])  #headers

    for i in range(num_records):
        record_id = i + 1
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        random_value = round(random.uniform(0.1, 100.0), 2)
        #creating a line entry in Excel
        sheet.append([record_id, random_date.strftime("%Y-%m-%d"), random_value])

    #saving Excel file
    workbook.save(file_name)

#call the function for file creation
generate_large_xlsx("large_file.xlsx", 100000)  #generating file with 100000 records

