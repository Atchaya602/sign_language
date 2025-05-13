# sign_language


1. 🤟 **Sign Language Detection using Transformers + OpenCV**
2. 🌐 **Campus Network Traffic Analyzer using Scapy**


---


# 🔍 AI & Network Analysis Projects

This repository contains two Python-based mini-projects:
1. 🤟 **Sign Language Detection** – A real-time sign language recognizer using Hugging Face Transformers and OpenCV.
2. 🌐 **Campus Network Analyzer** – A tool to analyze `.pcap` files and extract insights from captured network traffic.

---

## 📁 Project 1: Sign Language Detection

This project uses a pre-trained image classification model from Hugging Face to detect hand gestures for sign language in real time using a webcam.

### 🛠 Tech Stack
- Python
- Transformers (`RavenOnur/Sign-Language`)
- OpenCV
- PIL (Pillow)

### 🚀 How to Run
```bash
pip install transformers opencv-python pillow
````

```bash
python sign_language_live.py
```

### 📸 Sample Output

Real-time video stream showing gesture prediction:

```
A: 0.98
```

### 📜 Description

* Uses `pipeline("image-classification", model="RavenOnur/Sign-Language")` to classify live frames.
* Displays the most probable sign label with confidence score on the webcam feed.
* Press **'q'** to quit the app.

---

## 📁 Project 2: Campus Network Traffic Analyzer

This script reads and analyzes network traffic from `.pcap` files and outputs:

* The top 5 most active IP addresses.
* The protocol distribution (TCP, UDP, etc.).

### 🛠 Tech Stack

* Python
* Scapy

### 🚀 How to Run

```bash
pip install scapy
```

```bash
python analyze_traffic.py
```

Make sure to replace this line with your actual `.pcap` file:

```python
pcap_file = "network_traffic.pcap"
```


## 🧰 Folder Structure

```
project-root/
├── sign_language_live.py        # Real-time sign language detector
├── analyze_traffic.py           # Network traffic analyzer script
├── network_traffic.pcap         # Example PCAP file (optional)
├── README.md                    # This file
├── requirements.txt             # Dependencies
└── .gitignore                   # Files to exclude from version control
```





