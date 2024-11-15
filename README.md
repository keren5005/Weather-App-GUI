Here’s an updated **README.md** for your enhanced **Weather App GUI** project:

---

# 🌦 Weather App GUI

A Python-based GUI application that fetches and displays weather information for a specific country and city. The application allows users to choose between two data sources:
1. **Time and Date Scraper**: Uses web scraping to fetch weather details from [Time and Date](https://www.timeanddate.com/weather/).
2. **MetaWeather API**: Fetches weather data from the [MetaWeather API](https://www.metaweather.com/api/).

The app is built with `tkinter` for a user-friendly graphical interface.

---

## 🚀 Features

- 🌍 **Dynamic Input**: Users can input any country and city to fetch weather details.
- 🌡️ **Multiple Data Sources**: Choose between a web scraper or the MetaWeather API.
- ⚠️ **Error Handling**: Handles invalid inputs and network-related errors gracefully.
- 🖥️ **Interactive GUI**: Built with `tkinter` for a clean and responsive user interface.

---

## 🖼️ Screenshots

### Main Interface
![Main GUI](/home_screen.png)

### Weather Display
![Weather Display](/run_screen.png)

---

## 🛠️ Technologies Used

- **Python**: The core programming language.
- **tkinter**: For building the graphical user interface (GUI).
- **BeautifulSoup**: For web scraping weather data.
- **Requests**: For making HTTP requests to fetch API and web data.

---

## 🧑‍💻 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-app-gui.git
cd weather-app-gui
```

### 2. Install Dependencies
Make sure you have Python installed. Then, install the required libraries:
```bash
pip install requests beautifulsoup4
```

### 3. Run the Application
Run the `weather_gui.py` file:
```bash
python weather_gui.py
```

### 4. Use the GUI
- Enter the **country** name (e.g., `israel`).
- Enter the **city** name (e.g., `tel-aviv`).
- Choose a data source:
  - **Fetch from Scraper**: Uses web scraping.
  - **Fetch from MetaWeather API**: Uses MetaWeather.

---

## 📋 Example Outputs

### Example 1: Using Time and Date Scraper
**Input**:
```
Country: israel
City: tel-aviv
```

**Output**:
```
Weather in Tel-Aviv, Israel:
Temperature: 25°C
Condition: Clear sky
```

---

### Example 2: Using MetaWeather API
**Input**:
```
City: tel aviv
```

**Output**:
```
Weather in Tel Aviv:
Temperature: 24.5°C
Condition: Clear
```

---

## 📦 Project Structure

```
weather-app-gui/
├── weather_gui.py          # Main Python file to run the GUI
├── weather_scraper.py      # Contains scraper and API functions
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

## 🤝 Contributions

Contributions are welcome! If you'd like to add features or improve the app, feel free to:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request with your changes.

---

## 🐛 Known Issues

- The scraper relies on the structure of the source website. If the website changes, the scraper may break.
- MetaWeather API availability is subject to their uptime.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- Weather data is sourced from [Time and Date](https://www.timeanddate.com/weather/) and the [MetaWeather API](https://www.metaweather.com/api/).
- Built with love using Python. ❤️

