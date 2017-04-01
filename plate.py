import json
import sqlite3
import os
from operator import itemgetter


class Plate(object):
    plate = ""
    confidence = ""
    entrance_time = ""
    location = ""
    processing_time = ""
    plate_processing = ""
    candidates = []

    def __init__(self, plate, entrance_time, confidence, location, candidates, processing_time, plate_processing):
        self.plate = plate
        self.entrance_time = entrance_time  # convert time?
        self.confidence = confidence
        self.location = location
        self.candidates = candidates
        self.processing_time = processing_time
        self.plate_processing = plate_processing

    def debug_print(self):
        print("Plate: ", self.plate)
        print("Confidence: ", self.confidence)
        print("Entrance Time: ", self.entrance_time)
        print("Processing Time: ", self.processing_time)
        print("Plate Time: ", self.plate_processing)
        # print("LotId: ", self.location)
        # print("candidates: ", self.candidates)

    def add_candidates(self, new_candidates):
        candidate_array = self.candidates
        for new_candidate in new_candidates:
            found = False
            for candidate in candidate_array:
                if new_candidate['plate'] == candidate['plate']:
                    found = True
                    if float(new_candidate['confidence']) > float(candidate['confidence']):
                        candidate['confidence'] = new_candidate['confidence']
            if found is False:
                candidate_array.append(new_candidate)
        new_candidate_array = sorted(candidate_array, key=itemgetter('confidence'), reverse=True)
        # if self.plate != new_candidate_array[0]['plate']:
        #     print('updating plate')
        self.plate = new_candidate_array[0]['plate']
        self.confidence = new_candidate_array[0]['confidence']
        self.candidates = new_candidate_array

    def check_candidate_size(self):
        verified_plates = []
        for each in self.candidates:
            if len(each['plate']) >= 6:
                verified_plates.append(each)
        self.candidates = verified_plates

    def write_to_db(self):
        # pass
        other_possiblilties = json.dumps(self.candidates)
        db = sqlite3.connect('/path/to/db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO plates(plate, confidence, entrance_time,
                          processing_time, plate_processing, location, candidates)
                          VALUES(?,?,?,?,?,?,?)
                          ''', (self.plate, self.confidence, self.entrance_time,
                                self.processing_time, self.plate_processing,
                                self.location, other_possiblilties))
        db.commit()
        db.close()

        # make_db_call(sql)


def make_db_call(sql):
    db = sqlite3.connect('/path/to/db')
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()


def create_plate_db():
    # make_db_call('DROP TABLE plates')
    sql = """Create Table plates(id INTEGER PRIMARY KEY, plate TEXT,
                                 confidence REAL, entrance_time TEXT,
                                 processing_time TEXT, plate_processing TEXT,
                                 location TEXT, candidates TEXT)"""
    make_db_call(sql)
