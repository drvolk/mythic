'''
Created on 19.01.2015

@author: Dirk.Voelcker
'''
class game_field(object):
    
    __length = 0
    __width = 0
    __rooms = ()
    
    def __init__(self, length, width):    
        self.__length = length
        self.__width = width

    def set_background(self):
        pass
    
    def set_room(self, game_room, x, y):
        pass
    
class game_view(game_field):
    __v_length = 0
    __v_width = 0
    
    def __init__(self, length, width, v_length, v_width):
        super.__init__(length, width)
        __v_length = v_length
        __v_width = v_width
    
    def show_view(self):
        pass
    
    def set_view(self, x, y):
        pass

class game_token(object):
    '''
    classdocs
    '''
    __name=None
    __type=None
    __picture=None
    __pos = (0,0)
    
    def __init__(self, name, token_type):
        '''
        Constructor
        '''
        self.__name = name
        self.__type = token_type
        self.load_picture(name)
    
    def load_picture(self, filename):
        self.__picture = filename
    
    def set_pos(self,x,y):
        self.__pos[0]=x
        self.__pos[1]=y
    
    def display_picture(self):
        pass
    
    def hide_picture(self):
        pass