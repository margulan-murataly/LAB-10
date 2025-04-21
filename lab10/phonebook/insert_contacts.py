import psycopg2
from config import load_config


def insert_contact(first_name, phone_number):
    """ Insert a new contact into the contacts table """

    sql = """INSERT INTO contacts(first_name)
             VALUES(%s) RETURNING contact_id;"""

    contact_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:  
                cur.execute(sql, (first_name,))

                rows = cur.fetchone()
                if rows:
                    contact_id = rows[0]
                    
                cur.execute(
                    "INSERT INTO phone_numbers (contact_id, phone_number) VALUES (%s, %s)",
                    (contact_id, phone_number)
                )

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return contact_id
    
def insert_many_contacts(contact_list):
    """ Insert multiple contacts into the contacts table  """

    contact_sql = "INSERT INTO contacts(first_name) VALUES(%s) RETURNING contact_id"
    phone_sql = "INSERT INTO phone_numbers (contact_id, phone_number) VALUES (%s, %s)"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                for first_name, phone_number in contact_list:
                    cur.execute(contact_sql, (first_name,))
                    rows = cur.fetchone()
                    if rows:
                        contact_id = rows[0]

                    cur.execute(phone_sql, (contact_id, phone_number))
                
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    insert_contact("margulan", "+77020711054")
    
    insert_many_contacts([
        ('Sake', '+77077170770'),
        ('Bake', '+77777077007'),
        ('Ereke', '+77011017171'),
        ('Make', '+77177771771'),
        ('Nureke', '+77777777777'),
        ('Make', '+77177771771'),
        ('Nureke', '+77777777777')
    ])