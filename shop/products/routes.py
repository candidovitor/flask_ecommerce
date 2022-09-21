from flask import redirect, render_template, url_for, flash, request, session, current_app
import secrets, os

from shop import db, app, photos
from .models import Brand, Category, Addproduct
from .forms import AddProducts

@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    """ if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))  """

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
    """ if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))  """

    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)
        flash(f'The Category {getcat} was added to your database', 'sucess')
        db.session.commit()
        return redirect(url_for('addcat'))

    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    """ if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))  """

    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddProducts(request.form)

    if request.method =='POST':
        name= form.name.data
        price= form.price.data
        discount= form.discount.data
        stock= form.stock.data
        colors= form.colors.data
        desc= form.discription.data
        brand= request.form.get('brand')
        category= request.form.get('category')

        image_1=photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + '.')
        image_2=photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + '.')
        image_3=photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + '.')


        addpro = Addproduct(name=name,price=price,discount=discount, stock=stock, colors=colors, 
        desc=desc, brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpro)
        flash(f'The product {name} has been added to your database.', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html' , title='Add product page', form=form, brands=brands, categories= categories)

@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):
    """ if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))  """

    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatebrand.name = brand
        db.session.commit()
        flash(f'The brand {brand} has been updated.', 'success')
        return redirect(url_for('brands'))

    return render_template('products/updatebrand.html', title='Update brands', updatebrand=updatebrand)

@app.route('/updatecategory/<int:id>', methods=['GET', 'POST'])
def updatecategory(id):
    """ if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))  """

    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')

    if request.method == 'POST':
        updatecategory.name = category
        db.session.commit()
        flash(f'The category {category} has been updated.', 'success')
        return redirect(url_for('category'))

    return render_template('products/updatebrand.html', title='Update categories', updatecategory=updatecategory)

@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updatecategory(id):
    form = Addproduct(request.form):

    return render_template('products/updatebrand.html', title='Update categories', form=form)