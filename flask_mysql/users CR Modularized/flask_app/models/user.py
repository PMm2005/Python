from flask_app.config.mysqlconnection import connectToMySQL


class users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #read all users
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users;"
        results = connectToMySQL("users").query_db(query)

        print(results)

        user_instances = []
        for row in results:
            this_user = cls(row)
            user_instances.append(this_user)
        return user_instances
    
    #create user
    @classmethod
    def create(cls, data):
        print ("******************", data)

        q = """
            INSERT INTO users (first_name, last_name, email)
            VALUES (%(First_Name)s, %(Last_Name)s, %(Email)s); 
            """
        return connectToMySQL("users").query_db(q, data)

