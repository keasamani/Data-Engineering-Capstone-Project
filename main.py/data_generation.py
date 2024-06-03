# Libraries used
import csv
from faker import Faker
import random
import pandas as pd

# Initializing faker
fake = Faker()

# Generating patient_record_log_data...

def generate_patient_record_log_data(num_rows):
    
    def generate_patient_id():
        return f"PT{random.randint(1, 1000):03d}"

    def generate_nurse_and_doctor_names():
        last_name = fake.last_name().replace("(", "").replace(")", "")  # Remove parenthesis from last name
        return f"Nr {last_name}", f"Dr. {last_name}"

    common_symptoms = [
        "Pain", "Fever", "Shortness of Breath", "Cough", "Nausea and Vomiting",
        "Dizziness or Vertigo", "Fatigue", "Chest Pain", "Weakness", "Abdominal Distress",
        "Rash", "Difficulty Urinating", "Headache", "Changes in Vision", "Bleeding", "Seizures",
        "Altered Mental Status"
    ]
    random.shuffle(common_symptoms)

    def shuffle_diagnosis():
        return random.sample(common_symptoms, random.randint(1, 3))

    data = []
    for _ in range(num_rows):
        date = fake.date_this_year()
        patient_id = generate_patient_id()
        admission_time, discharge_time = fake.time(), fake.time()
        diagnosis = shuffle_diagnosis()
        attending_officer = generate_nurse_and_doctor_names()
        is_admitted = random.choice(["Yes", "No"])
        data.append([date, patient_id, admission_time, discharge_time, diagnosis, attending_officer, is_admitted])

    return data

def save_to_csv(data, file_name):
    columns = ['Date', 'Patient ID/Name', 'Admission Time', 'Discharge Time', 'Diagnosis', 'Attending_Officer', 'is_admitted']
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)

if __name__ == "__main__":
    num_rows = 30
    patient_record_log_data = generate_patient_record_log_data(num_rows)
    csv_file = "patient_record_log_data.csv"
    save_to_csv(patient_record_log_data, csv_file)
    print("patient_record_log_data csv file saved successfully!")


# Generating financial data...

def generate_department_data(department_name):
    num_employees = random.randint(5, 50)
    revenue = random.uniform(20000, 200000)  # Random revenue between $20,000 and $200,000 per department
    expenses = random.uniform(10000, 100000)   # Random expenses between $10,000 and $100,000 per department
    profitability = (revenue - expenses) / revenue * 100  # Profitability as percentage
    budget_allocations = {
        'Salaries': random.uniform(5000, 50000),
        'Equipment': random.uniform(1000, 10000),
        'Supplies': random.uniform(1000, 20000),
        'Training': random.uniform(500, 5000)
    }
    
    return {
        'Department Name': department_name,
        'Number of Employees': num_employees,
        'Revenue': round(revenue, 2),
        'Expenses': round(expenses, 2),
        'Profitability (%)': round(profitability, 2),
        'Budget Allocations': (budget_allocations)
    }
departments = ['Emergency Department (ED)', 'Internal Medicine', 'Laboratory Services', 'Intensive Care Unit (ICU)', 'Pharmacy']
department_data = [generate_department_data(department) for department in departments]

columns = ['Department Name', 'Number of Employees', 'Revenue', 'Expenses', 'Profitability (%)', 'Budget Allocations']
csv_file = "financial_data_quarter.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    for department_info in department_data:
        writer.writerow([
            department_info['Department Name'],
            department_info['Number of Employees'],
            department_info['Revenue'],
            department_info['Expenses'],
            department_info['Profitability (%)'],
            department_info['Budget Allocations']
        ])

print("financial data per quarter csv file successfully saved!")


# Generating data for hospital human resource status...

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

data = []
for month in months:
    total_employees = random.randint(500, 1000)
    new_hires = random.randint(20, 50)
    terminations = random.randint(10, 30)
    turnover_rate = (terminations / total_employees) * 100 if total_employees != 0 else 0
    average_tenure = random.uniform(1, 5)  # Assuming average tenure in years
    overtime_hours = random.randint(1000, 2000)
    training_hours = random.randint(500, 1000)
    employee_satisfaction = random.randint(70, 90)
    data.append([month, total_employees, new_hires, terminations, turnover_rate, average_tenure, overtime_hours, training_hours, employee_satisfaction])

with open('human_resource_status.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Month', 'Total Employees', 'New Hires', 'Terminations', 'Employee Turnover Rate (%)', 'Average Tenure (Years)', 'Overtime Hours', 'Training Hours', 'Employee Satisfaction Score'])
    writer.writerows(data)

print("human_resource_status_data csv file successfully saved")
    

# Generating data for hospital performance in the previous year...

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

data = []
for month in months:
    patients_treated = random.randint(1000, 2000)
    surgeries_performed = random.randint(50, 150)
    revenue_generated = random.randint(50000, 150000)
    patient_satisfaction = random.randint(80, 95)
    data.append([month, patients_treated, surgeries_performed, revenue_generated, patient_satisfaction])

with open('previous_year_statistics.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Month', 'Patients Treated', 'Surgeries Performed', 'Revenue Generated ($)', 'Patient Satisfaction (%)'])
    writer.writerows(data)

print("statistics data for the previous year successfully saved!")
