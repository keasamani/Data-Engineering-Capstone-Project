import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Function to create PostgreSQL connection
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="password",
            host="localhost",
            port="5432"
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return conn
    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)
        return None

# Function to create table in PostgreSQL
def create_table(conn, table_name, columns):
    try:
        with conn.cursor() as cur:
            create_table_query = sql.SQL(
                "CREATE TABLE IF NOT EXISTS {} ({});"
            ).format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(sql.Identifier(col) for col in columns)
            )
            cur.execute(create_table_query)
            print(f"Table {table_name} created successfully!")
    except psycopg2.Error as e:
        print("Error while creating table:", e)

# Function to insert data into PostgreSQL table
def insert_data(conn, table_name, data):
    try:
        with conn.cursor() as cur:
            insert_query = sql.SQL(
                "INSERT INTO {} VALUES ({}) ON CONFLICT DO NOTHING;"
            ).format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(sql.Placeholder() * len(data[0]))
            )
            cur.executemany(insert_query, data)
            print(f"Data inserted into table {table_name} successfully!")
    except psycopg2.Error as e:
        print("Error while inserting data:", e)

# Function to ingest data into PostgreSQL database
def ingest_data(conn, table_name, columns, data):
    create_table(conn, table_name, columns)
    insert_data(conn, table_name, data)

# PostgreSQL connection
conn = create_connection()

# If connection is successful, ingest data
if conn:
    try:
        # Ingest patient record log data
        ingest_data(conn, "patient_record_log", patient_columns, patient_record_log_data)

        # Ingest financial data
        ingest_data(conn, "financial_data", financial_columns, department_data)

        # Ingest human resource status data
        ingest_data(conn, "human_resource_status", ['Month', 'Total Employees', 'New Hires', 'Terminations', 'Employee Turnover Rate (%)', 'Average Tenure (Years)', 'Overtime Hours', 'Training Hours', 'Employee Satisfaction Score'], hr_status_data)

        # Ingest hospital performance data for the previous year
        ingest_data(conn, "previous_year_statistics", ['Month', 'Patients Treated', 'Surgeries Performed', 'Revenue Generated ($)', 'Patient Satisfaction (%)'], previous_year_statistics_data)
    finally:
        # Close the connection
        conn.close()
