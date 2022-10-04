
from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app.models import ninja
class Dojo:

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        query = """
            INSERT INTO dojos
            (name)
            VALUES (%(name)s);
            """
        return connectToMySQL("dojos_ninjas_schema").query_db(query,data)

    @classmethod
    def return_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_ninjas_schema").query_db(query)
        dojo_objects = []
        for dojo_dictionary in results:
            dojo_obj = cls(dojo_dictionary)                                                                                                                                                                                                                                                                                                                             
            dojo_objects.append(dojo_obj)
        return dojo_objects

    @classmethod 
    def get_one_dojo_with_ninjas(cls, data):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas
        ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s
        """
        results = connectToMySQL("dojos_ninjas_schema").query_db(query, data)
        if len(results) == 0:
            return None
        else: 
            this_dojo_object = cls(results[0])
            for this_ninja in results:
                this_ninja_dictionary = {
                    "id": this_ninja["ninjas.id"],
                    "first_name": this_ninja["first_name"],
                    "last_name": this_ninja["last_name"],
                    "age": this_ninja["age"],
                    "created_at": this_ninja["ninjas.created_at"],
                    "updated_at": this_ninja["ninjas.updated_at"],
                }
                this_ninja_obj = ninja.Ninja(this_ninja_dictionary)
                this_dojo_object.ninjas.append(this_ninja_obj)
            return this_dojo_object