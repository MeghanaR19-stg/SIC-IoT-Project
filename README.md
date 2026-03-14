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


