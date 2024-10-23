from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

from web_scrapers.data_getter import get_data

bp = Blueprint('blog', __name__)


def initialize_data():
    dba, fmf, gundam = get_data()
    db = get_db()
    db.execute(
        '''
        DELETE FROM regional;
        '''
    )
    db.execute(
        '''
        DELETE FROM fmf_news;
        '''
    )
    db.execute(
        '''
        DELETE FROM gundam;
        '''
    )
    for item in dba:
        db.execute(
            '''
            INSERT INTO regional (title, description, date, link)
            VALUES (?, ?, ?, ?);
            ''',
            (item['title'], item['description'], item['date'], item['link'])
        )
    for item in fmf:
        db.execute(
            '''
            INSERT INTO fmf_news (title, description, date, link)
            VALUES (?, ?, ?, ?);
            ''',
            (item['title'], item['description'], item['date'], item['link'])
        )
    for item in gundam:
        db.execute(
            '''
            INSERT INTO gundam (title)
            VALUES (?);
            ''',
            (item,)
        )
    db.commit()

@bp.route('/')
def index():
    initialize_data()
    db = get_db()
    dba = db.execute(
        '''
        SELECT * FROM regional;
        '''
    ).fetchall()
    fmf = db.execute(
        '''
        SELECT * FROM fmf_news;
        '''
    ).fetchall()
    gundam = db.execute(
        '''
        SELECT * FROM gundam;
        '''
    ).fetchall()
    return render_template('main/index.html', dba = dba, fmf = fmf, gundam = gundam)

