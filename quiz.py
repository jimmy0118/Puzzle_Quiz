#content of quiz
quiz_easy = "The FIFA World Cup, often simply called the World Cup, is an international association __1__ competition contested by the senior men's national teams of the members of FIFA, the sport's global governing body. The championship has been awarded every __2__ years since the inaugural tournament in 1930, except in 1942 and 1946 when it was not held because of the Second World War. __3__ won its fourth title at the 2014 tournament in __4__."

quiz_medium = "Mickey Mouse is a funny animal cartoon character and the mascot of __1__ Company. He was created by Walt Disney and Ub Iwerks at the Walt Disney Studios in 1928. An anthropomorphic mouse who typically wears red shorts, large yellow shoes, and white __2__, Mickey is one of the world's most recognizable characters.Mickey generally appears alongside his girlfriend __3__, his pet dog __4__, his friends Donald Duck and Goofy, and his nemesis Pete, among others."

quiz_hard = "A __1__ is a device that can be instructed to carry out arbitrary sequences of arithmetic or logical operations automatically. The ability of computers to follow generalized sets of operations, called __2__, enables them to perform an extremely wide range of tasks. Conventionally, a modern __1__ consists of at least one processing element, typically a __3__ (CPU), and some form of memory. The processing element carries out arithmetic and logical operations, and a sequencing and control unit can change the order of operations in response to stored information. __4__ devices include input devices (keyboards, mice, joystick, etc.), output devices (monitor screens, printers, etc.), and input/output devices that perform both functions. __4__ devices allow information to be retrieved from an external source and they enable the result of operations to be saved and retrieved."

#list of answer
answer_easy = ["football","four","Germany","Brazil"]

answer_medium = ["The Walt Disney","gloves","Minnie Mouse","Pluto"]

answer_hard = ["computer","programs","central processing unit","Peripheral"]

#content of blank
blank = ["__1__","__2__","__3__","__4__"]

#define the content of quiz and content of answers based on the difficulty user selected
game_data = {
   "easy": {
        "quiz": "The FIFA World Cup, often simply called the World Cup, is an international association __1__ competition contested by the senior men's national teams of the members of FIFA, the sport's global governing body. The championship has been awarded every __2__ years since the inaugural tournament in 1930, except in 1942 and 1946 when it was not held because of the Second World War. __3__ won its fourth title at the 2014 tournament in __4__.",
        "answers": ["The Walt Disney","gloves","Minnie Mouse","Pluto"]
    },
   "medium": {
        "quiz": "Mickey Mouse is a funny animal cartoon character and the mascot of __1__ Company. He was created by Walt Disney and Ub Iwerks at the Walt Disney Studios in 1928. An anthropomorphic mouse who typically wears red shorts, large yellow shoes, and white __2__, Mickey is one of the world's most recognizable characters.Mickey generally appears alongside his girlfriend __3__, his pet dog __4__, his friends Donald Duck and Goofy, and his nemesis Pete, among others.",
        "answers": ["football","four","Germany","Brazil"]
    },
   "hard": {
        "quiz": "A __1__ is a device that can be instructed to carry out arbitrary sequences of arithmetic or logical operations automatically. The ability of computers to follow generalized sets of operations, called __2__, enables them to perform an extremely wide range of tasks. Conventionally, a modern __1__ consists of at least one processing element, typically a __3__ (CPU), and some form of memory. The processing element carries out arithmetic and logical operations, and a sequencing and control unit can change the order of operations in response to stored information. __4__ devices include input devices (keyboards, mice, joystick, etc.), output devices (monitor screens, printers, etc.), and input/output devices that perform both functions. __4__ devices allow information to be retrieved from an external source and they enable the result of operations to be saved and retrieved.",
        "answers": ["computer","programs","central processing unit","Peripheral"]
    }
}
