import psycopg2
from config import load_config

#fetchone()

def get_vendors():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                print("The number of parts: ", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_vendors()
    
print("========================================")

#fetchall()

def get_vendors_all():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors WHERE vendor_id > 5")
                rows = cur.fetchall()

                print("The number of parts: ", cur.rowcount)
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_vendors_all()
    

    
print("=============================================")


#fetchmany()

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_part_vendors():
    """ Retrieve data from the vendors table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT part_name, vendor_name
                    FROM parts
                    INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
                    INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
                    ORDER BY part_name;
                """)
                for row in iter_row(cur, 10):
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_part_vendors()