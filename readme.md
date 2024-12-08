# Real-Time Air Quality Monitoring System

This project demonstrates a real-time pipeline for ingesting, processing, and storing air quality sensor data.

## Features
- **Data Ingestion**: Simulates real-time air quality sensor data generation.
- **Data Processing**: Filters and transforms data based on PM2.5 levels.
- **Data Storage**: Stores processed data into an SQLite database.

## Technologies Used
- **Python**: Core programming language.
- **SQLite**: Lightweight database for data storage.
- **Threading**: Enables real-time operation.

## How It Works
1. **Ingestion**: Simulated air quality data is generated every 5 seconds.
2. **Processing**: Data is processed to add a "status" field based on PM2.5 levels.
3. **Storage**: Processed data is stored in an SQLite database (`air_quality_data.db`).

## Setup and Usage
### Prerequisites
- Python 3.7 or higher installed.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
