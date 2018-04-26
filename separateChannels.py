def separateChannels(imageArray, arrayShape):
    """Separate z-stacks based on channel (2 total)
       Return the two arrays corresponding to each channel
    """
    # initialize new arrays for the separate channels
    arrayChannel1 = None
    arrayChannel2 = None
    print imageArray.shape

    splitArray = np.split(imageArray, 130, axis=0)

    counter = 0
    # print 'splitArray is', splitArray
    for i in splitArray:
        counter += 1
        if (counter % 2 == 0):
            if (counter == 2):
                arrayChannel2 = i
            else:
                arrayChannel2 = np.concatenate((arrayChannel2, i), axis = 0)
        else:
            if (counter == 1):
                arrayChannel1 = i
            else:
                arrayChannel1 = np.concatenate((arrayChannel1, i), axis = 0)

    # TODO: remove me once tested
    print
    print 'channel 1 array'
    print arrayChannel1.shape
    print "~~~~~~~~~~~~~~~~~~~~~~~~"
    print 'channel 2 array'
    print arrayChannel2.shape
    return arrayChannel1, arrayChannel2