

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
    Comic("Superdude", "image", "8"),
    Comic("Lizard Man", "image", "12"),
    Comic("Water Woman", "image", "3")
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


@route ('/picture/<filename>')
def serve_picture (filename):
    return static_file (filename, root = '/images')

run(host='0.0.0.0', port = 8080, reloader=True, debug=True)