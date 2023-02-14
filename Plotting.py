import matplotlib.pyplot as plt                                     # import matplotlib library
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg    # FigureCanavasTkAgg class is an interface between the figure and Tkinter canvas
from matplotlib.figure import Figure
import tkinter as tk
import Housetype_Salecount as hs
import Avgsales_perNeighborhood as an
import Avgsales_perYear as py                                       # import module Avgsales_perNeighbohood


root = tk.Tk()                                                      # create instance of TK() class
root.title("Housing price analytics")
fig, ax = plt.subplots(figsize=(14, 8))                             # creating fix and ax object
c1 = FigureCanvasTkAgg(fig, root)                                   #matplotlib Zeichenflaeche/create the canvas to polt charts
c1.get_tk_widget().grid(row=0, column=1, rowspan=20)                # Geometriemanager


def average_salesprice_peryear_plot():                              # plot1
    clear_plot()
    x_axis = []
    y_axis = []
    for key, value in py.getavgsalesprice_peryear().items():        # loop on the dicto (result of getavgsalesprice_per year function)
        x_axis.append(key)                                          # list of year
        y_axis.append(value)                                        # list of Average price
    ax.plot(x_axis, y_axis, "o-g", label="Average Price")
    ax.axis([0, 5, 0, 250000])
    ax.set_ylabel("Average Price", size=12, labelpad=10, color="green")     # create label on y_axis
    ax.set_xlabel("Year", size=12, labelpad=10, color="green")              # create label on x_axis
    ax.set_title("Average price per year", size=15, color="green")
    ax.grid(visible=True)
    c1.draw()                                                                    # entspricht dem plt.show()- Befehl


def average_salesprice_perneighborhood_plot():                               ## Plot2
    clear_plot()
    x_axis = []
    y_axis = []
    for key, value in an.getavgsalesprice_perneighborhood().items():
        x_axis.append(key)
        y_axis.append(value)
    ax.plot(x_axis, y_axis, "o-g", label="Average Price per neighborhood")  # plot y versus x
    ax.axis([0, 25, 0, max(y_axis)])
    ax.set_ylabel("Price", size=12, labelpad=10, color="green")
    ax.set_xlabel("Neighborhood", size=12, labelpad=10, color="green")
    ax.set_title("Average price per neighborhood", size=15, color="green")
    ax.grid(visible=True)
    fig.autofmt_xdate(rotation=30)                                           # this method figure module rotate and right align xticks lables
    c1.draw()                                                               # the rotation of the xtick labels
    c1.draw()

def salecount_perhouse_type():                                                   ##Plot3
    clear_plot()
    house_type = []
    sale_count = []
    for key, value in hs.getsales_perhousetype().items():               # using loop in dict to get the desc(HouseType) as x_axis and count as y_axis
        house_type.append(key)
        sale_count.append(value)
    ax.bar(house_type, sale_count,  color='green', label="Units sold per house type")
    ax.axis([0, 15, 0, max(sale_count)])
    ax.set_xlabel("House type Id", size=12, labelpad=10, color="green")
    ax.set_ylabel("Units sold", size=12, labelpad=10, color="green")
    ax.grid(visible=True)
    ax.legend()
    fig.autofmt_xdate(rotation=30)                                      # this method figure module rotate and right align xticks lables
    c1.draw()                                                           # the rotation of the xtick labels

def clear_plot():
    ax.cla()
    c1.draw()

def open_tinker():

    b1 = tk.Button(root, text="Show avg Price/Year", height=5, width=25, command=average_salesprice_peryear_plot, bd=3, relief='raised', font=('Arial',12,'bold'))
    b1.grid(row=0, column=0, sticky="nsew")
    b2 = tk.Button(root, text="Show avg Price/Neighborhood", height=5, width=25, command=average_salesprice_perneighborhood_plot, bd=3, relief='raised', font=('Arial',12,'bold'))
    b2.grid(row=1, column=0, sticky="nsew")
    b3 = tk.Button(root, text="Show total sales/ House type", height=5, width=25, command=salecount_perhouse_type, bd=3, relief='raised', font=('Arial',12,'bold'))  # Tkinter Button
    b3.grid(row=2, column=0, sticky="nsew")
    b4 = tk.Button(root, text="Clear", height=5, width=25, command=clear_plot, bd=3, relief='raised', font=('Arial',12,'bold'))  # Tkinter Button
    b4.grid(row=3, column=0, sticky="nsew")
    b5 = tk.Button(root, text="Quit", height=5, width=25, command=root.quit, bd=3, relief='raised', font=('Arial',12,'bold'))  # Tkinter Button
    b5.grid(row=4, column=0, sticky="nsew")
    root.mainloop()