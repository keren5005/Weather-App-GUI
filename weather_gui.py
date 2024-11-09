import tkinter as tk
from weather_scraper import get_weather  

def show_weather():
    country = input("Enter the country name: ").strip() 
    city = input("Enter the city name: ").strip()  
    temperature, condition = get_weather(country,city)    
    
    # Display the GUI
    window = tk.Tk()
    window.title(f"Weather in {city.title()}")
    window.geometry("400x300")  # Set window size
    window.configure(bg="#f0f8ff")  # Set background color

    # Add a title label
    tk.Label(
        window, 
        text=f"Weather in {city.title()}", 
        font=("Helvetica", 20, "bold"), 
        bg="#f0f8ff", 
        fg="#333333"
    ).pack(pady=20)

    # Add temperature and condition labels
    tk.Label(
        window, 
        text=f"Temperature: {temperature}", 
        font=("Arial", 16), 
        bg="#f0f8ff", 
        fg="#ff4500"
    ).pack(pady=10)

    tk.Label(
        window, 
        text=f"Condition: {condition}", 
        font=("Arial", 16), 
        bg="#f0f8ff", 
        fg="#1e90ff"
    ).pack(pady=10)

    # Add a close button with styling
    tk.Button(
        window, 
        text="Close", 
        command=window.destroy, 
        font=("Arial", 14), 
        bg="#ffdddd", 
        fg="#333333", 
        relief="raised"
    ).pack(pady=20)

    # Run the GUI event loop
    window.mainloop()

# Call the function
show_weather()
