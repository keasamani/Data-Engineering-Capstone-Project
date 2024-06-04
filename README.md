# Data-Engineering-Capstone-Project(@Trestle Academy)
## Hospital Data Ingestion Project
## Overview
This project aims to demonstrate a data ingestion pipeline for a hospital using data generated with the Faker library. 
This pipeline extracts data from various sources within the hospital and ingests it into a centralized database. 
The goal is to provide a daily overview of hospital operations to the medical director, enabling informed decision-making and monitoring of key metrics for effective hospital management.

## Getting Started

To get started with this project, kindly follow these steps:

1. Clone the repository using this: git clone <repository_url>
2. Open the main python file (`main.py`) in VS CODE or any IDE Environment
3. Execute each code cell to generate fake data and ingest it into your database.

## Data sources

1. Financial Data (Quarterly)- This dataset contains quarterly financial information, including revenue, expenses, profits, and other relevant financial metrics.

2. Human Resource Status - This dataset provides information on the status and demographics of our human resources,  including total employee count, new hires, terminations, employee turnover rate, average tenure, overtime hours, training hours, and employee satisfaction scores

3. Patient Record Log - Description: This dataset comprises logs of patient records, including details such as the date of admission, patient ID or name, admission time, discharge time, diagnosis, attending officer, and a binary indicator specifying whether the patient is admitted or not

4. Previous Year Statistics - This dataset contains statistical information from the previous year, encompassing various aspects such as financial performance, operational metrics, and any other relevant statistical data.

#### Caution: This dataset has been generated using the Faker library due to the unavailability of real hospital data. It is synthetic and does not represent real patient information. It is intended for demonstration and testing purposes only.

## Data Generation Pipeline
The data generation process employs the Faker library to create synthetic data sets.

Step 1: Import Required Libraries.

Step 2: Initialize Faker.

Step 3: Generate Patient Record Log Data and save data to csv.

Step 4: Generate Data for Hospital Human Resource Status and save data to csv

Step 5: Generate Financial Data per Quarter and save data to csv.

Step 6: Generate Data for Hospital Performance in the Previous Year and save data to csv.

## Data Ingestion Pipeline
The data ingestion pipeline facilitates the seamless flow of data from its generation to storage, laying the groundwork for subsequent analysis and insights generation.

Following the generation of synthetic data, the next crucial step is its ingestion into a centralized PostgreSQL database. This centralized repository serves as a core storage area where the generated data is stored for further processing, analysis, and integration with other datasets.

Step 1: Set Up Database Connection.

NB: Ensure that you have PostgreSQL installed and running on your local machine or server.

Step 2: Define Data Reading and Insertion Functions.

Step 3: Establish Connection to PostgreSQL Database.

Step 4: Define File Paths and Read CSV Files.

Step 5: Handle Schema Evolution (Optional).

Step 6: Insert Data into PostgreSQL Database.

Step 7: Close Database Connection.

## Technologies Used
- Python (for data generation and transformation)
- Faker library (for generating fake data)
- PostgreSQL (for the centralized database)
- Jupyter Notebook (for development and documentation)

## Contribution
Contributions to this project are welcome. You can contribute by:
- Opening an issue to report bugs or suggest improvements.
- Forking the repository, making changes, and opening a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
