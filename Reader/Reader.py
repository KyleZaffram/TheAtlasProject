import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def load_excel():

    # Hide the main tkinter window
    Tk().withdraw()

    # Open file explorer
    file_path = askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx")]
    )

    # Load Excel file
    df = pd.read_excel(file_path)

    return df