import urllib3
import json
from bs4 import BeautifulSoup

# Deshabilitar advertencias SSL
urllib3.disable_warnings()

url = "https://www.bcv.org.ve"
http = urllib3.PoolManager(cert_reqs='CERT_NONE')

try:
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Extraer tasa del dólar desde bcv.org.ve
    div_dolar = soup.find('div', id='dolar')
    tasa_texto = div_dolar.find('strong').text.strip()
    
    # Convertir "36,50" a 36.50
    tasa_limpia = float(tasa_texto.replace(',', '.'))
    
    datos = {"tasa_bcv": tasa_limpia}
    
    with open('tasa.json', 'w') as f:
        json.dump(datos, f)
        
    print(f"Tasa BCV obtenida: {tasa_limpia}")
except Exception as e:
    print(f"Error extrayendo la tasa del BCV: {e}")
