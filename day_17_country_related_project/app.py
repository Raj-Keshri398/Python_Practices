from flask import Flask, render_template, request
import requests
from countries import countries

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = {}

    if request.method == 'POST':
        user_country = request.form['country'].strip().title()

        if user_country not in countries:
            result['error'] = "Country not found ❌"
        else:
            try:
                # ---------------------------
                # 1. BASIC DATA (RestCountries)
                # ---------------------------
                url = f"https://restcountries.com/v3.1/name/{user_country}?fullText=true"
                response = requests.get(url)

                data = response.json()[0]

                population = data.get('population', 0)

                # ---------------------------
                # 2. ESTIMATION (custom logic)
                # ---------------------------
                male = int(population * 0.51)
                female = int(population * 0.49)

                below_18 = int(population * 0.30)
                above_18 = int(population * 0.70)

                # ---------------------------
                # 3. WIKIPEDIA DATA
                # ---------------------------
                wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{user_country}"
                wiki_res = requests.get(wiki_url)

                history = ""
                if wiki_res.status_code == 200:
                    history = wiki_res.json().get('extract', "No history found")

                # ---------------------------
                # 4. FINAL RESULT
                # ---------------------------
                result = {
                    "name": user_country,
                    "capital": data.get('capital', ["N/A"])[0],
                    "region": data.get('region', "N/A"),
                    "population": population,
                    "lat": data.get('latlng', ["N/A","N/A"])[0],
                    "lng": data.get('latlng', ["N/A","N/A"])[1],
                    "flag": data.get('flags', {}).get('png', ""),
                    
                    "male": male,
                    "female": female,
                    "below_18": below_18,
                    "above_18": above_18,

                    "history": history[:500]  # short history
                }

            except Exception as e:
                result['error'] = str(e)

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)