from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load CSV data
csv_path = "/Users/nguyenphucthanh/Downloads/price_optimization/data/retail_price.csv"
data = pd.read_csv(csv_path)

@app.route("/api/ids/<category>", methods=["GET"])
def get_ids(category):
    if category == "":
        ids = list(data["product_id"].unique())
        return jsonify(ids)
    else:
        ids = list(data[data["product_category_name"] == category]["product_id"].unique())
        return jsonify(ids)


@app.route("/api/categories/<id>", methods=["GET"])
def get_categories(id):
    if id == "":
        categories = list(data["product_category_name"].unique())
        return jsonify(categories)
    else:
        categories = list(data[data["product_id"] == id]["product_category_name"].unique())
        return jsonify(categories)



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
