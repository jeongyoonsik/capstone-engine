# get result feed - get from DB?
# loop through feed, combine as follows
# if timestamp is within a half second of the previous timestamp + processing time,
# add combine the candidates arrays
#
# continue, separating into groups.

# form "new" result entries, where the results will be *hopefully* more accurate


from plate import Plate
import sqlite3
import json


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('/path/to/db')

db.row_factory = dict_factory
cur = db.cursor()
cur.execute("SELECT * FROM plates")
dbplates = cur.fetchall()
db.close()

plates = []

for dbplate in dbplates:
    print(dbplate['plate'])
    plate = Plate(dbplate['plate'], dbplate['entrance_time'], dbplate['confidence'],
                  dbplate['location'], json.loads(dbplate['candidates']),
                  dbplate['processing_time'], dbplate['plate_processing'])
    plates.append(plate)

prev = None
first = None
newplates = []

for each in plates:
    if prev is None:
        first = each
        prev = each
    else:
        if float(prev.entrance_time) + float(prev.plate_processing) + float(prev.processing_time) >= float(each.entrance_time):
            print(each.entrance_time)
            first.add_candidates(each.candidates)
        else:
            print(each.plate)
            newplates.append(first)
            first = each
        prev = each
newplates.append(first)
for each in newplates:
    each.debug_print()
    # print(each.candidates)
