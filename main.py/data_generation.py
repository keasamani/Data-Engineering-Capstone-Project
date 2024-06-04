# Libraries used
import csv
from faker import Faker
import random

fake = Faker()

def generate_patient_record_log_data(num_rows):
    common_symptoms = [
        "Pain", "Fever", "Shortness of Breath", "Cough", "Nausea and Vomiting",
        "Dizziness or Vertigo", "Fatigue", "Chest Pain", "Weakness", "Abdominal Distress",
        "Rash", "Difficulty Urinating", "Headache", "Changes in Vision", "Bleeding", "Seizures",
        "Altered Mental Status"
    ]

    def generate_patient_id():
        return f"PT{random.randint(1, 1000):03d}"

    def generate_nurse_and_doctor_names():
        last_name = fake.last_name().replace("(", "").replace(")", "")  # Remove parenthesis from last name
        return f"Nr {last_name}", f"Dr. {last_name}"

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

def save_to_csv(data, file_name, columns):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)
    print(f"{file_name} csv file saved successfully!")

def main():
    # Generating patient record log data
    num_rows = 30
    patient_record_log_data = generate_patient_record_log_data(num_rows)
    patient_columns = ['Date', 'Patient ID/Name', 'Admission Time', 'Discharge Time', 'Diagnosis', 'Attending_Officer', 'is_admitted']
    save_to_csv(patient_record_log_data, "patient_record_log_data.csv", patient_columns)

    # Generating financial data
    departments = ['Emergency Department (ED)', 'Internal Medicine', 'Laboratory Services', 'Intensive Care Unit (ICU)', 'Pharmacy']
    department_data = [generate_department_data(department) for department in departments]
    financial_columns = ['Department Name', 'Number of Employees', 'Revenue', 'Expenses', 'Profitability (%)', 'Budget Allocations']
    save_to_csv(department_data, "financial_data_quarter.csv", financial_columns)

    # Generating hospital human resource status data
    generate_hr_status_csv()

    # Generating hospital performance data for the previous year
    generate_previous_year_statistics()

def generate_department_data(department_name):
    num_employees = random.randint(5, 50)
    revenue = random.uniform(20000, 200000)
    expenses = random.uniform(10000, 100000)
    profitability = (revenue - expenses) / revenue * 100
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

def generate_hr_status_csv():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    data = []
    for month in months:
        total_employees = random.randint(500, 1000)
        new_hires = random.randint(20, 50)
        terminations = random.randint(10, 30)
        turnover_rate = (terminations / total_employees) * 100 if total_employees != 0 else 0
        average_tenure = random.uniform(1, 5)
        overtime_hours = random.randint(1000, 2000)
        training_hours = random.randint(500, 1000)
        employee_satisfaction = random.randint(70, 90)
        data.append([month, total_employees, new_hires, terminations, turnover_rate, average_tenure, overtime_hours, training_hours, employee_satisfaction])

    save_to_csv(data, 'human_resource_status.csv', ['Month', 'Total Employees', 'New Hires', 'Terminations', 'Employee Turnover Rate (%)', 'Average Tenure (Years)', 'Overtime Hours', 'Training Hours', 'Employee Satisfaction Score'])

def generate_previous_year_statistics():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    data = []
    for month in months:
        patients_treated = random.randint(1000, 2000)
        surgeries_performed = random.randint(50, 150)
        revenue_generated = random.randint(50000, 150000)
        patient_satisfaction = random.randint(80, 95)
        data.append([month, patients_treated, surgeries_performed, revenue_generated, patient_satisfaction])

    save_to_csv(data, 'previous_year_statistics.csv', ['Month', 'Patients Treated', 'Surgeries Performed', 'Revenue Generated ($)', 'Patient Satisfaction (%)'])

if __name__ == "__main__":
    main()
