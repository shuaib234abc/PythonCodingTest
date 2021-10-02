from libraries.DbConnectivity import DbConnectivity
import psycopg2

# ref: https://www.w3schools.com/python/python_inheritance.asp

class DbConnectivityPlus(DbConnectivity):
#{

    def executeQueryWithoutParamsImmediately(self, query):
    #{

        # this code almost fully copied from https://www.psycopg.org/psycopg3/docs/usage.html
        with psycopg2.connect(self.connectionString) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                cur.execute(query)

                # Make the changes to the database persistent
                conn.commit()

    #}

    def getBinaryDataWithParams(self, query, params):
    #{
        data = None

        # this code almost fully copied from https://www.psycopg.org/psycopg3/docs/usage.html
        with psycopg2.connect(self.connectionString) as conn:

            # Open a cursor to perform database operations
            with conn.cursor() as cur:

                if(params is not None): cur.execute(query, params)
                else: cur.execute(query)

                # ref: https://stackoverflow.com/questions/40049046/how-to-read-and-insert-bytea-columns-using-psycopg2
                memoryview = cur.fetchone()
                print(memoryview)
                print(memoryview[0])
                data = bytes(memoryview[0])

        return data
    #}
#}