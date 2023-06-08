from flask import Flask, render_template

app = Flask(_name_)

@app.route('/create-package', methods=['POST'])
def create_package():
    package_data = request.get_json()
    # Here is where you would process the data and add it to your database.
    # But for now, let's just return the data received.
    return jsonify(package_data), 200
if _name_ == '_main_':
    app.run(port=5000)