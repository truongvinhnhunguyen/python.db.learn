import psycopg2
from config import config


def insert_person(person_name):
    """ insert a new person into the Persons table """
    sql = """INSERT INTO persons(Name)
             VALUES(%s) RETURNING ID;"""
    conn = None
    person_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (person_name,))
        # get the generated id back
        person_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return person_id


if __name__ == '__main__':
    print(insert_person("Truong Vinh Nhu Nguyen"))
