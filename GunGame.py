from random import randint

score = 0
rounds = 1

while True:
    bullet_x = randint(1, 10)
    player_x = int(input('Pick a number from 1 to 10: '))

    if player_x < 1 or player_x > 10:
        print("Try again. I said 1-10. LISTEN!")
        continue

    if player_x == bullet_x:
        print("You died! Congratulations ;D")
        print("Final Score:", score)
        break
    else:
        print("You lived...for now.")
        input("Press Enter to load the gun.")

    score += 1

    if score >= rounds * 5:
        rounds += 1
        print("Round", rounds)
        print("The bullets are getting faster!")
        while True:
            bullet_x = randint(1, 5)
            player_x = int(input('Pick a number from 1 to 5: '))

            if player_x < 1 or player_x > 5:
                print("Try again. I said 1-5. LISTEN!")
                continue

            if player_x == bullet_x:
                print("You died! Congratulations ;D")
                print("Final Score:", score)
                break
            else:
                print("You lived...for now.")
                input("Press Enter to load the gun.")

            score += 2

        print("Game Over!")
