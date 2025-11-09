from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

_pool = pooling.MySQLConnectionPool(
    pool_name="hotel_pool",
    pool_size=int(os.getenv("DB_POOL_SIZE", 5)),
    **DB_CONFIG
)

def get_connection():
    """Obtener conexión del pool. Devuelve un MySQLConnection."""
    conn = _pool.get_connection()
    try:
        conn.ping(reconnect=True, attempts=3, delay=1)
    except Exception:
        conn.close()
        raise
    return conn

def select(query, params=None):
    """Ejecuta un SELECT y retorna filas (lista de tuplas)."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
            cur.execute(query, params or ())
            return cur.fetchall()
        finally:
            cur.close()
    finally:
        conn.close()

def commit(query, params=None):
    """Ejecuta INSERT/UPDATE/DELETE y hace commit. Retorna affected rows."""
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
            cur.execute(query, params or ())
            conn.commit()
            return cur.rowcount
        finally:
            cur.close()
    finally:
        conn.close()
