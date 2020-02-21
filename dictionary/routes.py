from flask import render_template, url_for, request
from dictionary import app
from dictionary.forms import SearchForm


@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    search = form.search.data

    return render_template('dictionary.html', search=search, form=form)

