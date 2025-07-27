# 🚗 Turkiye Fuel Cost Calculator

Calculate your car's fuel cost for all 81 provinces in Turkiye with a modern and user-friendly web application.

## ✨ Features

- **🌍 81 Province Support**: Separate fuel prices for all provinces in Turkiye
- **⛽ Multi-Fuel Support**: Gasoline, Diesel and LPG calculation
- **🔄 Real-Time Prices**: Current fuel prices with API integration
- **🏙️ City-Based Calculation**: Separate prices and calculations for each city
- **📱 Responsive Design**: Mobile and desktop compatible interface
- **⚡ Fast Calculation**: Instant results
- **🇹🇷 Turkish Character Support**: City names with İ, Ğ, Ş, Ç, Ö, Ü characters

## 🛠️ Technologies

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **API**: Hasan Adıgüzel API (Fuel prices)
- **URL Encoding**: Turkish character support

## 📋 Requirements

- Python 3.7+
- pip (Python package manager)

## 🚀 Installation

1. **Clone the project:**
   ```bash
   git clone <repository-url>
   cd FuelCostCalculator
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in your browser:**
   ```
   http://localhost:5000
   ```

## 📖 Usage

1. **🏙️ Select City**: Choose the city you want to calculate from the dropdown
2. **📊 Fuel Consumption**: Enter how many liters your car consumes per 100 km
3. **🛣️ Distance**: Enter the total distance you will travel in kilometers
4. **⛽ Fuel Type**: Select the type of fuel you use (Gasoline, Diesel, LPG)
5. **💰 Calculate**: Click the "Calculate Cost" button
6. **📈 View Results**: View the total cost and details

## 🔧 API Integration

The application uses Hasan Adıgüzel API to fetch current fuel prices:

- **Endpoint**: `http://hasanadiguzel.com.tr/api/akaryakit/sehir={sehir}`
- **Supported Cities**: 81 provinces
- **Fuel Types**: Gasoline, Diesel, LPG
- **Turkish Character Support**: With URL encoding

### API Data Structure
```json
{
  "data": {
    "51,20": {
      "Motorin(Eurodiesel)_TL/lt": "53,57",
      "Fuel_Oil_TL/Kg": "28,11",
      "Otogaz_TL/lt": ""
    }
  }
}
```

## 📁 Project Structure

```
FuelCostCalculator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── templates/
    └── index.html        # Main web page
```

## 🎯 Calculation Formula

```
Fuel Consumed (Liters) = (Consumption per 100 km × Total distance) ÷ 100
Total Cost (TL) = Fuel consumed × City-based fuel price
```

### Example Calculation
- **Consumption**: 7 L/100km
- **Distance**: 150 km
- **City**: ISTANBUL
- **Fuel**: Gasoline (51.20 TL/Liter)

```
Fuel Consumed = (7 × 150) ÷ 100 = 10.5 Liters
Total Cost = 10.5 × 51.20 = 537.60 TL
```

## 🌍 Supported Cities

All 81 provinces of Turkiye are supported:
- ADANA, ADIYAMAN, AFYON, AĞRI, AKSARAY, AMASYA, ANKARA, ANTALYA, AYDIN
- BALIKESİR, BARTIN, BATMAN, BİLECİK, BOLU, BURDUR, BURSA, ÇANAKKALE
- ÇANKIRI, ÇORUM, DENİZLİ, DİYARBAKIR, DÜZCE, EDİRNE, ELAZIĞ, ERZİNCAN
- ERZURUM, ESKİŞEHİR, GAZİANTEP, GİRESUN, HATAY, ISPARTA, İSTANBUL, İZMİR
- İÇEL, K.MARAŞ, KARABÜK, KARAMAN, KASTAMONU, KAYSERİ, KIRIKKALE, KIRKLARELİ
- KIRŞEHİR, KOCAELİ, KONYA, KÜTAHYA, MALATYA, MANİSA, MARDİN, MUĞLA
- NEVŞEHİR, NİĞDE, ORDU, OSMANİYE, RİZE, SAKARYA, SAMSUN, SİVAS
- SİNOP, ŞANLIURFA, TEKİRDAĞ, TOKAT, TRABZON, UŞAK, VAN, YALOVA
- YOZGAT, ZONGULDAK

## 🔒 Security and Error Handling

- **Input Validation**: All user inputs are validated
- **API Error Handling**: Appropriate error messages when API is down
- **Turkish Character Support**: Safe API calls with URL encoding
- **Try-Catch Blocks**: Robust error handling

## 🐛 Troubleshooting

### API Connection Error
- Check your internet connection
- API service may be temporarily unavailable
- Try again later

### Turkish Character Error
- The application automatically encodes Turkish characters
- If the problem persists, refresh your browser

### Port Error
- If port 5000 is in use, change the port in `app.py`:
  ```python
  app.run(debug=True, port=5001)
  ```

### Dependency Error
- Reinstall packages:
  ```bash
  pip install -r requirements.txt --force-reinstall
  ```

## 🚀 Feature Details

### City-Based Prices
- Separate fuel prices for each city
- Real-time updates
- Automatic price updates when city changes

### Fuel Types
- **Gasoline**: City-based prices
- **Diesel**: Motor oil prices
- **LPG**: Fuel Oil prices (from API)

### User Interface
- Modern and responsive design
- Easy to use
- Instant results
- Error messages

## 🎉 Acknowledgments

- [Hasan Adıgüzel API](https://www.hasanadiguzel.com.tr/api-tutorials/guncel-akaryakit-fiyatlari-api) - For fuel prices
- Flask - For web framework
- All contributors 
