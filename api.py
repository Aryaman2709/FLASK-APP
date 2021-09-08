from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

Contacts = [
    {
        'id':1,
        'Name': u'Raju',
        'Contact': u'9987644456',
        'done' : False
    },
    {
        'id':2,
        'Name': u'Rahul',
        'Contact': u'9876543222',
        'done': False
    }
]

@app.route('/add-data', methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status': 'error', 
            'message': 'Please provide the Data'
        }, 400)
    task = {
        'id' : Contacts[-1]['id'] + 1,
        'Name' : request.json['Name'],
        'Contact': request.json.get('Contact', ''),
        'done' : False
    }
    Contacts.append(task)
    return jsonify({
        'status': 'success',
        'message': 'task added successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data': Contacts
    })

if(__name__ =='__main__'):
    app.run(debug=True)
