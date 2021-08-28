import random
import time

score = 0

oscore = 0

def read_int(prompt):
    while True:
        try:
            global integer
            integer = int(input(prompt))

            if 20 >= integer >= 1:
                break
            else:
                print('Too large or too small, try again.\n')
        except:
            print('Not an integer, try again.\n')

x = 1

while True:
    try:
        difficulty = int(input('Select your difficulty from 1 to 10.\n'))

        if 10 >= difficulty >= 1:
            break
        else:
            continue
    except:
        print('Error, try again.')

while x <= 10:
    print(f'Round {x}!\n')

    time.sleep(1)

    while True:
        try:
            req1 = random.randint(difficulty, difficulty + 10)
            req2 = random.randint(difficulty, difficulty + 10)

            ans = req1 * req2

            answer = int(input(f'What is {req1} times {req2}?\n'))

            if answer == ans:
                print('That is correct.\n')
            else:
                print('Sorry, try again.\n')
                continue
            break
        except:
            print('Error, try again.\n')

    read_int('Select a number 1 through 20.\n')

    double = False
    triple = False

    throw_result = random.randint(1, 20)

    random_range = random.randint(5, 12)

    random_deviation = random.randint(0, 3)

    range_start = integer - random_range + random_deviation
    range_end = integer + random_range

    req1 = random.randint(difficulty, difficulty + 10)
    req2 = random.randint(difficulty, difficulty + 10)

    if range_end >= throw_result >= range_start:
        multiplier = random.randint(0, 30)

        if multiplier > 25:
            triple = True
            throw_result *= 3
        elif multiplier > 15:
            double = True
            throw_result *= 2

        if triple == True:
            print(f'Wow! You tripled and gained {throw_result}!\n')
            time.sleep(1)
        elif double == True:
            print(f'Nice! You doubled and gained {throw_result}!\n')
            time.sleep(1)
        else:
            print(f'Hit! You gained {throw_result} points!\n')
            time.sleep(1)

        score += throw_result
    else:
        print('Aw, you missed!\n')

    time.sleep(1)
    
    odouble = False
    otriple = False

    ointeger = random.randint(8, 12)

    othrow_result = random.randint(difficulty + 0, difficulty + 10)

    orandom_range = random.randint(difficulty - 1, 10)

    orandom_deviation = 0

    orange_start = ointeger - orandom_range + orandom_deviation
    orange_end = ointeger + orandom_range

    if orange_end >= othrow_result >= orange_start:
        omultiplier = random.randint(0, 30)

        if omultiplier > 25:
            otriple = True
            othrow_result *= 3
        elif omultiplier > 15:
            odouble = True
            othrow_result *= 2

        if otriple == True:
            print(f'No! Your friend tripled and gained {othrow_result}!\n')
            time.sleep(1)
        elif odouble == True:
            print(f'Shoot! Your friend doubled and gained {othrow_result}!\n')
            time.sleep(1)
        else:
            print(f'Argh! Your friend gained {othrow_result} points!\n')
            time.sleep(1)

        oscore += othrow_result
    else:
        print('Yay, your friend missed!\n')
        time.sleep(1)

    x += 1

print(f'You scored a total of {score} points! Nice work!')

print(f'Your friend scored a total of {oscore} points...')

if oscore > score:
    print('Well, your friend won. Good game!')
elif oscore == score:
    print('Whoa, you tied! Nice game!')
else:
    print('You won! Nice victory!')
