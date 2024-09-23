from flask import Flask, render_template, request, redirect, url_for
from models import db, Product, Store, Sale
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/store_tracking_poc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# -------------------- Home Route --------------------
@app.route('/')
def index():
    product_count = Product.query.count()
    store_count = Store.query.count()
    sale_count = Sale.query.count()
    return render_template('index.html', product_count=product_count, store_count=store_count, sale_count=sale_count, active_page='home')


# -------------------- CRUD for Products --------------------
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products, active_page='products')

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    category = request.form['category']
    price = request.form['price']
    new_product = Product(product_name=name, category=category, price=price)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('products'))

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        product.product_name = request.form['name']
        product.category = request.form['category']
        product.price = request.form['price']
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('edit_product.html', product=product, active_page='products')

@app.route('/delete_product/<int:id>')
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products'))

# -------------------- CRUD for Stores --------------------
@app.route('/stores')
def stores():
    stores = Store.query.all()
    return render_template('stores.html', stores=stores, active_page='stores')

@app.route('/add_store', methods=['POST'])
def add_store():
    name = request.form['name']
    location = request.form['location']
    new_store = Store(store_name=name, location=location)
    db.session.add(new_store)
    db.session.commit()
    return redirect(url_for('stores'))

@app.route('/edit_store/<int:id>', methods=['GET', 'POST'])
def edit_store(id):
    store = Store.query.get(id)
    if request.method == 'POST':
        store.store_name = request.form['name']
        store.location = request.form['location']
        db.session.commit()
        return redirect(url_for('stores'))
    return render_template('edit_store.html', store=store, active_page='stores')

@app.route('/delete_store/<int:id>')
def delete_store(id):
    store = Store.query.get(id)
    db.session.delete(store)
    db.session.commit()
    return redirect(url_for('stores'))

# -------------------- CRUD for Sales --------------------
@app.route('/sales')
def sales():
    sales = Sale.query.order_by(Sale.sale_date.desc()).all()  # Sort by sale_date descending
    products = Product.query.all()
    stores = Store.query.all()
    return render_template('sales.html', sales=sales, products=products, stores=stores, active_page='sales')

@app.route('/add_sale', methods=['POST'])
def add_sale():
    product_id = request.form['product_id']
    store_id = request.form['store_id']
    sale_date = datetime.strptime(request.form['sale_date'], '%Y-%m-%d')
    quantity = int(request.form['quantity'])
    
    product = Product.query.get(product_id)
    total_amount = product.price * quantity

    new_sale = Sale(product_id=product_id, store_id=store_id, sale_date=sale_date, quantity=quantity, total_amount=total_amount)
    db.session.add(new_sale)
    db.session.commit()
    return redirect(url_for('sales'))

@app.route('/edit_sale/<int:id>', methods=['GET', 'POST'])
def edit_sale(id):
    sale = Sale.query.get(id)
    if request.method == 'POST':
        sale.product_id = request.form['product_id']
        sale.store_id = request.form['store_id']
        sale.sale_date = datetime.strptime(request.form['sale_date'], '%Y-%m-%d')
        sale.quantity = int(request.form['quantity'])
        
        product = Product.query.get(sale.product_id)
        sale.total_amount = product.price * sale.quantity
        
        db.session.commit()
        return redirect(url_for('sales'))
    
    products = Product.query.all()
    stores = Store.query.all()
    return render_template('edit_sale.html', sale=sale, products=products, stores=stores, active_page='sales')

@app.route('/delete_sale/<int:id>')
def delete_sale(id):
    sale = Sale.query.get(id)
    db.session.delete(sale)
    db.session.commit()
    return redirect(url_for('sales'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
