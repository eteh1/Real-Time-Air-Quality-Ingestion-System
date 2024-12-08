import random
import time
import sqlite3
import requests
import threading
from datetime import datetime

# Mock sensor data ingestion (you can replace this with real sensor data API)
def generate_air_quality_data():
    """Simulate real-time air quality sensor data."""
    return {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'sensor_id': random.randint(1, 10),  # Simulated sensor ID
        'pm2_5': round(random.uniform(0, 100), 2),  # PM2.5 in µg/m³
        'pm10': round(random.uniform(0, 150), 2),  # PM10 in µg/m³
        'temperature': round(random.uniform(15, 35), 2),  # Temperature in Celsius
        'humidity': round(random.uniform(30, 90), 2)  # Humidity in percentage
    }

# Data Ingestion (simulate real-time data fetching every 5 seconds)
def ingest_air_quality_data():
    """Fetch or simulate real-time air quality data."""
    data = generate_air_quality_data()
    print(f"Received data: {data}")
    return data

# Data Processing (e.g., basic filtering and transformation)
def process_data(raw_data):
    """Process and clean the incoming air quality data."""
    # Example transformations (e.g., filter data if PM2.5 exceeds a threshold)
    if raw_data['pm2_5'] > 50:  # Example filter
        raw_data['status'] = 'Unhealthy'
    else:
        raw_data['status'] = 'Good'
    
    return raw_data

# Data Storage (store the processed data into a SQLite database)
def store_data(processed_data):
    """Store the processed air quality data into an SQLite database."""
    conn = sqlite3.connect('air_quality_data.db')
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS air_quality (
            timestamp TEXT,
            sensor_id INTEGER,
            pm2_5 REAL,
            pm10 REAL,
            temperature REAL,
            humidity REAL,
            status TEXT
        )
    ''')

    # Insert the processed data
    cursor.execute('''
        INSERT INTO air_quality (timestamp, sensor_id, pm2_5, pm10, temperature, humidity, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (processed_data['timestamp'], processed_data['sensor_id'], processed_data['pm2_5'],
          processed_data['pm10'], processed_data['temperature'], processed_data['humidity'],
          processed_data['status']))

    conn.commit()
    conn.close()

# Real-Time Ingestion and Processing Loop
def real_time_pipeline():
    """Simulate a real-time pipeline for ingesting, processing, and storing air quality data."""
    while True:
        # Ingest data
        raw_data = ingest_air_quality_data()
        
        # Process the data
        processed_data = process_data(raw_data)
        
        # Store the data in the database
        store_data(processed_data)
        
        time.sleep(5)  # Wait 5 seconds before fetching the next data

# Run the pipeline in a separate thread for real-time operation
def start_real_time_ingestion():
    """Start the real-time ingestion process in a separate thread."""
    ingestion_thread = threading.Thread(target=real_time_pipeline)
    ingestion_thread.daemon = True  # Daemon thread will stop when the main program ends
    ingestion_thread.start()

if __name__ == '__main__':
    # Start the real-time air quality ingestion system
    print("Starting real-time air quality ingestion system...")
    start_real_time_ingestion()
    
    # Run the main program indefinitely (simulating real-time operation)
    try:
        while True:
            # In a real application, you would display or analyze the data here
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down real-time ingestion system.")
