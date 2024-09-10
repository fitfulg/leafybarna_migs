from flask import Flask
from endpoints import get_trees_in_parks, get_local_street_trees, get_parks_and_gardens, get_local_interest_trees, get_trees_in_parks_unique_neighborhoods, get_local_street_trees_unique_catalogation

app = Flask(__name__)

# Define routes
@app.route('/trees-in-parks', methods=['GET'])
def trees_in_parks():
    return get_trees_in_parks()

@app.route('/trees-in-parks/unique-neighborhoods', methods=['GET'])
def trees_in_parks_unique_neighborhoods():
    return get_trees_in_parks_unique_neighborhoods()

@app.route('/local-street-trees', methods=['GET'])
def local_street_trees():
    return get_local_street_trees()

@app.route('/local-street-trees/unique-catalogation', methods=['GET'])
def local_street_trees_unique_catalogation():
    return get_local_street_trees_unique_catalogation()

@app.route('/parks-and-gardens', methods=['GET'])
def parks_and_gardens():
    return get_parks_and_gardens()

@app.route('/local-interest-trees', methods=['GET'])
def local_interest_trees():
    return get_local_interest_trees()

if __name__ == '__main__':
    app.run(debug=True)
