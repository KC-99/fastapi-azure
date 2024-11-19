from databases import get_connection

def create_field(actor):
    query = """
    INSERT INTO actor (actor_id, first_name, last_name, last_update)
    VALUES (%s, %s, %s)
    """
    values = (actor.id, actor.first_name, actor.last_name, actor.last_update)
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
            actor_id = cursor.lastrowid
    finally:
        connection.close()
    return {"id": actor_id, **actor.dict()}

def get_field(actor_id):
    query = "SELECT actor_id, first_name, last_name, last_update FROM actor WHERE actor_id = %s"
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (actor_id,))
            result = cursor.fetchone()
    finally:
        connection.close()
    return result

def get_fields(skip=0, limit=10):
    query = "SELECT actor_id, first_name, last_name, last_update FROM actor LIMIT %s OFFSET %s"
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (limit, skip))
            results = cursor.fetchall()
    finally:
        connection.close()
    return results

def update_field(actor_id, updates):
    fields = ", ".join(f"{key} = %s" for key in updates.keys())
    query = f"UPDATE actor SET {fields} WHERE actor_id = %s"
    values = list(updates.values()) + [actor_id]
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
    finally:
        connection.close()
    return get_field(actor_id)

def delete_field(actor_id):
    query = "DELETE FROM actor WHERE actor_id = %s"
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (actor_id,))
            connection.commit()
    finally:
        connection.close()
    return {"message": f"Item {actor_id} deleted successfully"}
