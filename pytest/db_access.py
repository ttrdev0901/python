import psycopg2


def selectById():
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            res = cur.fetchall()

    return res