from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app.models import dojo

class Ninja:
    def __init__(self, db_data):
        self.id = db_data["id"]
        self.first_name = db_data["first_name"]
        self.last_name = db_data["last_name"]
        self.age = db_data["age"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.dojo = None
    
    @classmethod
    def create_ninja(cls, data):
        query = """
            INSERT INTO ninjas
            (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
            """
        return connectToMySQL("dojos_ninjas_schema").query_db(query, data)

    @classmethod
    def get_a_dojo(cls):
        query = """
            SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;
            """
        results = connectToMySQL("dojos_ninjas_schema").query_db(query)
        all_dojo_objects = []
        if len(results) == 0:
            return []
        else:
            for single_dojo_dictionary in results:
                single_dojo_obj = cls(single_dojo_dictionary)
                this_dojo_dictionary = {
                    "id" : single_dojo_dictionary ["dojos.id"],
                    "name" : single_dojo_dictionary ["name"],
                    "created_at" : single_dojo_dictionary ["dojos.created_at"],
                    "updated_at" : single_dojo_dictionary ["dojos.updated_at"],
                }
                this_dojo_object = dojo.Dojo(this_dojo_dictionary)
                single_dojo_obj.dojo = this_dojo_object
                all_dojo_objects.append(single_dojo_obj)
            return all_dojo_objects