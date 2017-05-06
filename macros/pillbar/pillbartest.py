from flask import Flask, render_template

from macros.pillbar.pillbar_classes import SearchPill, TablePill

app = Flask(__name__)


@app.route('/')
def hello_world():
    pill1 = SearchPill()
    pill1.makepill('myclass', 'data', 'user', 'Profile')
    pill1.load_table([])
    pill1.fillpill('data.0', 'profile_stuff', 'profile', 5)
    pill2 = TablePill()
    pill2.makepill('myclass', 'things', 'user', 'Stuff')
    pill2.load_table([])
    pill2.fillpill('theid', 'stuff')
    return render_template('pillbar/',
                           pill1=pill1.export_pill(),
                           pill2=pill2.export_pill())


if __name__ == '__main__':
    app.run()
