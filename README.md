# 🩺 Smart Health Monitoring Band using IoT

An IoT-based Smart Health Monitoring System designed to monitor multiple patients in real time using MQTT communication, Raspberry Pi, ESP32, Google Sheets, and a Flask dashboard.

The project simulates health data for multiple patients, detects abnormal vital signs, generates alerts, and provides real-time visualization through a web interface.

---

# 📌 Features

- Real-time health monitoring for **10 simulated patients**
- Heart rate monitoring
- Body temperature monitoring
- Automatic abnormality detection
- MQTT-based communication
- Raspberry Pi as the central processing unit
- LCD alert system
- Google Sheets cloud logging
- Flask web dashboard
- Modular and scalable architecture

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| IoT Hardware | ESP32, Raspberry Pi |
| Communication | MQTT |
| Cloud | Google Sheets API, Google Apps Script |
| Backend | Flask |
| Dashboard | HTML, CSS |
| Display | 16×2 LCD |

---

# 🏗️ System Architecture

```
                 +----------------+
                 |    ESP32 Node  |
                 +-------+--------+
                         |
                         | MQTT
                         |
                +--------v--------+
                |   MQTT Broker   |
                +--------+--------+
                         |
                +--------v--------+
                | Raspberry Pi    |
                +---+-----+-------+
                    |     |
                    |     |
         +----------+     +-----------+
         |                          |
         |                          |
+--------v--------+        +--------v---------+
| Google Sheets   |        | 16x2 LCD Display |
+-----------------+        +------------------+

                    |
                    |
            +-------v-------+
            | Flask Dashboard|
            +---------------+
```

---

# 📊 Workflow

1. ESP32 simulates patient health readings.
2. Sensor values are published using MQTT.
3. Raspberry Pi subscribes to MQTT topics.
4. Patient data is analysed.
5. Abnormal values generate alerts.
6. Data is logged to Google Sheets.
7. LCD displays emergency notifications.
8. Flask dashboard visualizes patient health.

---

# 🚨 Alert Conditions

## Heart Rate

- Below 60 BPM
- Above 100 BPM

## Temperature

- Above 38°C

Whenever abnormal readings are detected:

- LCD displays warning
- Dashboard updates immediately
- Data is logged to Google Sheets

---

# 📈 Dashboard Features

- Live patient monitoring
- Temperature visualization
- Heart rate visualization
- Patient status
- Emergency alerts
- Historical readings

---

# ☁️ Google Sheets Integration

Patient health records are automatically stored in Google Sheets using Google Apps Script.

## Setup

1. Create a Google Sheet.
2. Open **Extensions → Apps Script**.
3. Copy the script from

```
google_sheets_script/code.gs
```

4. Deploy as Web App.
5. Copy the generated URL.
6. Paste the URL into the Raspberry Pi application.

---

# 📂 Project Structure

```
SIC-IoT-Project
│
├── esp32/
│
├── raspberry_pi/
│
├── dashboard/
│
├── google_sheets_script/
│
├── architecture.png
│
└── README.md
```

---

# 🚀 Future Enhancements

- Blood oxygen (SpO₂) monitoring
- Blood pressure integration
- SMS notifications
- Email alerts
- AI-based health prediction
- Mobile application
- Cloud deployment

---

# 👥 Team Contribution

This project was developed collaboratively as part of the Samsung Innovation Campus IoT Program.

Contributions included:

- IoT system design
- MQTT communication workflow
- Raspberry Pi integration
- Dashboard development
- Google Sheets integration
- Testing and debugging
- Documentation

---

# 📜 License

Developed for educational purposes under the Samsung Innovation Campus IoT Program.
