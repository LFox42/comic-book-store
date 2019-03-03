

#Build log for Sign up web page
#Ver 1.1 - Created TEST data for Ticket variable
#Ver 1.2 - Adding server functionality to python


from bottle import run, route, view, get, post, request
from itertools import count

###Class START WITH CAPITAL LETTERS

class Ticket:
    
    # _ signifies a private variable. not to be used outside of this class.
    _ids = count (0)
    
    def __init__(self, name, email, date_of_birth, check_in): 
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in


#Test Data
comics = [
    Comic("Matt Evans", "mevans@stc.school.nz","27.01.1988", False),
    Comic("Superman", "superman@stc.school.nz", "15.12.1978", False),
    Comic("Batman", "batman@stc.school.nz", "23.07.1989",False),
    Comic("Hulk", "hulk@stc.school.nz", "26.06.2003",False)
    ]

#Pages

#index page
@route('/')
@view ('index')
def index():
    #need this function to attach the decorators above.
    pass


run(host='0.0.0.0', port = 8080, reloader=True, debug=True)