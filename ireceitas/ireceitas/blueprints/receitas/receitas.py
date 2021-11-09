from flask import Blueprint, render_template


bp = Blueprint('receitas', __name__, url_prefix='/receitas', template_folder='templates')


# @bp.route('/')
# def root():
#     return 'Hello from receitas'

@bp.route('/massas')
def massas():
    return render_template("MassasCarrossel.html")

@bp.route('/comidasfit')
def comidasfit():
    return render_template("ComidasFitnessCarrossel.html")

@bp.route('/sobremesas')
def sobremesas():
    return render_template("SobremesasCarrossel.html")

@bp.route('/acompanhamentos')
def acompanhamentos ():
    return render_template("acompanhamentos.html")

@bp.route('/cafedamanha')
def cafedamanha():
    return render_template("cafedamanha.html")

@bp.route('/comidasfitness')
def comidasfitness():
    return render_template("comidasfitness.html")

@bp.route('/comidasveganas')
def comidasveganas():
    return render_template("comidasveganas.html")

@bp.route('/docesesobremesas')
def docesesobremesas():
    return render_template("DoceseSobremesas.html")

@bp.route('/acompanhamentos1')
def acompanhamentos1():
    return render_template("1°acompanhamento_batata_assada.html")

def init_app(app):
    app.register_blueprint(bp)