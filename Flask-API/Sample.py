from flask import request, jsonify, Flask

app=Flask(__name__)

users=[]
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_users():
    data=request.json
    if not data or 'name' not in data:
        return jsonify({'error':'Name is Required'}), 400
    users.append({'name':data['name']})
    return jsonify({'message':'User added succesfully'}), 201

if __name__=='__main__':
    app.run(debug=False)
