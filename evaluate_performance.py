# Given CSVs of both solutions, read them in and compare results

# First analyze by timestamp - round timestamp to nearest second.
# May need additional logic to match up time stamps

import os
import csv


# Modified from http://stackoverflow.com/questions/32988295/efficiently-match-up-approximate-timestamps-in-python
def get_match(list_, el):
    # print(list_)
    import bisect
    i = bisect.bisect_left(list_, el)
    if i == len(list_):
        return i - 1
    elif list_[i] == el:
        return i
    elif i > 0:
        j = i - 1
        if list_[i] - el > el - list_[j]:
            return j
        else:
            return i
    return


def main():
    # These will be dictionaries of the following form:
    #       {timestamp: plate}
    byuCamResults = [{'timestamp': '1.234', 'plate': 'abc123'},
                     {'timestamp': '4.598', 'plate': '123abc'},
                     {'timestamp': '6.892', 'plate': '756PHP'}]
    newCamResults = [{'timestamp': '7.122', 'plate': '756PH'},
                     {'timestamp': '1.567', 'plate': 'abc123'},
                     {'timestamp': '4.238', 'plate': '123abc'}]

    # print(newCamResults)
    for i, each in enumerate(newCamResults):
        # print(i)
        j = get_match(list([float(d['timestamp']) for d in byuCamResults]), float(newCamResults[i]['timestamp']))
        # print("j: ", j)
        byuPlate = byuCamResults[j]['plate']
        newPlate = newCamResults[i]['plate']
        if byuPlate != newPlate:
            print('old: {}, new:{}'.format(byuPlate, newPlate))


if __name__ == '__main__':
    main()
