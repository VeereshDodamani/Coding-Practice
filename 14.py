# Suppose there is an analog clock having second nahd only. User have 3 attempts to stop second hand.
# User will be awarded woth the points accordingly.
# - If second hand stops at [1,5,9,11] - 10 points
# - If second hand stops at [4,7,8,10] - 20 points
# - If second hand stops at [3,2,6,12] - 30 points

# Also consider there are three players, declare the winner of the game.

from time import sleep
def run():
    print("Press 'Enter' to continue and 'Ctrl+C' to stop' the second hand.")
    attempt = 1
    points = 0
    points_tabel = {}

    player = input("Enter the name of the player: ")
    while True:
        for digit in range(1,13):
            try:
                    print(digit)
                    sleep(0.2)
            except KeyboardInterrupt:
                print(f"Stopped at : {digit}")
                print("Points are added")
                sleep(2)
                if digit in [1,5,9,11]:
                    points += 10
                elif digit in [4,7,8,10]:
                    points += 20
                else:
                    points += 30
                attempt += 1

                if attempt == 4:
                    print(f"{player} has scored : {points} points")
                    points_tabel[player] = points
                    ans = input("Is there any other player y/n : ").lower()

                    if ans == "y":
                        player = input("Enter the name of player : ")
                        attempt = 1
                        points = 0
                    else:
                        print(f"Final result : {points_tabel}")
                        max_key = max(points_tabel,key = points_tabel.get)
                        print(f"Player with maximum points : {max_key}")
                        print(f"Maximum points : {points_tabel[max_key]}")
                        return

run()
