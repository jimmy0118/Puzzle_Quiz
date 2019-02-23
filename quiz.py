#content of quiz
quiz_easy = """
            The FIFA World Cup, often simply called the World Cup, is an
            international association __1__ competition contested by the senior
            men's national teams of the members of FIFA, the sport's global
            governing body. The championship has been awarded every __2__ years
            since the inaugural tournament in 1930, except in 1942 and 1946 when
            it was not held because of the Second World War. __3__ won its
            fourth title at the 2014 tournament in __4__.
            """

quiz_medium = """
              Mickey Mouse is a funny animal cartoon character and the mascot
              of __1__ Company. He was created by Walt Disney and Ub Iwerks at
              the Walt Disney Studios in 1928. An anthropomorphic mouse who
              typically wears red shorts, large yellow shoes, and white __2__,
              Mickey is one of the world's most recognizable characters.Mickey
              generally appears alongside his girlfriend __3__, his pet dog
              __4__, his friends Donald Duck and Goofy, and his nemesis Pete,
              among others.
              """
quiz_hard = """
            A __1__ is a device that can be instructed to carry out arbitrary
            sequences of arithmetic or logical operations automatically. The
            ability of computers to follow generalized sets of operations,
            called __2__, enables them to perform an extremely wide range of
            tasks. Conventionally, a modern __1__ consists of at least one
            processing element, typically a __3__ (CPU), and some form of
            memory. The processing element carries out arithmetic and logical
            operations, and a sequencing and control unit can change the order
            of operations in response to stored information. __4__ devices
            include input devices (keyboards, mice, joystick, etc.), output
            devices (monitor screens, printers, etc.), and input/output devices
            that perform both functions. __4__ devices allow information to be
            retrieved from an external source and they enable the result of
            operations to be saved and retrieved.
            """

#list of answer
answer_easy = ["football","four","Germany","Brazil"]

answer_medium = ["The Walt Disney","gloves","Minnie Mouse","Pluto"]

answer_hard = ["computer","programs","central processing unit","Peripheral"]

#content of blank
blank = ["__1__","__2__","__3__","__4__"]

#define the content of quiz and answer based on the difficulty user selected
game_data = {
   "easy": {
        "quiz": "The FIFA World Cup, often simply called the World Cup, is an"
        "international association __1__ competition contested by the senior"
        "men's national teams of the members of FIFA, the sport's global"
        "governing body. The championship has been awarded every __2__ years"
        "since the inaugural tournament in 1930, except in 1942 and 1946 when"
        "it was not held because of the Second World War. __3__ won its fourth"
        "title at the 2014 tournament in __4__.",
        "answers": ["football","four","Germany","Brazil"]
    },
   "medium": {
        "quiz": "Mickey Mouse is a funny animal cartoon character and the"
        "mascot of __1__ Company. He was created by Walt Disney and Ub Iwerks"
        "at the Walt Disney Studios in 1928. An anthropomorphic mouse who"
        "typically wears red shorts, large yellow shoes, and white __2__,"
        "Mickey is one of the world's most recognizable characters.Mickey"
        "generally appears alongside his girlfriend __3__, his pet dog __4__,"
        "his friends Donald Duck and Goofy, and his nemesis Pete,"
        "among others.",
        "answers": ["The Walt Disney","gloves","Minnie Mouse","Pluto"]
    },
   "hard": {
        "quiz": "A __1__ is a device that can be instructed to carry out"
        "arbitrary sequences of arithmetic or logical operations automatically."
        "The ability of computers to follow generalized sets of operations,"
        "called __2__, enables them to perform an extremely wide range of"
        "tasks. Conventionally, a modern __1__ consists of at least one"
        "processing element, typically a __3__ (CPU), and some form of memory."
        "The processing element carries out arithmetic and logical operations,"
        "and a sequencing and control unit can change the order of operations"
        "in response to stored information. __4__ devices include input devices"
        "(keyboards, mice, joystick, etc.), output devices (monitor screens,"
        "printers, etc.), and input/output devices that perform both functions."
        "__4__ devices allow information to be retrieved from an external"
        "source and they enable the result of operations to be saved and"
        "retrieved.",
        "answers": ["computer","programs","central processing unit",
        "Peripheral"]
    }
}

#main function
def main():
    """The main function

        Input:
            difficulty (str): difficulty selected by user.
        Behavior:
            It checks the user input.
            If user input matches the difficulty from easy | medium | hard,
            run function fill(paragraph, difficulty).
            If user input is incorrect
            ask user to select difficulty from easy | medium | hard again.

    """
    while True:
        #prompt user to choose difficulty
        difficulty = raw_input("Please select a game difficulty!""\n"
                           "Difficulty choices: easy | medium | hard""\n"
                           "Please type your game difficulty:")
        #start the quiz and show user the content of quiz
        if difficulty =="easy" or difficulty =="medium" or difficulty =="hard":
            print "\n""You have selected difficulty "+ difficulty +"\n"
            paragraph = game_data[difficulty]["quiz"]
            fill(paragraph, difficulty)
            #for user complete the quiz
            print "You just finished the quiz. Thanks for playing!!!"
            break
        else:
            print "\n""Wrong difficulty! Please try again!"
    return difficulty

def fill(paragraph, difficulty):
    """Prompt user to fill answer in the blank.

        Input:
            answer (str): answer typed by user.
        Behavior:
            If user type the correct answer,
            run function replace(paragraph,count, difficulty) and print the quiz
            with right answer.
            After that, ask user to fill answer in the next blank.
            if user type the incorrect answer,
            ask user to try again.
            This process happens until all blanks are found.

    """
    answer_list = game_data[difficulty]["answers"]
    index = 0
    count = 0
    question_count = 1
    print paragraph
    while index < len(blank):
        answer_fill = raw_input(
        "\n""Q"+str(question_count)+". What should go in" +blank[count]+"?:")
        if answer_fill == answer_list[count]:
            print "\n""Correct!""\n"
            print replace(paragraph, count, difficulty)
            paragraph = replace(paragraph, count, difficulty)
            index += 1
            count += 1
            question_count += 1
        else:
            print "\n""Incorrect! Try again""\n"
            print paragraph
    return answer_fill

#replace blank content in the quiz with the correct answer
def replace(paragraph,count, difficulty):
    """replace the blank with the right answer

        Input:
            paragraph: content of quiz based on the difficulty user selected.
        Behavior:
            Replace the blank with right answer in the paragraph.

    """
    answer_list = game_data[difficulty]["answers"]
    quiz_list = paragraph.split()
    replaced = []
    for word in quiz_list:
        word = word.replace(blank[count],answer_list[count])
        replaced.append(word)
    paragraph = " ".join(replaced)
    return paragraph

#run the main()
main()
