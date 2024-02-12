import tkinter as tk
from tkinter import ttk
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# Function to fetch and plot stock data
def fetch_and_plot(symbol):
    # Fetch stock data
    end_date = datetime.now()
    start_date = end_date - pd.DateOffset(years=int(selected_years.get()))
    stock_data = web.DataReader(symbol, 'stooq', start_date, end_date)
    
    # Plotting
    fig, ax = plt.subplots()
    stock_data['Close'].plot(ax=ax, title=f'{symbol} Closing Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    
    # Clear previous figure
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    canvas.draw()

# Main application window
app = tk.Tk()
app.title('Stock Data Analyzer')

# Dropdown menu for stock symbol selection
label = ttk.Label(app, text="Select a stock symbol:")
label.pack(pady=10)

# Example stock symbols
stock_symbols = [
    'AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA',
    'AMD', 'AAL', 'ABNB','ACAD','ACB','ADBE',
    'CARS', 'BTCM', 'NVDA', 'META', 'COST'
    ]
selected_symbol = tk.StringVar()
dropdown = ttk.Combobox(app, textvariable=selected_symbol, values=stock_symbols)
dropdown.pack()

# Dropdown for year selection
label_years = ttk.Label(app, text="Select number of years:")
label_years.pack(pady=(10,0))

years_options = ['1', '2', '5', '10']
selected_years = tk.StringVar()
dropdown_years = ttk.Combobox(app, textvariable=selected_years, values=years_options)
dropdown_years.pack()

# Frame for plotting
frame = tk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True)

# Button to fetch and plot data
plot_button = ttk.Button(app, text="Plot", command=lambda: fetch_and_plot(selected_symbol.get()))
plot_button.pack(pady=10)

app.mainloop()