from flask import Flask, render_template, request, session, redirect, jsonify

import datetime
import os
import json
import db_helper


app = Flask(__name__, template_folder='template', static_url_path='/static')


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/api/initilize", methods=['POST'])
def initilize():
    configs, messengers = db_helper.getConfig()
    return jsonify({'messengers':[messenger['name'] for messenger in messengers],
     'qp_series':configs['qp_series'],
     'routes':configs['routes']}) 

@app.route("/api/get-colleges", methods=['POST'])
def get_colleges():
    selected_route = request.form.get("selectedRoute")
    clgList = db_helper.sortAndGetData("collegeList", "Route", str(selected_route))
    return jsonify({'collegeNames':[data["College Name"] + " " + data["Place"] for data in clgList]}) 

@app.route("/api/check-db-connection",  methods=['POST'])
def check_db_status():
    try:
        is_connected = db_helper.check_db_connection()
        return jsonify({'dbStatus':is_connected})
    except Exception as e:
        return jsonify({'dbStatus':False})

@app.route("/view-bundles", methods=['GET'])
def view_bundles_page():
    return render_template("view_bundles.html")

@app.route("/api/load-table", methods=['POST'])
def load_tables():
    def sort_keys(document, order):
        return {key: document[key] for key in order if key in document}

    return [ sort_keys(doc, ['qpSeries','qpCode','isNil','receivedDate','messenger','collegeName','remarks']) for doc in db_helper.getAllBundles()]
        
if __name__ == '__main__':
    app.run(debug=True)