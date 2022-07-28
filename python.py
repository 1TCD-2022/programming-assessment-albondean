print('Enter "true" (t) or "false" (f) for the following question, Enjoy!')
valid_answer = False
while not valid_answer:
        answer = input('Is North America a Continent ?')
        valid_answer = True
        if answer != 'true' and answer != 'false':
            print('try again')
            valid_answer = False

        if valid_answer:
            if answer == 'true':
                print('correct, North America is a continent but the USA is a country')
            elif answer == 'false' :
                print('incorrect ')
valid_answer = False
while not valid_answer:
        answer = input('Do Genetic Females have XY chromosomes ?')
        valid_answer = True
        if answer != 'true' and answer != 'false':
            print('try again')
            valid_answer = False

        if valid_answer:
            if answer == 'false':
                print('correct, Gentic Females actually have XX chromosomes')
            elif answer == 'true' :
                print('incorrect ')
valid_answer = False
while not valid_answer:
        answer = input('Do cheetahs bark ?')
        valid_answer = True
        if answer != 'true' and answer != 'false':
            print('try again')
            valid_answer = False

        if valid_answer:
            if answer == 'true':
                print('correct, Yes! Cheetahs are more related to dogs than cats due to the non-retractable claws and the barking gene')
            elif answer == 'false' :
                print('incorrect ')
valid_answer = False
while not valid_answer:
        answer = input('Was Hitler 5`6 ?')
        valid_answer = True
        if answer != 'true' and answer != 'false':
            print('try again')
            valid_answer = False

        if valid_answer:
            if answer == 'false':
                print('correct, He was actually 5`8 ')
            elif answer == 'true' :
                print('incorrect ')

