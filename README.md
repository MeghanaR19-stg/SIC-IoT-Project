# SIC-IoT-Project
Smart Health Monitoring Band using IoT (ESP32 + Raspberry Pi + MQTT + Google Sheets + LCD)

## Components
- ESP32
- Raspberry Pi
- MQTT Broker
- Google Sheets
- 16x2 LCD Display
- Flask Web Dashboard

## Features
- Simulates 10 patients
- Detects abnormal heart rate
- Detects abnormal temperature
- Shows alerts on LCD
- Stores data in Google Sheets
- Web dashboard for monitoring

## Architecture

ESP32 → MQTT Broker → Raspberry Pi → Google Sheets + LCD + Web Dashboad

![Architecture](architecture.png)

## Google Sheets Integration

The system stores patient health data in Google Sheets using Google Apps Script.

Steps:

1. Open Google Sheets
2. Click Extensions → Apps Script
3. Paste the script from /google_sheets_script/code.gs
4. Deploy as Web App
5. Copy the generated URL
6. Use the URL in the Raspberry Pi program

## Features

• Real-time patient monitoring  
• IoT communication using MQTT  
• Health data stored in Google Sheets  
• LCD alert system  
• Web dashboard monitoring  


