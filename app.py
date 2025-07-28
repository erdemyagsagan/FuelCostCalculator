from flask import Flask, render_template, request, jsonify
import json
import urllib.request
import urllib.error
import urllib.parse

app = Flask(__name__)

def get_cities_from_api():
    cities = [
        "ADANA", "ADIYAMAN", "AFYON", "AGRI", "AKSARAY", "AMASYA", "ANKARA", 
        "ANTALYA", "AYDIN", "BALIKESIR", "BARTIN", "BATMAN", "BILECIK", "BOLU", 
        "BURDUR", "BURSA", "CANAKKALE", "CANKIRI", "CORUM", "DENIZLI", 
        "DIYARBAKIR", "DUZCE", "EDIRNE", "ELAZIĞ", "ERZINCAN", "ERZURUM", 
        "ESKISEHIR", "GAZİANTEP", "GIRESUN", "HATAY", "ISPARTA", "ISTANBUL", 
        "IZMIR", "İÇEL", "K.MARAS", "KARABUK", "KARAMAN", "KASTAMONU", 
        "KAYSERI", "KIRIKKALE", "KIRKLARELI", "KIRSEHIR", "KOCAELI", "KONYA", 
        "KUTAHYA", "MALATYA", "MANISA", "MARDİN", "MUGLA", "NEVSEHIR", 
        "NİĞDE", "ORDU", "OSMANIYE", "RIZE", "SAKARYA", "SAMSUN", "SIVAS", 
        "SİNOP", "ŞANLIURFA", "TEKIRDAG", "TOKAT", "TRABZON", "USAK", "VAN", 
        "YALOVA", "YOZGAT", "ZONGULDAK"
    ]
    return cities

def get_fuel_prices_from_api(city="ISTANBUL"):
    try:
        encoded_city = urllib.parse.quote(city)
        api_url = f"http://hasanadiguzel.com.tr/api/akaryakit/sehir={encoded_city}"
        result = urllib.request.urlopen(api_url).read().decode('utf-8')
        data = json.loads(result)

        if "data" in data and data["data"]:
            # En son veriyi al (en güncel)
            data_keys = list(data["data"].keys())
            if data_keys:
                latest_key = data_keys[-1]  # En son veri
                latest_data = data["data"][latest_key]
                
                
                benzin_price = latest_key
                dizel_price = latest_data.get("Motorin(Eurodiesel)_TL/lt", "")
                lpg_price = latest_data.get("Fuel_Oil_TL/Kg", "")  
                
                if benzin_price and dizel_price and lpg_price and lpg_price != '':
                    # Virgülü noktaya çevir ve float'a dönüştür
                    prices = {
                        'benzin': float(benzin_price.replace(',', '.')),
                        'dizel': float(dizel_price.replace(',', '.')),
                        'LPG': float(lpg_price.replace(',', '.'))
                    }
                    return prices
                else:
                    return None
            else:
                return None
        else:
            return None
            
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"API hatası: {e}")
        return None

@app.route('/')
def index():
    # API'den şehir listesini ve fiyatları çek
    cities = get_cities_from_api()
    fuel_prices = get_fuel_prices_from_api()
    return render_template('index.html', prices=fuel_prices, cities=cities)

@app.route('/api/cities')
def get_cities():
    """API endpoint - şehir listesini döndür"""
    try:
        cities = get_cities_from_api()
        return jsonify({
            'success': True,
            'cities': cities
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/fuel-prices')
def get_fuel_prices():
    """API endpoint - yakıt fiyatlarını döndür"""
    try:
        city = request.args.get('city', 'ISTANBUL')
        prices = get_fuel_prices_from_api(city)
        
        if prices:
            return jsonify({
                'success': True,
                'prices': prices,
                'city': city
            })
        else:
            return jsonify({
                'success': False,
                'error': 'API\'den fiyat alınamadı'
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        consumption = float(data.get('consumption', 0))  # L/100km
        distance = float(data.get('distance', 0))        # km
        fuel_type = data.get('fuel_type', 'benzin')      # yakıt tipi
        city = data.get('city', 'ISTANBUL')              # şehir
        
        # API'den güncel fiyatları al
        fuel_prices = get_fuel_prices_from_api(city)
        
        # Debug: Fiyatları yazdır
        print(f"Calculate Debug - City: {city}, Fuel Type: {fuel_type}")
        print(f"Fuel Prices: {fuel_prices}")
        
        if not fuel_prices:
            return jsonify({
                'success': False,
                'error': f'{city} için API\'den fiyat alınamadı. Lütfen daha sonra tekrar deneyin.'
            })
        
        if fuel_type.lower() == 'lpg':
            fuel_price = fuel_prices.get('LPG', 0)  
        else:
            fuel_price = fuel_prices.get(fuel_type.lower(), 0)
        print(f"Found Fuel Price: {fuel_price}")
        
        if fuel_price == 0:
            return jsonify({
                'success': False,
                'error': f'{city} için {fuel_type} fiyatı bulunamadı'
            })
        
        total_fuel_needed = (consumption * distance) / 100  # Litre
        total_cost = total_fuel_needed * fuel_price         # TL
        
        return jsonify({
            'success': True,
            'total_fuel': round(total_fuel_needed, 2),
            'total_cost': round(total_cost, 2),
            'fuel_price': fuel_price,
            'consumption': consumption,
            'distance': distance,
            'fuel_type': fuel_type,
            'city': city,
            'prices': fuel_prices
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True) 
