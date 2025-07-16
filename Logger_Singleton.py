class Logger_Singleton:
    
    #Global instance variable to make sure only one logger object exists
    instance = None
    filename = ""
    
    def __init__(self, name):
        #Exception is called if a second logger is attempted to be created
        if (Logger_Singleton.instance != None):
            raise Exception("Logger already exist")
        else:
            Logger_Singleton.instance = self
            Logger_Singleton.filename = name
            #The log file is created if it doesn't exist but isn't overwritten here.
            temp = open(Logger_Singleton.filename, 'a')
            temp.close()
                 
    #The highscore is updated        
    def update_score(self, score):
        update = open(Logger_Singleton.filename, 'w')
        update.write(str(score))
        update.close()
        
    #The highscore is read
    def read_score(self):
        read = open(Logger_Singleton.filename, 'r')
        read.seek(0)
        #If the score is empty a 0 is placed for the highscore
        #This prevents errors when casting to int
        if (read.readline() == ''):
            read.seek(0)
            read.close()
            read = open(Logger_Singleton.filename, 'w')
            read.write('0')
            read.close()
            read = open(Logger_Singleton.filename, 'r')
        read.seek(0)
        temp = read.readline()
        read.close()
        return int(temp)
    
    #The highscore is reset
    def reset_score(self):
        update = open(Logger_Singleton.filename, 'w')
        update.write('0')
        update.close()
        