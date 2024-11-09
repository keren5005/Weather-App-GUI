import tkinter as tk
from weather_scraper import get_weather, get_weather_from_metaweather

# def show_weather():
#     country = input("Enter the country name: ").strip() 
#     city = input("Enter the city name: ").strip()  
#     temperature, condition = get_weather(country,city)    
    
#     # Display the GUI
#     window = tk.Tk()
#     window.title(f"Weather in {city.title()}")
#     window.geometry("400x300")  # Set window size
#     window.configure(bg="#f0f8ff")  # Set background color

#     # Add a title label
#     tk.Label(
#         window, 
#         text=f"Weather in {city.title()}", 
#         font=("Helvetica", 20, "bold"), 
#         bg="#f0f8ff", 
#         fg="#333333"
#     ).pack(pady=20)

#     # Add temperature and condition labels
#     tk.Label(
#         window, 
#         text=f"Temperature: {temperature}", 
#         font=("Arial", 16), 
#         bg="#f0f8ff", 
#         fg="#ff4500"
#     ).pack(pady=10)

#     tk.Label(
#         window, 
#         text=f"Condition: {condition}", 
#         font=("Arial", 16), 
#         bg="#f0f8ff", 
#         fg="#1e90ff"
#     ).pack(pady=10)

#     # Add a close button with styling
#     tk.Button(
#         window, 
#         text="Close", 
#         command=window.destroy, 
#         font=("Arial", 14), 
#         bg="#ffdddd", 
#         fg="#333333", 
#         relief="raised"
#     ).pack(pady=20)

#     # Run the GUI event loop
#     window.mainloop()

# # Call the function
# show_weather()

def show_weather():
    def fetch_and_display_weather(source):
        country = country_entry.get().strip()
        city = city_entry.get().strip()

        if not city:
            result_label.config(text="Please enter a city name.")
            return

        if source == "scraper":
            temperature, condition = get_weather(country, city)
        elif source == "metaweather":
            temperature, condition = get_weather_from_metaweather(city)
        else:
            temperature, condition = "N/A", "N/A"

        # Update the GUI with the results
        result_label.config(
            text=f"Weather in {city.title()}, {country.title()}:\n"
                 f"Temperature: {temperature}\n"
                 f"Condition: {condition}"
        )

    # Create the main GUI window
    window = tk.Tk()
    window.title("Weather App")
    window.geometry("400x400")
    window.configure(bg="#f0f8ff")

    # Input fields for country and city
    tk.Label(window, text="Country:", bg="#f0f8ff").pack(pady=5)
    country_entry = tk.Entry(window, width=30)
    country_entry.pack(pady=5)

    tk.Label(window, text="City:", bg="#f0f8ff").pack(pady=5)
    city_entry = tk.Entry(window, width=30)
    city_entry.pack(pady=5)

    # Buttons for choosing data source
    tk.Label(window, text="Choose data source:", bg="#f0f8ff").pack(pady=10)
    tk.Button(
        window, text="Fetch from Scraper", command=lambda: fetch_and_display_weather("scraper"), bg="#add8e6"
    ).pack(pady=5)

    tk.Button(
        window, text="Fetch from MetaWeather API", command=lambda: fetch_and_display_weather("metaweather"), bg="#90ee90"
    ).pack(pady=5)

    # Result display
    result_label = tk.Label(window, text="", font=("Arial", 14), bg="#f0f8ff", justify="left")
    result_label.pack(pady=20)

    # Close button
    tk.Button(window, text="Close", command=window.destroy, bg="#ffdddd").pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    show_weather()
