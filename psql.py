import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        # Создание таблицы клиентов
        cur.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE
            )
        ''')

        # Создание таблицы телефонов
        cur.execute('''
            CREATE TABLE IF NOT EXISTS phones (
                id SERIAL PRIMARY KEY,
                client_id INTEGER REFERENCES clients(id) ON DELETE CASCADE,
                phone_number VARCHAR(20) NOT NULL
            )
        ''')

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute('''
            INSERT INTO clients (first_name, last_name, email)
            VALUES (%s, %s, %s)
            RETURNING id
        ''', (first_name, last_name, email))
        client_id = cur.fetchone()[0]

        if phones:
            for phone in phones:
                cur.execute('''
                    INSERT INTO phones (client_id, phone_number)
                    VALUES (%s, %s)
                ''', (client_id, phone))

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute('''
            INSERT INTO phones (client_id, phone_number)
            VALUES (%s, %s)
        ''', (client_id, phone))

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        if first_name:
            cur.execute('''
                UPDATE clients
                SET first_name = %s
                WHERE id = %s
            ''', (first_name, client_id))

        if last_name:
            cur.execute('''
                UPDATE clients
                SET last_name = %s
                WHERE id = %s
            ''', (last_name, client_id))

        if email:
            cur.execute('''
                UPDATE clients
                SET email = %s
                WHERE id = %s
            ''', (email, client_id))

        if phones:
            # Удаление старых телефонов
            cur.execute('''
                DELETE FROM phones
                WHERE client_id = %s
            ''', (client_id,))

            # Добавить телефон
            for phone in phones:
                cur.execute('''
                    INSERT INTO phones (client_id, phone_number)
                    VALUES (%s, %s)
                ''', (client_id, phone))

def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute('''
            DELETE FROM phones
            WHERE client_id = %s AND phone_number = %s
        ''', (client_id, phone))

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute('''
            DELETE FROM clients
            WHERE id = %s
        ''', (client_id,))

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute('''
            SELECT clients.id, first_name, last_name, email, phone_number
            FROM clients
            LEFT JOIN phones ON clients.id = phones.client_id
            WHERE first_name = %s OR last_name = %s OR email = %s OR phone_number = %s
        ''', (first_name, last_name, email, phone))
        return cur.fetchall()

with psycopg2.connect(database="netology_db", user="postgres", password="ADIdas1322") as conn:
    create_db(conn)

    # Пример использования функций
    add_client(conn, 'Антон', 'Клепиковский', 'antonyklep@example.com', phones=['79999998888', '79999997777'])
    add_phone(conn, 1, '79999996666')
    change_client(conn, 1, last_name='Иванов')
    delete_phone(conn, 1, '79999998888')
    result = find_client(conn, last_name='Иванов')
    print(result)

conn.close()