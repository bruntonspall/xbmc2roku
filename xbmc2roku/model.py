import pymysql

def tvshow(row):
    return dict(
        id=row['idShow'], 
        name=row['c00'], 
        description=row['c01'].decode('cp1252'),
        url='http://test/')

def episode(row):
    return dict(
        id=row['idEpisode'], 
        name=row['c00'], 
        description=row['c01'].decode('cp1252'), 
        season=row['c12'], 
        episode=row['c13'], 
        url='http://localhost:6543/media/%s/%s' % (row['idShow'], row['idEpisode']),
        length=0)

def get_all_shows(db):
    cur = db.cursor(pymysql.cursors.DictCursor)
    rs = cur.execute("select * from tvshowview order by c00 ASC")
    return [tvshow(row) for row in cur.fetchall()]

def get_show(db, id):
    cur = db.cursor(pymysql.cursors.DictCursor)
    rs = cur.execute("select * from tvshowview where idShow = %s",id)
    return tvshow(cur.fetchone())

def get_all_episodes(db, show_id):
    cur = db.cursor(pymysql.cursors.DictCursor)
    rs = cur.execute("select * from episodeview where idShow = %s order by dateAdded DESC", show_id)
    return [episode(row) for row in cur.fetchall()]

def get_episode(db, show_id, episode_id):
    cur = db.cursor(pymysql.cursors.DictCursor)
    rs = cur.execute("select c18 from episodeview where idShow = %s and idEpisode = %s", (show_id, episode_id))
    return episode(cur.fetchone())

