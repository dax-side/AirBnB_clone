#!/usr/bin/python3

'''This module defines all common attributes/methods for other classes'''

import uuid
from datetime import datetime


class BaseModel():
    ''' defines common attributes/methods for other classes

        Public Instance Attributes:
            id: (string) - assigned with an uuid when an instance is created.
            created_at: (datetime) - assigned with the current datetime when
                        an instance is created
            updated_at: (datetime) - assigned with the current datetime when
                        an instance is created and will be updated every time
                        the object changes
            __str__: prints: [<class name>] (<self.id>) <self.__dict__>

        Public Instance Methods:
            save(self): updates the public instance attribute updated_at with
                        the current datetime
            to_dict(self): returns a dictionary containing all keys/values of
                        __dict__ of the instance.
    '''
    def __init__(self):
        ''' Instantiates objects '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat('T')
        self.updated_at = datetime.now().isoformat('T')

    def __str__(self):
        ''' returns a formated string '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at with the
            current datetime
        '''
        self.updated_at = datetime.now().isoformat('T')

    def to_dict(self):
        '''
            returns a dictionary containing all keys/values of __dict__
            of the instance.
        '''
        return self.__dict__
