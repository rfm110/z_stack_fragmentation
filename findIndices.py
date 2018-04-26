def findIndices(array1):
    # TODO: something to consider, are the z values always even, i mean i would think so but confirm this
    channel = raw_input('Please enter 1 or 2 for channel ')
    availableIndices = []
    totalZSlices = array1.shape[0]
    if channel == 1:
        availableIndices.append(0)
        for i in (2, totalZSlices, 2):
            availableIndices.append(i)
    else:
        for i in (1, totalZSlices, 2):
            availableIndices.append(i)
    print availableIndices
    return availableIndices