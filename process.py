# opens a file in the directory and stores data in a variable
log_file = open("um-server-01.txt")


def sales_reports(log_file): #function declaration
    for line in log_file: # for-loop going over each line in the filew
        line = line.rstrip() # removing whitespaceon each line
        day = line[0:3] # sets the first 3 chars of the line = to a new variable
        if day == "Mon": # checking the variable against a specific day
            print(line) #pints the line to the terminal if it = true


# sales_reports(log_file) # Calls the functoion -- needed to comment out for extra credit function

def melons(log_file):
    for line in log_file:
        if float(line.split(' ')[2])>10:
            print(line)

melons(log_file)