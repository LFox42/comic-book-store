

#Build log for Sign up web page
#Ver 1.1 - Created TEST data for Ticket variable
#Ver 1.2 - Adding server functionality to python


from bottle import run, route, view, get, post, request, static_file
from itertools import count

###Class START WITH CAPITAL LETTERS

class Comic:
    
    # _ signifies a private variable. not to be used outside of this class.
    _ids = count (0)
    
    def __init__(self, name, image, amount): 
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = name
        self.image = image
        self.amount = amount


#Test Data
comic = [
    Comic("Superdude", "image", 8),
    Comic("Lizard Man", "image", 12),
    Comic("Water Woman", "image",3)
    ]

#Pages

#index page
@route('/')
@view ('index')
def index():
    #need this function to attach the decorators above.
    pass


@route('/Purchase_Page')
@view ('Purchase_Page')
def Purchase():
    #buy and restock books
    data = dict (comic_list = comic)
    return data

@route('/purchase-success/<Comic_id>')
@view('purchase-success')
def purchase_success(Comic_id):
    Comic_id = int(Comic_id)
    found_comic = None
    for Comic in comic:
        if Comic.id == Comic_id:
            found_comic = Comic
    data = dict (Comic = found_comic)
    found_comic.purchase = Comic.amount - 1
    return data

@route('/restock/<Comic_id>')
@view('restock')
def Restock(Comic_id):
    Comic_id = int(Comic_id)
    found_comic = None
    for Comic in comic:
        if Comic.id == Comic_id:
            found_comic = Comic
    data = dict (Comic = found_comic)
    found_comic.purchase = Comic.amount = 100
    return data    

@route ('/picture/<filename>')
def serve_picture (filename):
    return static_file (filename, root = '/images')

run(host='0.0.0.0', port = 8080, reloader=True, debug=True)