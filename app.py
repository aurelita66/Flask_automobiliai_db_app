from models import db, Automobilis
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("searchlaukelis")
    if search_text:
        filtered_rows = Automobilis.query.filter(Automobilis.modelis.ilike(f"{search_text}%"))
        average_year = Automobilis().average_year
        return render_template("index.html", autos=filtered_rows, average_year=average_year)
    else:
        all_autos = Automobilis.query.all()
        average_year = Automobilis().average_year
        return render_template("index.html", autos=all_autos, average_year=average_year)


@app.route("/automobilis/<int:row_id>")
def one_auto(row_id):
    auto = Automobilis.query.get(row_id)
    if auto:
        return render_template("one_auto.html", auto=auto)
    else:
        return f"Automobilis su id {row_id} neegzistuoja"


@app.route("/automobilis/redaguoti/<int:row_id>", methods=["get", "post"])
def update_auto(row_id):
    auto = Automobilis.query.get(row_id)
    if not auto:
        return f"Automobilis su id {row_id} neegzistuoja"

    if request.method == "GET":
        return render_template("update_auto_form.html", auto=auto)

    elif request.method == "POST":
        gamintojas = request.form.get("gamintojaslaukelis")
        modelis = request.form.get("modelislaukelis")
        spalva = request.form.get("spalvalaukelis")
        metai = int(request.form.get("metailaukelis"))
        auto.gamintojas = gamintojas
        auto.modelis = modelis
        auto.spalva = spalva
        auto.metai = metai
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/automobilis/trynimas/<int:row_id>", methods=["POST"])
def delete_auto(row_id):
    auto = Automobilis.query.get(row_id)
    if not auto:
        return f"Automobilis su id {row_id} neegzistuoja"
    else:
        db.session.delete(auto)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/automobilis/naujas", methods=["GET", "POST"])
def create_auto():
    if request.method == "GET":
        return render_template("create_auto_form.html")
    if request.method == "POST":
        gamintojas = request.form.get("gamintojaslaukelis")
        modelis = request.form.get("modelislaukelis")
        spalva = request.form.get("spalvalaukelis")
        metai = int(request.form.get("metailaukelis"))
        if gamintojas and modelis and spalva and metai:
            new_auto = Automobilis(gamintojas=gamintojas, modelis=modelis, spalva=spalva, metai=metai)
            db.session.add(new_auto)
            db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(port=5001, debug=True)
