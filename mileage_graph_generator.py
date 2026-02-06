import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime

# Dates (DD/MM/YYYY)
dates = [
    "20/10/2025",
    "27/10/2025",
    "6/11/2025",
    "16/11/2025",
    "23/11/2025",
    "10/12/2025",
    "18/12/2025",
    "19/12/2025",
    "30/12/2025",
    "19/1/2026",
    "5/2/2026"
]

# Corresponding values
values = [233256, 234144, 234866, 235684, 236351, 237319, 238094, 238221, 239154, 239994, 241468]

# Convert strings to datetime objects
dates = [datetime.strptime(d, "%d/%m/%Y") for d in dates]

# Plot
plt.plot(dates, values, marker='o')

# Remove rounding on Y-axis labels
# plt.ticklabel_format(style='plain', axis='y', useOffset=False)

# plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
# plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
# plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))


plt.xlabel("Date")
plt.ylabel("Mileage (km)")
plt.title("Mileage over Time")

plt.show()
