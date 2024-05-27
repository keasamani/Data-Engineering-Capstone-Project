# Data-Engineering-Capstone-Project
## Hospital Data Ingestion Project
## Overview
This project aims to demonstrate a data ingestion pipeline for a hospital using fake data generated with the Faker library. 
The pipeline extracts data from various sources within the hospital, transforms it, and ingests it into a centralized database. 
The goal is to provide a daily overview of hospital operations to the medical director, enabling informed decision-making and monitoring of key metrics.

## Project Structure
- `hospital_data_ingestion.ipynb`: Jupyter Notebook file containing the project code.
- `README.md`: This file providing an overview of the project and instructions for getting started.
- `hospital.db`: SQLite database file where the fake data is ingested.

## Getting Started
To get started with this project, kindly follow these steps:

1. Clone the repository using this: git clone <repository_url>
2. Open the Jupyter Notebook file (`hospital_data_ingestion.ipynb`) in Jupyter Notebook or JupyterLab.
3. Execute each code cell to generate fake data, transform it, and ingest it into the database.

## Data Sources

1. **Patient Admissions and Discharges:**
   - Number of patients admitted to the hospital.
   - Number of patients discharged from the hospital.
   - Average length of stay for discharged patients.
   - Bed occupancy rate (percentage of occupied beds).

2. **Clinical Activities:**
   - Number of outpatient visits (clinic appointments, consultations).
   - Number of inpatient consultations (physician rounds, specialist consultations).
   - Number of surgeries performed (by type of surgery).
   - Number of emergency department visits.

3. **Medical Procedures and Treatments:**
   - Number of diagnostic tests performed (e.g., blood tests, imaging studies).
   - Number of medications administered (by type of medication).
   - Number of procedures performed (e.g., surgeries, endoscopies, catheterizations).

4. **Patient Safety and Quality Indicators:**
   - Incidence of patient falls or adverse events.
   - Hospital-acquired infections (e.g., bloodstream infections, surgical site infections).
   - Compliance with quality measures and patient safety protocols.

5. **Financial Data:**
    - Revenue generated from patient services (e.g., hospital charges, reimbursements).
    - Expenses incurred for hospital operations (e.g., salaries, supplies, utilities).
    - Accounts receivable and payable.

## Data Ingestion Pipeline
The data ingestion pipeline consists of the following steps:
1. Generation of fake data using the Faker library.
2. Transformation and enrichment of the fake data.
3. Ingestion of the transformed data into a centralized PostgreSQL database.

## Technologies Used
- Python (for data generation and transformation)
- Faker library (for generating fake data)
- PostgreSQL (for the centralized database)
- SQL (for data manipulation and ingestion)
- Jupyter Notebook or similar tools (for development and documentation)

## Contribution
Contributions to this project are welcome. You can contribute by:
- Opening an issue to report bugs or suggest improvements.
- Forking the repository, making changes, and opening a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
