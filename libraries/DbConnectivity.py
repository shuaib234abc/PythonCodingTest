import psycopg2

"""
## references
1. https://www.psycopg.org/psycopg3/docs/usage.html
2. https://www.w3schools.com/python/python_classes.asp
"""

"""
for DB connectivity, we have used psycopg2 library (https://www.psycopg.org/), which is licensed under LGPL 3.0
License link: https://www.psycopg.org/docs/license.html
"""

class DbConnectivity:
#{

    def __init__(self):
    #{
        self.connectionString = "hostaddr=127.0.0.1 dbname=mydb user=postgres password=1234Pass"
    #}

    def executeQueryImmediatelyWithParams(self, query, params):
    #{

        # this code almost fully copied from https://www.psycopg.org/psycopg3/docs/usage.html
        with psycopg2.connect(self.connectionString) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                if(params is not None): cur.execute(query, params)
                else: cur.execute(query)

                # Make the changes to the database persistent
                conn.commit()

    #}

    def getSingleResultWithParams(self, query, params):
    #{
        data = None

        # this code almost fully copied from https://www.psycopg.org/psycopg3/docs/usage.html
        with psycopg2.connect(self.connectionString) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                if(params is not None): cur.execute(query, params)
                else: cur.execute(query)
                data = cur.fetchone()

        return data
    #}

    def getResultWithParams(self, query, params):
    #{
        data = None

        # this code almost fully copied from https://www.psycopg.org/psycopg3/docs/usage.html
        with psycopg2.connect(self.connectionString) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                if(params is not None): cur.execute(query, params)
                else: cur.execute(query)
                data = cur.fetchall()

        return data
    #}

    def getScalarResultWithParams(self, query, params):
    #{
        data = None

        # this code almost fully copied from https://www.psycopg.org/psycopg3/docs/usage.html
        with psycopg2.connect(self.connectionString) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                if(params is not None): cur.execute(query, params)
                else: cur.execute(query)

                data = cur.fetchone()
                return data[0]

    #}
#}
