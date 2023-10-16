from flask import Flask, jsonify

app = Flask(__name)

# Sample data - Replace this with your actual data source or generation logic
data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
