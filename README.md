# 🌦️ Weather Info Mini Project

A Python-based mini project that fetches **real-time weather information** for any city using the **OpenWeatherMap API**.
This project demonstrates how Python can interact with **web APIs**, handle **JSON data**, and display meaningful output.

---

## 📌 Project Overview

* **Course:** Python for Computational Problem Solving
* **Course Code:** UE25CS151A
* **University:** PES University
* **Project Type:** Mini Project
* **Domain:** API Integration / Real-Time Data Fetching

---

## 🎯 Objective

* To understand and implement **API-based data retrieval**
* To learn **HTTP requests** using Python
* To parse and extract data from **JSON responses**
* To display real-time weather details in a user-friendly format

---

## ⚙️ Technologies Used

| Tool / Technology  | Description                      |
| ------------------ | -------------------------------- |
| Python             | Core programming language        |
| OpenWeatherMap API | Source of real-time weather data |
| `requests` library | To send HTTP requests            |
| JSON               | Data exchange format             |
| Visual Studio Code | Development environment          |
| Git & GitHub       | Version control and code hosting |

---

## 📂 Project Structure

```
weather-info-mini-project/
│
├── weather_info.py     # Main Python program
├── README.md           # Project documentation
```

---

## 🚀 How the Project Works

1. The user enters a **city name**
2. The program sends a request to the **OpenWeatherMap API**
3. The API returns weather data in **JSON format**
4. The program extracts:

   * Temperature
   * Weather condition
   * Humidity
   * Wind speed
5. The information is displayed neatly in the terminal

---

## 🧠 Key Concepts Used

* REST APIs
* HTTP GET requests
* API authentication using API keys
* JSON parsing
* Conditional statements (`if-else`)
* Functions and modular code
* Error handling

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rohanbuilds-ai/weather-info-mini-project.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd weather-info-mini-project
```

### 3️⃣ Install Required Library

```bash
pip install requests
```

### 4️⃣ Run the Program

```bash
python weather_info.py
```

---

## 🧪 Sample Input / Output

### Input

```
Enter city name: Bengaluru
```

### Output

```
Weather Information for Bengaluru
Temperature: 28°C
Weather: Clear sky
Humidity: 45%
Wind Speed: 3.5 m/s
```

---

## ❗ Error Handling

* Invalid city names are detected and handled
* Incorrect or inactive API keys are identified
* User-friendly error messages are displayed

---

## 🔍 Challenges Faced

* Understanding API request and response flow
* Parsing nested JSON data
* Handling API errors and invalid inputs
* Managing Git merge conflicts during GitHub push

---

## 🔮 Future Enhancements

* Add 5-day weather forecast
* Display weather icons
* Build a GUI using Tkinter
* Save weather reports to a file
* Support multiple cities in one run

---

## 📚 Learning Outcomes

* Practical understanding of APIs
* Real-world Python application development
* JSON data handling
* Git and GitHub workflow experience

---

## 📖 References

* OpenWeatherMap API Documentation
  [https://openweathermap.org/api](https://openweathermap.org/api)
* Python Requests Library
  [https://docs.python-requests.org](https://docs.python-requests.org)
* Python Official Documentation
  [https://www.python.org](https://www.python.org)

---

## 👤 Author

**Rohan K**
PES University
B.Tech CSE (AIML)
