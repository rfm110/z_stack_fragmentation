def extractZSlice(array1, array2):
    #  if the following is not appropriate, move the two to parameters provided to the function
    channelToExtract = raw_input('Please enter 1 or 2 for the channel you want to extract ')
    levelToExtract = raw_input('Please enter the z stack level to be extracted ')
    if channelToExtract == 1:
        return array1[levelToExtract-1]
    if channelToExtract == 2:
        return array2[levelToExtract-1]