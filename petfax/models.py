from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


class Fact(db.Model):
    __tablename__ =  'facts' 
    
    id = db.Column(db.Integer, primary_key = True) 
    submitter = db.Column(db.String(250)) 
    fact = db.Column(db.Text) 

@bp.route('/<int:id>')
def show(id): 
    user = models.User.query.filter_by(id=id).first()
    user_dict = {
        'username': user.username
    }

    return user_dict
