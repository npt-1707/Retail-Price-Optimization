from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load CSV data
csv_path = "/Users/nguyenphucthanh/Downloads/price_optimization/data/retail_price.csv"
data = pd.read_csv(csv_path)

@app.route("/api/ids", methods=["GET"])
def get_ids():
    ids = list(data["product_id"].unique())
    return jsonify(ids)


@app.route("/api/categories", methods=["GET"])
def get_categories():
    categories = list(data["product_category_name"].unique())
    return jsonify(categories)


@app.route("/api/ids/<category>", methods=["GET"])
def get_ids_by_category(category):
    ids = list(data[data["product_category_name"] == category]["product_id"].unique())
    return jsonify(ids)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
