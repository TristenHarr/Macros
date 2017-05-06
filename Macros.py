from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('operate/workspace.html',
                           kwargs={'pill-class': 'myclass',
                                   'pill-id': 'data',
                                   'pill-glyph': 'trash',
                                   'pill-title': 'My Data',
                                   'pill-type': 'searchtable',
                                   'pill-contents':
                                       {'id': 'data.0',
                                        'database_location': 'data_sets',
                                        'multilabel': 'Things',
                                        'contents': [['abcbc'], ['bcc'], ['c'], ['d'], ['ef'], ['hik'], ['hey']],
                                        'display-limit': 5
                                        }
                                   }
                           )


if __name__ == '__main__':
    app.run()
