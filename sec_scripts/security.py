import os
import requests
from datetime import datetime
import csv

def check_website(url):
    """Verifica el estado del sitio web y registra el resultado en un archivo CSV."""
    status = ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            status = "Active and running under github Pages"
        else:
            status = f"Error {response.status_code}"
    except requests.RequestException as e:
        status = f"Error {e}"
    
    # Obtiene la ruta absoluta del directorio de trabajo
    base_path = os.getcwd()
    # Combina la ruta del directorio de trabajo con la ubicación del archivo CSV
    csv_path = os.path.join(base_path, 'checks', 'log.csv')

    # Registra la fecha, hora y el estado en un archivo CSV
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), status])

    return status

if __name__ == "__main__":
    check_website("https://edujbarrios.github.io/eyemadmusicwebsite/")
