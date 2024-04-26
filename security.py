import requests
from datetime import datetime
import csv

def check_website(url):
    """Verifica el estado del sitio web y registra el resultado en un archivo CSV."""
    status = ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            status = "Activo"
        else:
            status = f"Error {response.status_code}"
    except requests.RequestException as e:
        status = f"Error {e}"
    
    # Registra la fecha, hora y el estado en un archivo CSV
    with open('checks/log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), status])

    return status

if __name__ == "__main__":
    check_website("https://edujbarrios.github.io/eyemadmusicwebsite/")
