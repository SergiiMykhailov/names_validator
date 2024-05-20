try:
  import flask
except ImportError:
  try:
    import pip
    pip.main(['install', 'flask'])
  except Exception as e:
    print(e)

try:
    import names_dataset
except ImportError:
    import pip
    pip.main(['install', 'names_dataset'])


from names_dataset import NameDataset
from flask import Flask, request, jsonify


app = Flask(__name__)
names_dataset = NameDataset()


@app.route("/")
def hello_world():
    name = request.args.get('name', '')
    if name is None or not isinstance(name, str) or len(name) == 0:
        return jsonify({})
    
    response = {}
    try:
        name_info = names_dataset.search(name)
        response = {
           'status': 'succeeded',
           'data': name_info
        }
    except Exception as e:
        response = {
          'status': 'failed',
          'reason': str(e)
        }

    response_data = jsonify(response)
    return response_data


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")