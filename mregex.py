import re

#DO NOT TOUCH anything until mentioned in comments......

#Replace 'line' by joining arguments(list) to String
#Following are some test cases:
#line = "Betty tell me About the Weather at Faridabad"
#line = "Betty What hello means"
#line = "Betty What is the meaning of hello"
#line = "Betty What is the Time"
#line = "Betty tell me about movie Om Shanti Om"

#Following Functions are to be used to call their respective Modules

def weather():
    print("weather is called")
    regex = r"weather (of|at|in) "
    if re.search(regex, line, re.M|re.I):
        match = re.search(regex, line, re.M|re.I )
        location = line[match.end():]
        print(location)
        #Call Weather API here usinng location


def mean():
    print("Word mean is called")
    regex = r"mean"
    if re.search(regex, line, re.M|re.I):
        match = re.search(regex, line, re.M|re.I )
        i = match.start()-2
        while(line[i]!=" "):
            i=i-1
        word = line[i+1:match.start()-1]
        print(word)
        #call Meaning API here using word


def meaning():
    print("Word meaning is called")
    regex = r"meaning (of|at|in) "
    if re.search(regex, line, re.M|re.I):
        match = re.search(regex, line, re.M|re.I )
        word = line[match.end():]
        print(word)
        #call Meaning API here using word

def time():
    print("Time is called")
    #call Time API here

def movie():
    print("Movie is called")
    regex = r" movie "
    if re.search(regex, line, re.M|re.I):
        match = re.search(regex, line, re.M|re.I )
        movie = line[match.end():]
        print(movie)
        #call Movie API hereusing movie
    

MODULES = {
    "weather": weather,
    "mean":mean,
    "means":mean,
    "meaning":meaning,
    "time":time,
    "movie":movie
     }


regex = r"(( weather )|( meaning )|( mean)|( means)|( time)|( movie ))"
if re.search(regex, line, re.M|re.I):
    match = re.search(regex, line, re.M|re.I )
    MODULES[match.group().strip().lower()]()
else:
    print("MODULE Not Found")
    









