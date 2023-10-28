
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import pandas as pd


serno = list(range(1, 51))
state = ['Agra', 'Ahmedabad', 'Allahabad(Prayagraj)', 'Amritsar', 'Asansol Durgapur', 'Aurangabad', 'Bengaluru',
         'Bhopal', 'Chandigarh', 'Coimbatore', 'Chennai', 'Delhi', 'Dhanbad', 'Faridabad', 'Ghaziabad', 'Gwalior',
         'Hyderabad',
         'Indore', 'Jabalpur', 'Jaipur', 'Jamshedpur', 'Jodhpur', 'Kannur', 'Kanpur', 'Khozikode', 'Kochi',
         'Kolkata', 'Kollam',
         'Kota', 'Lucknow', 'Ludhiana', 'Madurai', 'Mallapuram', 'Meerut', 'Mumbai', 'Nagpur', 'Nashik', 'Patna',
         'Pune',
         'Raipur', 'Rajkot', 'Srinagar', 'Surat', 'Thiruvanthapuram', 'Thrissur', 'Tiruchirapalli',
         'Vadodra', 'Varanasi', 'Vijaywada city', 'Vizaq']
stagJ = [31, 82, 123, 0, 4, 0, 347, 0, 72, 139, 367, 497, 9, 6, 27, 0, 227, 16, 0, 179,
         20, 2, 0, 57, 184, 278, 39, 0, 0, 60, 12, 0, 0, 0, 28, 16, 0, 0, 27, 44, 0, 0, 28,
         99, 228, 229, 7, 44, 77, 98]
roabJ = [23, 12, 53, 0, 3, 0, 33, 0, 31, 35, 45, 105, 2, 2, 11, 0, 27, 0, 32, 32, 9, 1, 0, 13, 13, 12, 9, 0, 0, 7,
         25, 0, 0, 0, 33, 9, 0, 0, 3, 21, 0, 0, 23, 78, 58, 78, 0, 0, 198, 13]
oth = [17, 41, 21, 0, 2, 0, 232, 0, 4, 97, 255, 12, 23, 1, 10, 0, 43, 0, 61, 13, 23, 7, 0, 21, 134, 129, 32, 0, 0,
       4, 13, 0, 0, 0, 66, 28, 0, 0, 8, 53, 119, 4, 60, 41, 119, 0, 87, 67, 23, 34]
tna = [30, 78, 1, 7, 3, 694, 0, 96, 146, 464, 440, 55, 14, 59, 5, 746, 9, 87, 90, 1, 1, 1, 17, 299, 204, 127, 0, 0,
       307, 105, 9, 0, 0, 107, 100, 0, 0, 16, 201, 812, 37, 440, 45, 76, 237, 276, 464, 68, 299, 127]
perinj = [3, 16, 66, 0, 1, 3, 398, 0, 20, 14, 709, 111, 55, 6, 23, 3, 52, 16, 5, 93, 5, 1, 13, 84, 255, 23, 5, 0, 6,
          6, 0, 6, 3, 13, 3, 4, 0, 0, 55, 5, 1, 13, 24, 44, 56, 78, 86, 45, 67, 19]
SIGNAL = {'Serial No': serno, 'States/UTs': state, 'Staggered Junction': stagJ,
          'Round about Junction': roabJ, 'Others': oth, 'Total number of Accidents': tna, 'Persons Injured': perinj}
SUG = pd.DataFrame(SIGNAL)
SUG.set_index("Serial No", inplace=True)
TLS = [31, 82, 123, 0, 4, 0, 347, 0, 72, 139, 367, 497, 9, 6, 27, 0, 227, 16, 0, 179, 20, 2,
       0, 57, 184, 278, 39, 60, 12, 0, 0, 0, 28, 16, 0, 0, 27, 44, 0, 0, 28, 99, 228, 229, 7, 109, 44, 77, 98,
       189]
PC = [3, 12, 53, 0, 3, 0, 33, 0, 31, 35, 45, 105, 2, 2, 11, 0, 27, 0, 32, 32, 9, 1, 0, 13, 13,
      12, 9, 0, 0, 7, 25, 0, 0, 0, 33, 9, 0, 0, 3, 21, 0, 0, 23, 78, 58, 78, 0, 0, 198, 13]
SS = [7, 41, 21, 30, 71, 29, 12, 7, 13, 20, 21, 5, 13, 3, 16, 0, 7, 0, 7, 0, 7, 24, 31, 27, 10, 5, 15,
      3, 0, 7, 0, 7, 31, 23, 17, 7, 24, 31, 27, 10, 5, 15, 3, 0, 7, 0, 7, 8, 20, 0]
PI = [24, 29, 20, 3, 71, 29, 12, 7, 13, 20, 21, 5, 13, 3, 16, 0, 7, 0, 7, 0, 7, 24, 31, 27, 10, 5,
      15, 3, 0, 7, 0, 7, 24, 31, 27, 10, 5, 15, 3, 0, 7, 0, 7, 24, 31, 27, 10, 5, 8, 27]
data = {'S.No': serno, 'States/UTs': state, 'Traffic Light Signal': TLS,
          'Police Controlled': PC, 'Stop Sign': SS, 'Persons Injured': PI}
df = pd.DataFrame(data)
df.set_index("S.No", inplace=True)

def change_color():
    color = colorchooser.askcolor()
    hexcolor = color[1]
    root.config(bg=hexcolor)
    label.config(bg=hexcolor)
    heading.config(bg=hexcolor)
    # print(hexcolor)


# Initialize a Tkinter window
root = tk.Tk()
root.title("accidents statistics")
root.geometry("1200x800")
root.config(background="#00e6e6")


# Function to display statistics
def display_statistics():
    option = combo.get()
    if option == "View Accidents by Junction Type":
        text.delete('1.0', tk.END)
        text.insert(tk.END, SUG.to_string())
    elif option == "View Accidents by Control Type":
        text.delete('1.0', tk.END)
        text.insert(tk.END, df.to_string())


# Function to display graphs
def display_graphs():
    plt.figure(figsize=(10, 6))
    option = combo.get()

    if option == "View Accidents by Junction Type":
        for col in SUG.columns[2:]:
            plt.barh(SUG['States/UTs'], SUG[col], label=col)
    else:
        for col in df.columns[2:]:
            plt.barh(df['States/UTs'], df[col], label=col)

    # Customize plot appearance here

    plt.xlabel('Accidents')
    plt.ylabel('Cities/Towns')
    plt.legend(loc='upper right')
    plt.title("Accidents Statistics")
    plt.tight_layout()
    plt.show()


# Create a label
label = Label(root, text="Choose an option:",background="#00e6e6",font=(17))
label.place(x=10,y=10)

# Create a combo box for user selection
options = ["View Accidents by Junction Type", "View Accidents by Control Type"]
combo = ttk.Combobox(root, values=options,width=29)
combo.place(x=150,y=10)

# Create a button to display statistics
statistics_button = Button(root, text="Display Statistics", command=display_statistics,activebackground="red")
statistics_button.place(x=10,y=50)

# Create a button to display graphs
graphs_button = Button(root, text="Display Graphs", command=display_graphs,activebackground="blue")
graphs_button.place(x=110,y=50)

heading = Label(root,text="Graphs and Statistics of Accidents in India",font=('Times New Roman',25),background="#00e6e6")
heading.place(x=370,y=20)

cc_button = Button(root, text="change background color ", command=change_color,activebackground="orange",background="blue",fg="white",activeforeground="white")
cc_button.place(x=1000,y=50)
# Create a text box to display statistics
text = tk.Text(root, height=30, width=142)
text.place(x=10,y=100)
root.mainloop()