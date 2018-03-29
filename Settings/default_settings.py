import randomcolor

from Settings.database import db_session
from orm.team_color import Team_color
from orm.map_status import Map_status
from map import Map
from settings import MAIN_PATH
import os
from os.path import join
from pathlib import Path

def clear_all_olds(map):
    # remain initial map
    new_map = Path(join(MAIN_PATH, "templates", 'new_' + map))
    if new_map.exists():
        os.remove(join(MAIN_PATH, 'templates', 'new_' + map))

    num_rows_deleted = db_session.query(Team_color).delete()
    print("[Deleted Rows] %d" % num_rows_deleted)
    num_rows_deleted = db_session.query(Map_status).delete()
    print("[Deleted Rows] %d" % num_rows_deleted)
    db_session.commit()

    # team_color table init setting
    rand_color = randomcolor.RandomColor()
    generated_color = rand_color.generate(count=20)

    # default color
    t = Team_color(str(-1), '#C8C8C8')
    db_session.add(t)

    for i in range(20):
        t = Team_color(str(i), str(generated_color[i]).upper())
        db_session.add(t)

    db_session.commit()

    db_session.execute('ALTER TABLE map_status AUTO_INCREMENT=1')
    db_session.commit()

    # map_status table init setting
    m = Map(join(MAIN_PATH, 'templates', map))
    for id in m.get_id():
        ms = Map_status('0', id, None, None, None)
        db_session.add(ms)

    db_session.commit()

if __name__ == '__main__':
    clear_all_olds()