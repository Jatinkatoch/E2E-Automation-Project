from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

import random
import datetime
from database import db
from models import Product,User


app=Flask(__name__)

app.secret_key="techstore-secret-key-2026"


app.config[
"SQLALCHEMY_DATABASE_URI"
]="sqlite:///store.db"


db.init_app(app)



with app.app_context():

    db.create_all()


    if Product.query.count()==0:


        products=[


        Product(
        name="Gaming Laptop",
        category="Laptop",
        price=85000,
        rating=4.8,
        image="https://images.unsplash.com/photo-1603302576837-37561b2e2302",
        description="High performance gaming laptop"
        ),



        Product(
        name="MacBook Pro",
        category="Laptop",
        price=150000,
        rating=4.9,
        image="https://images.unsplash.com/photo-1517336714731-489689fd1ca8",
        description="Apple professional laptop"
        ),



        Product(
        name="Wireless Headphones",
        category="Accessories",
        price=5000,
        rating=4.5,
        image="https://images.unsplash.com/photo-1505740420928-5e560c06d30e",
        description="Noise cancelling headphones"
        ),



        Product(
        name="Mechanical Keyboard",
        category="Accessories",
        price=7000,
        rating=4.7,
        image="https://images.unsplash.com/photo-1587829741301-dc798b83add3",
        description="RGB gaming keyboard"
        )


        ]

        db.session.add_all(products)
        db.session.commit()

    if User.query.count()==0:

        user = User(
            name="Test User",
            email="test@gmail.com",
            password="Test@12345"
        )

        db.session.add(user)
        db.session.commit()

@app.route("/")
def home():

    products=Product.query.all()

    return render_template(
        "home.html",
        products=products
    )



@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing = User.query.filter_by(email=email).first()

        if existing:
            flash("Email already registered.", "danger")
            return redirect("/register")

        user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.", "success")

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:

            session["user"] = user.email

            flash("Login Successful!", "success")

            return redirect("/")

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")



@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/product/<int:id>")
def product_details(id):

    product = db.session.get(Product, id)

    if not product:
        flash("Product not found", "danger")
        return redirect("/")

    return render_template(
        "product.html",
        product=product
    )

@app.route("/add/<int:id>")
def add(id):

    product = db.session.get(Product, id)

    if not product:
        flash("Product not found", "danger")
        return redirect("/")

    cart = session.get("cart", [])


    found = False


    for item in cart:

        if item["id"] == product.id:

            item["quantity"] += 1

            found = True

            break



    if not found:

        cart.append({

            "id": product.id,

            "name": product.name,

            "price": product.price,

            "image": product.image,

            "quantity": 1

        })


    session["cart"] = cart


    return redirect("/checkout")




@app.route("/checkout")
def checkout():

    cart=session.get(
        "cart",
        []
    )

    total=sum(
       x["price"] * x["quantity"]
       for x in cart
)

    return render_template(
        "checkout.html",
        cart=cart,
        total=total
    )

@app.route("/order", methods=["GET", "POST"])
def order():
    if "user" not in session:
        flash("Please login before placing an order.", "warning")
        return redirect("/login")

    cart = session.get("cart", [])

    if not cart:
        flash("Your cart is empty.", "warning")
        return redirect("/")

    if request.method == "POST":

        order_number = random.randint(
            100000,
            999999
        )

        total = sum(
            item["price"] * item["quantity"]
            for item in cart
        )

        session.pop("cart", None)

        return render_template(
            "ordersuccess.html",
            order_number=order_number,
            total=total,
            customer=request.form["name"],
            date=datetime.date.today()
        )

    total = sum(
        item["price"] * item["quantity"]
        for item in cart
    )

    return render_template(
        "order.html",
        cart=cart,
        total=total
    )

@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    cart=session.get(
        "cart",
        []
    )


    action=request.form["action"]


    for item in cart:

        if item["id"] == id:


            if action=="increase":

                item["quantity"] += 1



            elif action=="decrease":

                if item["quantity"] > 1:

                    item["quantity"] -= 1



    session["cart"]=cart


    return redirect("/checkout")
@app.route("/remove/<int:id>")
def remove(id):

    cart=session.get(
        "cart",
        []
    )


    cart=[
        item for item in cart
        if item["id"] != id
    ]


    session["cart"]=cart


    return redirect("/checkout")

@app.route("/clear")
def clear():

    session.pop(
        "cart",
        None
    )

    return redirect("/checkout")



if __name__=="__main__":

    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)