from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__(self,data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * from dojos;"
        results  = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row in results:
            dojo = cls(row)
            all_dojos.append(dojo)
        return all_dojos

    @classmethod
    def create(cls,data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        result  = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM dojos WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])