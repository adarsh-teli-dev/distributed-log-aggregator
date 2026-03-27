# Distributed Log Aggregation System

## 📌 Overview
This project implements a distributed system where multiple clients generate logs and send them to a centralized server using TCP sockets with TLS encryption.

The server aggregates logs, stores them centrally, and displays them in real-time using a dashboard.

---

## 🏗️ Architecture

Clients → TLS TCP → Log Server → Log Storage → Dashboard

---

## ⚙️ Features

- Multi-client system
- TCP socket communication
- TLS/SSL secure communication
- Multithreaded server
- Load testing with multiple clients
- Real-time dashboard (Flask)
- Performance monitoring (throughput, latency, CPU, memory)

---

## 🔐 Security

TLS encryption is implemented using Python's `ssl` module to ensure secure communication between client and server.

---

## 📊 Performance Evaluation

- Tested with multiple concurrent clients
- Measured throughput (logs/sec)
- Measured latency (round-trip time)
- Monitored CPU and memory usage

---

## 🔧 Optimization & Fixes

- Implemented multithreading for concurrency
- Added exception handling for stability
- Handled client disconnections
- Managed SSL connection issues

---

## 🚀 How to Run

### 1. Start Server
python server.py

### 2. Run Clients
python load_test.py

### 3. Start Dashboard
python dashboard.py

### 4. Open Browser
http://127.0.0.1:5000

---

## 🧑‍🤝‍🧑 Team

- Adarsh
- [Teammate Names]

---

## 💡 Conclusion

This project demonstrates distributed system concepts, secure communication, and real-time log monitoring similar to industry logging systems.
