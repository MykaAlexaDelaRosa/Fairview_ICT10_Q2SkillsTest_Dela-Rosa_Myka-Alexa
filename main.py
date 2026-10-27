from pyscript import document, display 

# Getting the value of the input field
# Dictionary containing non-metal element information
# Format: Symbol: (Name, Atomic Number, Atomic Mass)
nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "Al": ("Aluminum", 13, 26.982),
    "Si": ("Silicon", 14, 28.085),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948), 
    "Se": ("Selenium", 34, 78.971), 
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904), 
    "Xe": ("Xenon", 54, 131.293),
    "At": ("Astatine", 85, 210), 
    "Rn": ("Radon", 86, 222)}

# Function that runs when the button is clicked
def search_element(event):
    # Get the symbol entered by the user
    symbol = document.getElementById("symbol").value.strip().capitalize()

    # Get the element information from the dictionary
    element = nonmetals.get(symbol, ("Not found", "N/A", "N/A"))

    # Get the result area
    result = document.getElementById("result")

    # Display each detail on a separate line
    result.innerHTML = (
        "<h3>Element Information</h3>"
        "<p><b>Element Symbol:</b> " + symbol + "</p>"
        "<p><b>Element Name:</b> " + str(element[0]) + "</p>"
        "<p><b>Atomic Number:</b> " + str(element[1]) + "</p>"
        "<p><b>Atomic Mass:</b> " + str(element[2]) + "</p>"
    )
