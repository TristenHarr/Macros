from flask import Flask, render_template
from macros.pillbar.pillbar_classes import SearchPill, TablePill
app = Flask(__name__)




@app.route('/')
def hello_world():
    pill1 = SearchPill()
    pill1.makepill('myclass', 'data', 'user', 'Profile', '/links')
    pill1.load_table([[1],[2],[3]])
    pill1.fillpill('data.0', 'profile_stuff', 'profile', 5, '/stuff')
    pill2 = TablePill()
    pill2.makepill('myclass', 'things', 'user', 'Stuff')
    pill2.load_table([[1,2],[2,3],[3,4]])
    pill2.fillpill('theid', 'stuff')
    return render_template('pillbar/pillbartest.html',
                           pill1=pill1.export_pill(),
                           pill2=pill2.export_pill())


if __name__ == '__main__':
    app.run()


# class tablepill(object):
#     def __init__(self):
#         self.pill = None
#         self.pill_contents = None
#
#     def makepill(self, pillclass, pillid, pillglyph, pilltitle):
#         self.pill = { 'pill-class': pillclass,
#                       'pill-id': pillid,
#                       'pill-glyph': pillglyph,
#                       'pill-title': pilltitle,
#                       'pill-type': 'table'
#                     }
#
#     def load_table(self, table):
#         self.table_contents = table
#
#     def fillpill(self, contentid, multilabel, nonelabel="You don't have any"):
#         self.pill_contents = {
#             'id':contentid,
#             'contents':self.table_contents,
#             'multilabel':multilabel,
#             'nonelabel':nonelabel
#         }
#
#     def export_pill(self):
#         return {**self.pill, "pill-contents":self.pill_contents}
#
#
# class searchpill(object):
#
#     def __init__(self):
#         self.pill = None
#         self.table_contents = None
#         self.pill_contents = None
#         self.export = None
#
#     def makepill(self, pillclass, pillid, pillglyph, pilltitle):
#         self.pill = {'pill-class':pillclass,
#                      'pill-id':pillid,
#                      'pill-glyph':pillglyph,
#                      'pill-title':pilltitle,
#                      'pill-type': 'searchtable'
#                      }
#
#     def load_table(self, table_contents):
#         self.table_contents = table_contents
#
#     def fillpill(self, contentid, input_id, multilabel, displaylimit, nonelabel="You don't have any"):
#         self.pill_contents = {
#             'id': contentid,
#             'database_location': input_id,
#             'multilabel': multilabel,
#             'contents': self.table_contents,
#             'display-limit': displaylimit,
#             'nonelabel':nonelabel,
#         }
#
#     def export_pill(self):
#         return {**self.pill, "pill-contents":self.pill_contents}
