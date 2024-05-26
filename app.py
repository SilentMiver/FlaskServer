from flask import Flask
from controllers.product_controller import product_bp
from controllers.order_controller import order_bp
from controllers.health_check_controller import health_bp

app = Flask(__name__)

app.register_blueprint(product_bp)
app.register_blueprint(order_bp)
app.register_blueprint(health_bp)

if __name__ == '__main__':
    app.run(debug=True)
