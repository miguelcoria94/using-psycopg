import psycopg2

CONNECTION_PARAMETERS = {
    'dbname': 'psycopg_test_db',
    'user': 'psycopg_test_user',
    'password': 'password',
}

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    print(conn.get_dsn_parameters())
