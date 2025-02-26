from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }
    return render_template('data.html', user_data=user_data)