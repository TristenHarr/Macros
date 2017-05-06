class TablePill(object):
    def __init__(self):
        self.pill = None
        self.pill_contents = None
        self.table_contents = None

    def makepill(self, pillclass, pillid, pillglyph, pilltitle):
        self.pill = {'pill-class': pillclass,
                     'pill-id': pillid,
                     'pill-glyph': pillglyph,
                     'pill-title': pilltitle,
                     'pill-type': 'table',
                     }

    def load_table(self, table):
        self.table_contents = table

    def fillpill(self, contentid, multilabel, nonelabel="You don't have any"):
        self.pill_contents = {
            'id': contentid,
            'contents': self.table_contents,
            'multilabel': multilabel,
            'nonelabel': nonelabel,
        }

    def export_pill(self):
        return {**self.pill, "pill-contents": self.pill_contents}


class SearchPill(object):
    def __init__(self):
        self.pill = None
        self.table_contents = None
        self.pill_contents = None
        self.export = None

    def makepill(self, pillclass, pillid, pillglyph, pilltitle, pill_link):
        self.pill = {'pill-class': pillclass,
                     'pill-id': pillid,
                     'pill-glyph': pillglyph,
                     'pill-title': pilltitle,
                     'pill-type': 'searchtable',
                     'link': pill_link
                     }

    def load_table(self, table_contents):
        self.table_contents = table_contents

    def fillpill(self, contentid, input_id, multilabel, displaylimit, link, nonelabel="You don't have any"):
        self.pill_contents = {
            'id': contentid,
            'database_location': input_id,
            'multilabel': multilabel,
            'contents': self.table_contents,
            'display-limit': displaylimit,
            'nonelabel': nonelabel,
            'link': link
        }

    def export_pill(self):
        return {**self.pill, "pill-contents": self.pill_contents}
