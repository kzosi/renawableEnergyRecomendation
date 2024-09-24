from flask import Flask, render_template, request, redirect, url_for
from energy_logic import dobierz_zrodlo_energii  # Importowanie logiki z pliku

app = Flask(__name__)

# Średnie zużycie energii na podstawie liczby domowników (kWh/rok)
zuzycie_na_rok = {
    1: (800, 1600),
    2: (1100, 1700),
    3: (1400, 2100),
    4: (1900, 2300),
    5: (2200, 2700),
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        budget = float(request.form['budget'])
        preference = request.form['preference'].lower()

        # Sprawdzamy, czy użytkownik zaznaczył "Nie wiem" dla zużycia energii
        if 'dont_know_energy' in request.form:
            num_people = int(request.form['num_people'])
            min_usage, max_usage = zuzycie_na_rok.get(num_people, (800, 1600))
            energy_usage = (min_usage + max_usage) / 2 / 12  # Przeliczamy na zużycie miesięczne
        else:
            energy_usage = float(request.form['energyUsage'])
        
        rekomendacja = dobierz_zrodlo_energii(location, energy_usage, budget, preference)
        return redirect(url_for('best_choice', rekomendacja=rekomendacja))
    
    return render_template('index.html')

@app.route('/bestChoice')
def best_choice():
    rekomendacja = request.args.get('rekomendacja')
    return render_template('bestChoice.html', rekomendacja=rekomendacja)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/save-coordinates', methods=['POST'])
def save_coordinates():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    
    # You can process the coordinates here (e.g., reverse geocoding, etc.)
    # For now, just print the coordinates
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    
    return f"Coordinates received: Latitude {latitude}, Longitude {longitude}"

if __name__ == "__main__":
    app.run(debug=True)
