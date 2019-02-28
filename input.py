def load(datasetSrc = "a_example.txt" ):
    f = open(datasetSrc, "r")
    first = True
    array = []
    for x in f:
        if(first):
            N = int(x.strip())
            first = False
        else :
            aux = x.strip().split(" ")
            dic = {}
            dic['isVertical'] = (aux[0] == 'V');
            dic['qtt'] = aux[1];
            dic['tags'] = aux[2:];
            print(dic)
            array.append(dic)
    return array