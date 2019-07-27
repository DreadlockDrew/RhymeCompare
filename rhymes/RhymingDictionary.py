def findRhymes (fileName, userInput):
    output=[]
    with open(fileName) as f:
        f=f.read().splitlines()

        for line in f:
            if userInput==line.split()[0]:
                userInputRhyme=returnRhyme(line)
        for line in f:

           if userInputRhyme == returnRhyme(line):
               output.append(line.split()[0])
    return output
def returnRhyme(verboseWordGroup): #this code block makes sure rhyme is stripped of its precision EX.) input(['AH0', 'L', 'D']) returns ['AH', 'L', 'D']
    line = verboseWordGroup.split()
    Rhyme=[]
    for aspect in line:

        if(aspect.isalpha() == False):  # checks if the aspect has a number
            Rhyme = []                  # Clears the output if it does have a number and starts a new output
        Rhyme.append(aspect)            # adds the aspect to the output.
        characterFamily = "" 
        for character in Rhyme[0]:
            if(character.isalpha() == True):
                characterFamily+=character 
        Rhyme[0]= characterFamily
    return Rhyme

def returnRAWRhyme(verboseWordGroup):

    if len(verboseWordGroup)!=0:
        verboseWordGroup.pop(0)
    return verboseWordGroup

def getSounds(fileName, userInput):
    with open(fileName) as f:
        f=f.read().splitlines()
        for line in f:
            if userInput.upper()==line.split()[0]:
                userInputRhyme=returnRAWRhyme(line.split())
                return userInputRhyme

    return []


# getSounds('data/cmudict-0.7b' , 'FISH'))
# Yields Linguistic Components of the word "fish"


print(findRhymes('data/cmudict-0.7b' ,"CODE"))




