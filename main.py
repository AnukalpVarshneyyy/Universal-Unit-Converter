import customtkinter as ctk

# --- Unit Conversion Dictionary ---
units = {
    # Length
    "meter (m)": ("length", 1),
    "kilometer (km)": ("length", 1000),
    "centimeter (cm)": ("length", 0.01),
    "millimeter (mm)": ("length", 0.001),
    "mile (mi)": ("length", 1609.344),
    "yard (yd)": ("length", 0.9144),
    "foot (ft)": ("length", 0.3048),
    "inch (in)": ("length", 0.0254),

    # Mass
    "kilogram (kg)": ("mass", 1),
    "gram (g)": ("mass", 0.001),
    "milligram (mg)": ("mass", 0.000001),
    "pound (lb)": ("mass", 0.45359237),
    "ounce (oz)": ("mass", 0.02834952),

    # Time
    "second (s)": ("time", 1),
    "minute (min)": ("time", 60),
    "hour (h)": ("time", 3600),
    "day": ("time", 86400),

    # Temperature
    "celsius (°C)": ("temp", None),
    "fahrenheit (°F)": ("temp", None),
    "kelvin (K)": ("temp", None),

    # Area
    "square meter (m²)": ("area", 1),
    "square kilometer (km²)": ("area", 1_000_000),
    "square centimeter (cm²)": ("area", 0.0001),
    "square millimeter (mm²)": ("area", 0.000001),
    "hectare (ha)": ("area", 10_000),
    "acre": ("area", 4046.856),

    # Volume
    "cubic meter (m³)": ("volume", 1),
    "liter (L)": ("volume", 0.001),
    "milliliter (mL)": ("volume", 0.000001),
    "cubic centimeter (cm³)": ("volume", 0.000001),
    "cubic inch (in³)": ("volume", 1.6387e-5),
    "cubic foot (ft³)": ("volume", 0.0283168),
    "gallon (US)": ("volume", 0.00378541),

    # Speed
    "meter/second (m/s)": ("speed", 1),
    "kilometer/hour (km/h)": ("speed", 0.277778),
    "mile/hour (mph)": ("speed", 0.44704),
    "knot": ("speed", 0.514444),

    # Pressure
    "pascal (Pa)": ("pressure", 1),
    "bar": ("pressure", 100000),
    "atmosphere (atm)": ("pressure", 101325),
    "pound/sq inch (psi)": ("pressure", 6894.76),

    # Energy
    "joule (J)": ("energy", 1),
    "kilojoule (kJ)": ("energy", 1000),
    "calorie (cal)": ("energy", 4.184),
    "kilocalorie (kcal)": ("energy", 4184),
    "watt hour (Wh)": ("energy", 3600),
    "kilowatt hour (kWh)": ("energy", 3.6e6),

    # Digital Storage
    "bit": ("data", 1),
    "byte (B)": ("data", 8),
    "kilobyte (KB)": ("data", 8 * 1024),
    "megabyte (MB)": ("data", 8 * 1024**2),
    "gigabyte (GB)": ("data", 8 * 1024**3),
    "terabyte (TB)": ("data", 8 * 1024**4),
}

# --- Functions ---
def convert_units():
    try:
        value = float(entry_from.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        from_type, from_factor = units[from_unit]
        to_type, to_factor = units[to_unit]

        if from_type != to_type:
            entry_to.delete(0, ctk.END)
            entry_to.insert(0, "Invalid")
            return

        if from_type == "temp":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            base_value = value * from_factor
            result = base_value / to_factor

        entry_to.delete(0, ctk.END)
        entry_to.insert(0, f"{result:.4f}")
    except:
        entry_to.delete(0, ctk.END)
        entry_to.insert(0, "Error")

def convert_temperature(value, from_u, to_u):
    if from_u == "celsius (°C)":
        c = value
    elif from_u == "fahrenheit (°F)":
        c = (value - 32) * 5/9
    elif from_u == "kelvin (K)":
        c = value - 273.15

    if to_u == "celsius (°C)":
        return c
    elif to_u == "fahrenheit (°F)":
        return c * 9/5 + 32
    elif to_u == "kelvin (K)":
        return c + 273.15

# --- UI Setup ---
ctk.set_appearance_mode("light")  # "dark" or "light"
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Universal Unit Converter")
root.geometry("500x500")

title_label = ctk.CTkLabel(root, text="Universal Unit Converter", font=("Segoe UI", 22, "bold"))
title_label.pack(pady=20)

# First Row
frame1 = ctk.CTkFrame(root, corner_radius=15)
frame1.pack(pady=10, padx=20, fill="x")
entry_from = ctk.CTkEntry(frame1, placeholder_text="Enter value", font=("Segoe UI", 14), corner_radius=12, width=200)
entry_from.grid(row=0, column=0, padx=10, pady=10)
combo_from = ctk.CTkComboBox(frame1, values=list(units.keys()), font=("Segoe UI", 14), corner_radius=12, width=220)
combo_from.set("meter (m)")
combo_from.grid(row=0, column=1, padx=10, pady=10)

# "to" label
to_label = ctk.CTkLabel(root, text="to", font=("Segoe UI", 14))
to_label.pack(pady=5)

# Second Row
frame2 = ctk.CTkFrame(root, corner_radius=15)
frame2.pack(pady=10, padx=20, fill="x")
entry_to = ctk.CTkEntry(frame2, placeholder_text="Result", font=("Segoe UI", 14), corner_radius=12, width=200)
entry_to.grid(row=0, column=0, padx=10, pady=10)
combo_to = ctk.CTkComboBox(frame2, values=list(units.keys()), font=("Segoe UI", 14), corner_radius=12, width=220)
combo_to.set("kilometer (km)")
combo_to.grid(row=0, column=1, padx=10, pady=10)

# Convert Button
convert_btn = ctk.CTkButton(root, text="CONVERT", font=("Segoe UI", 15, "bold"), corner_radius=12, command=convert_units, height=40, width=200)
convert_btn.pack(pady=20)

# Footer
footer_label = ctk.CTkLabel(root, text="Developed By Anukalp Varshney", font=("Segoe UI", 12, "italic"))
footer_label.pack(side="bottom", pady=10)

root.mainloop()
