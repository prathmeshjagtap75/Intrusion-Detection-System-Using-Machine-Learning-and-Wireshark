#  Intrusion Detection System Using Machine Learning and Wireshark

> A Machine Learning-based Intrusion Detection System (IDS) that captures real network traffic using **Wireshark**, extracts packet features, and classifies network activity as **Normal** or **Suspicious** using a **Random Forest** classifier. Developed on **Kali Linux** using Python and Scikit-learn.

---

#  Overview

Intrusion Detection Systems (IDS) play a critical role in modern cybersecurity by monitoring network traffic and identifying suspicious activities. Traditional IDS solutions rely on signature-based detection, whereas Machine Learning-based IDS solutions learn traffic patterns and can identify anomalies from captured network data.

This project demonstrates a complete IDS workflow—from capturing packets with **Wireshark** to training and evaluating a Machine Learning model using **Python** and **Scikit-learn**.

---

#  Objectives

* Capture real-time network traffic using Wireshark.
* Extract meaningful packet features from PCAP files.
* Build a structured dataset for machine learning.
* Train a Random Forest classifier.
* Classify network traffic as **Normal** or **Suspicious**.
* Evaluate model performance using standard machine learning metrics.

---

#  Features

*  Live packet capture using Wireshark
*  PCAP file processing using PyShark
*  Automatic CSV dataset generation
*  Random Forest-based intrusion detection
*  Model evaluation with Accuracy Score
*  Confusion Matrix generation
*  Feature Importance visualization
*  Command-line implementation
*  Developed and tested on Kali Linux

---

#  Technology Stack

| Category             | Technology   |
| -------------------- | ------------ |
| Programming Language | Python 3     |
| Operating System     | Kali Linux   |
| Packet Capture       | Wireshark    |
| Packet Parsing       | PyShark      |
| Machine Learning     | Scikit-learn |
| Data Processing      | Pandas       |
| Numerical Computing  | NumPy        |
| Visualization        | Matplotlib   |

---

#  Installation

Clone the repository

```bash
git clone https://github.com/your-username/Intrusion-Detection-System-Using-Machine-Learning-and-Wireshark.git
```

Navigate to the project directory

```bash
cd Intrusion-Detection-System-Using-Machine-Learning-and-Wireshark
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

#  Workflow

### Step 1 – Capture Network Traffic

Capture live network traffic using Wireshark and save it as a **PCAP** file.

---

### Step 2 – Extract Packet Features

Run the packet extraction script:

```bash
python3 ids.py
```

This extracts packet details such as:

* Source IP Address
* Destination IP Address
* Protocol
* Packet Length

and stores them in:

```text
network_data.csv
```

---

### Step 3 – Train the Machine Learning Model

Execute:

```bash
python3 train_model.py
```

The script performs:

* Data preprocessing
* Feature encoding
* Train-test split
* Random Forest training
* Traffic prediction
* Performance evaluation

---

### Step 4 – Analyze Results

The model generates:

* Accuracy Score
* Prediction Output
* Confusion Matrix
* Classification Report
* Feature Importance Graph

---

#  Results

The IDS successfully demonstrates:

* Live packet capture
* Dataset generation from network traffic
* Machine Learning model training
* Network traffic classification
* Performance evaluation
* Feature visualization

---

#  Model Evaluation

Evaluation metrics used:

* Accuracy Score
* Confusion Matrix
* Precision
* Recall
* F1-Score
* Feature Importance

---

#  Limitations

The dataset used during testing consisted primarily of **ICMP packets with identical packet lengths**. Due to the lack of diversity in the captured traffic, the Random Forest model assigned **feature importance values close to 0.0**.

This is an expected outcome because Machine Learning models require varied data to accurately determine feature significance.

For improved results, future datasets should include:

* TCP Traffic
* UDP Traffic
* DNS Requests
* HTTP/HTTPS Traffic
* FTP Traffic
* Mixed benign and suspicious traffic
* Larger packet size variations

---

#  Skills Acquired

* Machine Learning for Cybersecurity
* Network Traffic Analysis
* Packet Inspection
* Feature Engineering
* Data Preprocessing
* Random Forest Classification
* Model Evaluation
* Wireshark Packet Analysis
* Cybersecurity Fundamentals
* Python Programming

---
# 📄 Requirements

```text
pandas
numpy
scikit-learn
matplotlib
pyshark
```

---
