from flask import render_template, request
from app import dao
from app import app


@app.route('/')
def index():
    cate_id = request.args.get("category_id")

    products = dao.load_products(cate_id=cate_id)

    categories = dao.load_categories()

    return render_template('index.html',
                           categories=categories,
                           products=products)


if __name__ == '__main__':
    app.run(debug=True)