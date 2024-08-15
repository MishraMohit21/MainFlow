import tkinter as tk
from tkinter import ttk
import requests
import os
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")
rates = {}

def fetch_rates():
    """Fetch exchange rates and update the dropdown with available currencies."""
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(url)
    data = response.json()

    if data['result'] == "success":
        global rates
        rates = data['conversion_rates']
        currency_dropdown['values'] = sorted(rates.keys())  
        if "INR" in rates:
            selected_currency.set("INR")  
        else:
            selected_currency.set(list(rates.keys())[0])  
        result_label.config(text="Rates fetched successfully!")
    else:
        result_label.config(text="Failed to fetch rates: " + data.get('error-type', 'Unknown error'))

def convert_currency():
    """Convert USD to selected currency using the latest fetched rate."""
    try:
        amount = float(usd_entry.get())
        currency = selected_currency.get()
        result = amount * rates[currency]
        result_label.config(text=f"{amount} USD is {result:.2f} {currency}")
    except ValueError:
        result_label.config(text="Please enter a valid amount.")
    except KeyError:
        result_label.config(text="Please select a valid currency.")


root = tk.Tk()
root.title("Currency Converter")
root.configure(background='#333')  


style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#333', foreground='white', font=('Helvetica', 12))
style.configure('TLabel', background='#333', foreground='white', font=('Helvetica', 12))
style.configure('TEntry', foreground='black', font=('Helvetica', 12))
style.configure('TCombobox', foreground='black', font=('Helvetica', 12))


usd_entry = ttk.Entry(root, font=('Helvetica', 16))
usd_entry.pack(pady=20, padx=20)


selected_currency = tk.StringVar()
currency_dropdown = ttk.Combobox(root, textvariable=selected_currency, width=18, font=('Helvetica', 16))
currency_dropdown.pack(pady=10, padx=20)
currency_dropdown.config(state="readonly")


convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=20, padx=20)


result_label = ttk.Label(root, text="Result will appear here...", font=('Helvetica', 14))
result_label.pack(pady=20, padx=20)

fetch_rates()  

root.mainloop()
