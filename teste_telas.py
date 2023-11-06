import sqlite3


def crypt():
  key_encryption = "Ravi"
  path_db = "venv\\Lib\\site-packages\\.lt\\temp\\sqlite\\cryptograf\\.manager.db"
  conn = pysqlcipher3.connect(path_db)

  conn.execute(f"ATTACH DATABASE '{path_db}' AS encrypted KEY '{key_encryption}'")

  conn.execute("SELECT sqlcipher_export('encrypted')")

  conn.execute("DETACH DATABASE encrypted")
  conn.commit()
  conn.close()

crypt()