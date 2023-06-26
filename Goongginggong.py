while True: 
    candy = input('You like candy?')

    if candy.lower() in ['yes', 'ye']:
        print('Me too! I got a bag in my van full of candy!')
        while True:
            age= int(input('How old is ya?')) 
            if age >= 13:
                quit()
            if age <= 12:
                print('if the age is on the clock, they ready for the cock!')
                quit()
    elif candy.lower() in ['no', 'n']:
        print('get the fuck outta here!')
        quit()
    else:
        print('Invalid input. Please respond with "yes" or "no".')
        