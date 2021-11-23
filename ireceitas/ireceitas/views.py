from flask import render_template, flash
from flask_login import current_user
from .blueprints.usuario.entidades import Receitas
# import json

def root():
    receitas = Receitas.query.all()
    nomes_receitas = [titulo.titulo for titulo in receitas]

    if not current_user.is_authenticated:
        flash("\nVocê não esta logado.")
    else:
        flash(f"\n\nOlá {current_user.name}, seja bem vindo(a).")
    return render_template('index.html', nomes_receitas=nomes_receitas)

