from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import sys
from .web_scrapers.data_getter import GetAllContent 


bp = Blueprint('data', __name__)

#@bp.route('/index', methods=('GET', 'POST'))
def initialize_data():
    all = GetAllContent()
    dba,fmf,gundam = all['blue_alliance'], all['fmf_news'], all['gundam']
    print(dba)
    print(fmf)
    print(gundam)
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
    print(dba)
    for item in dba:
        print(item)
        db.execute(
            '''
            INSERT INTO regional (event, url, direction)
            VALUES (?, ?, ?);
            ''',
            (item['event'], item['url'], item['direction'])
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

@bp.route('/dba', methods=('GET',))
@login_required
def dba():
    db = get_db()
    dba = db.execute(
        '''
        SELECT * FROM regional;
        '''
    ).fetchall()
    return render_template('main/dba.html', posts = dba)
@bp.route('/fmf', methods=('GET',))
@login_required
def fmf():
    db = get_db()
    fmf = db.execute(
        '''
        SELECT * FROM fmf_news;
        '''
    ).fetchall()
    return render_template('main/fmf.html', posts = fmf)

@bp.route('/gundam', methods=('GET',))
@login_required
def gundam():
    db = get_db()
    gundam = db.execute(
        '''
        SELECT * FROM gundam;
        '''
    ).fetchall()
    return render_template('main/gundam.html', posts = gundam)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))