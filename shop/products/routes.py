from flask import redirect, render_template, url_for, flash, request, session
from shop import db, app
from .models import Brand, Category, Addproduct
from .forms import Addproducts

@app.route('/')
def gome():
    return''

@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The Brand {getbrand} was added to your database', 'sucess')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', brands='brands')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The Category {getbrand} was added to your database', 'sucess')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    form = Addproducts(request.form)
    return render_template('products/addproduct.html' , title='Add product page', form=form)    