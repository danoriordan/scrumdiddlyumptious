# filename: install_geopy.py

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install geopy
install("geopy")

print("Geopy has been installed successfully.")