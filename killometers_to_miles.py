from flask import Flask

app = Flask(__name__)


@app.route('/')
def site_rules():
    return 'Kilometer to Miles converter \n Add on /km/<int> to display that int number in miles'


@app.route('/km/<int:km>')
def km_to_miles(km):
    miles = km / 1.609
    return f'{km} kilometers converted to {miles} miles'


if __name__ == "__main__":
    app.run()
