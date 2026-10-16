def save_observations_to_db(observations, conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            observer TEXT,
            filter_name TEXT,
            exposure REAL
        )
    """)

    for obs in observations:
        cursor.execute("""
            INSERT INTO observations
            (target, observer, filter_name, exposure)
            VALUES (?, ?, ?, ?)
        """, (
            obs.target,
            obs.observer,
            obs.filter,
            obs.exposure
        ))

    conn.commit()
    print("All observations saved successfully.")