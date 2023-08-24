#!/usr/bin/python3
"""This modr hbnb clone"""
import json


class FileStorage:
    """Thi JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Retuype
        Args:
            cls (BaseModel object to lis
        Returns:
            all_ols`.
        """
        if cls is None:
            return self.__objects
        else:
            all_of_class = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    all_of_class[key] = value
            return all_of_class

    def new(self, obj):
        """Adds n dictionary"""
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Save to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads stfile"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletexists"""
        try:
            if obj:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
        except ValueError:
            pass

    def close(self):
        """ File stog JSON file
        Project: gines
        """
        self.reload()
