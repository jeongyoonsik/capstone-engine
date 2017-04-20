import editdistance
from time import sleep
from plate_tree import PlateTree


# def merge_results(*args):
def merge_results(plate1, plate2):
    distance = editdistance.eval(plate1, plate2)
    if distance < 2:
        return "Cannot be merged to form new result"
    plate_array = []
    while len(plate1) != len(plate2):
        if len(plate1) > len(plate2):
            temp_array = list(plate2)
            for i in range(0, len(plate2) + 1):
                temp_array2 = list(temp_array)
                temp_array2.insert(i, '_')
                tempstring = ''.join(temp_array2)
                print(tempstring)
                if editdistance.eval(plate1, plate2) == editdistance.eval(plate1, tempstring):
                    print(tempstring)
                    plate2 = tempstring
                    continue
        if len(plate2) > len(plate1):
            temp_array = list(plate2)
            for i in range(0, len(plate2) + 1):
                temp_array2 = list(temp_array)
                temp_array2.insert(i, '_')
                tempstring = ''.join(temp_array2)
                print(tempstring)
                if editdistance.eval(plate1, plate2) == editdistance.eval(plate1, tempstring):
                    print(tempstring)
                    plate2 = tempstring
                    continue
    for i, each in enumerate(plate1):
        value = []
        if each == plate2[i]:
            value.append(each)
        else:
            value.append(each)
            value.append(plate2[i])
        plate_array.append(value)
    print(plate_array)
    possible_plates = []

    plateTree = PlateTree('', plate_array)
    plateTree.create_tree()
    plateTree.get_plates()
    results = plateTree.final_array
    # print(results)
    for result in results:
        newplate = ''
        # print(result)
        for value in result:
            newplate += value[0]
        if newplate != plate1 and newplate != plate2:
            possible_plates.append(newplate)
    print(possible_plates)
