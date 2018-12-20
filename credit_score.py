from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SECRET_KEY'] = 'thisissupposedtobesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///credit_score.db"
app.config['MONGO_DBNAME'] = 'mongologinexample'

db=SQLAlchemy(app)

class addField(db.Model):
	__tablename__ = " addField"
	id = db.Column (db.Integer, primary_key = True)
	name = db.Column(db.Text)
	type = db.Column (db.Boolean, default=False)



@app.route('/fields', methods=["GET", "POST"])
def addField():
	if request.method == "POST " :
		name = request.form ['addField']
		type = request.form ['type']
		if not addField.query.filter_by (name=name).first():
			new = addField(name=name, type=type)
			db.session.add(new)
			db.session.commit()
			
		



if __name__ == '__main__':
	app.run(port=0000, debug=True)
