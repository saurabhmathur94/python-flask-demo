from flask import request, redirect, url_for, render_template, jsonify

from app import app, db
from app.models import Teacher


@app.route("/", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        address = request.form.get("address")
        teacher = Teacher(
            name=name,
            age=age,
            address=address
        )
        print(teacher)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('teacher', teacher_id=teacher.id))
    return render_template("insert.html")


@app.route("/teacher/<teacher_id>", methods=["GET"])
def teacher(teacher_id):
    teacher = Teacher.query.get(int(teacher_id))
    return jsonify(teacher.tojson)


@app.route("/teachers", methods=["GET"])
def teachers():
    teachers = Teacher.query.all()

    json_list = []
    for teacher in teachers:
        json_list.append(teacher.tojson)

    return jsonify(json_list)
