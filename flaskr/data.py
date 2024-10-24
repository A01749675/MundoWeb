from flask import (
   Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from flaskr.auth import login_required
from flaskr.db import get_db
import sys
from .web_scrapers.data_getter import GetAllContent


bp = Blueprint('data', __name__)


def initialize_data():
   all = GetAllContent()
   dba, fmf, gundam = all['blue_alliance'], all['fmf_news'], all['gundam']


   db = get_db()
   db.execute('DELETE FROM regional;')
   db.execute('DELETE FROM fmf_news;')
   db.execute('DELETE FROM gundam;')


   for item in dba:
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
   titles = []
   dba, fmf, gundam = [], [], []


   if g.user:
       if g.user['regional']:
           dba = db.execute('SELECT * FROM regional;').fetchall()
           titles.append("Robotics")
       if g.user['fmf']:
           fmf = db.execute('SELECT * FROM fmf_news;').fetchall()
           titles.append("Sports")
       if g.user['gundam']:
           gundam = db.execute('SELECT * FROM gundam;').fetchall()
           titles.append("Gundam")
   else:
       titles = ["Robotics", "Sports", "Gundam"]
       dba = db.execute('SELECT * FROM regional;').fetchall()
       fmf = db.execute('SELECT * FROM fmf_news;').fetchall()
       gundam = db.execute('SELECT * FROM gundam;').fetchall()


   return render_template('main/index.html', dba=dba, fmf=fmf, gundam=gundam, titles=titles)


@bp.route('/dba', methods=('GET', 'POST'))
@login_required
def dba():
   if not g.user['regional']:
       return render_template('main/subscribe.html', category='regional')
  
   db = get_db()
   dba = db.execute('SELECT * FROM regional;').fetchall()
   return render_template('main/dba.html', posts=dba)


@bp.route('/fmf', methods=('GET', 'POST'))
@login_required
def fmf():
   if not g.user['fmf']:
       return render_template('main/subscribe.html', category='fmf')
  
   db = get_db()
   fmf = db.execute('SELECT * FROM fmf_news;').fetchall()
   return render_template('main/fmf.html', posts=fmf)


@bp.route('/gundam', methods=('GET', 'POST'))
@login_required
def gundam():
   if not g.user['gundam']:
       return render_template('main/subscribe.html', category='gundam')
  
   db = get_db()
   gundam = db.execute('SELECT * FROM gundam;').fetchall()
   return render_template('main/gundam.html', posts=gundam)


@bp.route('/subscribe/<category>', methods=('POST',))
@login_required
def subscribe(category):
   db = get_db()
   db.execute(
       f'UPDATE user SET {category} = 1 WHERE id = ?', (g.user['id'],)
   )
   db.commit()
  
   # Recargar el usuario actualizado en g.user
   g.user = db.execute(
       'SELECT * FROM user WHERE id = ?', (g.user['id'],)
   ).fetchone()
  
   return redirect(url_for('index'))