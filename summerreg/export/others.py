def mysql_get_cursor(user, passwd, db):
    import MySQLdb
    from MySQLdb import cursors
    conn = MySQLdb.connect(
    user="user",
    passwd="password",
    db="contrib",
    cursorclass = cursors.SSCursor                                                  )
    return conn.cursor()


