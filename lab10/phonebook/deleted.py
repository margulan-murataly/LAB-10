import psycopg2
from config import load_config


def delete_contact(first_name):
    """ Delete part by part id """

    rows_deleted  = 0
    sql = 'DELETE FROM contacts WHERE first_name = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (first_name,))
                rows_deleted = cur.rowcount

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted

if __name__ == '__main__':
    deleted_rows = delete_contact("Make")
    print('The number of deleted rows: ', deleted_rows)