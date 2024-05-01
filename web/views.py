from flask import Flask, render_template
from users.controllers.user_controller import user_controller
from users.controllers.products_controller import products_controller
from users.models.db import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(user_controller)
# Registrando el blueprint del controlador de productos
app.register_blueprint(products_controller)

# Ruta para renderizar el template index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit/<string:id>')
def edit_user(id):
    print("id recibido",id)
    return render_template('edit.html', id=id)

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/edit_product/<string:id>')
def edit_product(id):
    print("id recibido",id)
    return render_template('edit_product.html', id=id)

if __name__ == '__main__':
    app.run()

