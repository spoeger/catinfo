from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
CAT_FACT_API_URL = "https://meowfacts.herokuapp.com/"

@app.route('/')
def index():
    return redirect('/cat-info')

@app.route('/cat-info')
def cat_info():
    # Fetch Cat Image
    image_response = requests.get(CAT_API_URL)
    if image_response.status_code == 200:
        image_url = image_response.json()[0]['url']
    else:
        image_url = "https://via.placeholder.com/400?text=No+Cat+Image"

    # Fetch Cat Fact
    fact_response = requests.get(CAT_FACT_API_URL)
    if fact_response.status_code == 200:
        fact = fact_response.json()['data'][0]
    else:
        fact = "No fact available at the moment."

    # Pass data to template
    return render_template("cat_page.html", image_url=image_url, fact=fact)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
