def find_missing(array1, array2):
    if type(array1) == list and type(array2) == list:
        if len(array1) == len(array2):  # check which list has the extra number
            return 0
        if len(array1) > len(array2):
            for item in array1:  ## if list a has the extra number
                if item in array2:
                    continue
                else:
                    return item
        else:  ## if list b has the extra number
            for item in array2:
                if item in array1:
                    continue
                return item
    return 'Only lists allowed'
def main():
    a = [1, 2, 3]
    b = [1, 2, 3, 4]
    print(find_missing(a, b))
if __name__ == '__main__':main()