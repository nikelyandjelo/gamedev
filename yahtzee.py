from random import randint


def POSSIBLE_COMBOS() -> list:

    return ["One's", "Two's", "Three's", "Four's", "Five's", "Six's",
            "Three of a Kind", "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Chance", "Yahtzee"]


def FULL_HOUSE_VALUE() -> int:
    return 25


def SMALL_STRAIGHT_VALUE() -> int:
    return 30


def LARGE_STRAIGHT_VALUE() -> int:
    return 40


def NO_MATCH_VALUE() -> int:
    return 0


def yahtzee():
    user1 = init_scoresheet()
    user2 = init_scoresheet()

    while None in user1.values() or None in user2.values():
        if None in user1.values():
            print('\n----------------------------\n---USER 1, take your turn---\n----------------------------\n')
            user1 = take_a_turn(user1)
            print_scoresheet(user1)
            print("^^^^^ USER 2 had ended their turn with this score sheet ^^^^^")
        else:
            print('USER 1 has filled all field on their score sheet. They skip the turn')
        if None in user2.values():
            print('\n----------------------------\n---USER 2, take your turn---\n----------------------------\n')
            user2 = take_a_turn(user2)
            print_scoresheet(user2)
            print("^^^^^ USER 2 had ended their turn with this score sheet ^^^^^")
        else:
            print('USER 2 has filled all field on their score sheet. They skip the turn')

    user1 = submit_scoresheet(user1)
    user2 = submit_scoresheet(user2)
    process_winner(user1["Total"], user2["Total"])


def take_a_turn(scoresheet: dict) -> dict:

    hand = roll_dice([0, 0, 0, 0, 0])
    count = 1
    while count < 3:
        print_hand(hand)
        user_inp = input(f'You rolled {count} time(s). Enter your next action: Re-Roll(1),'
                         f' Submit(2) or My Score(3)>>> ').replace(" ", '')
        while (user_inp != 'Re-Roll' and user_inp != 'Submit' and user_inp != 'My Score'
               and user_inp != '1' and user_inp != '2' and user_inp != '3'):
            user_inp = input(f'Invalid entry. Please enter Re-Roll(1) to re-roll dice, Submit(2)'
                             f' to submit the score sheet or My Score(3) to see the current score sheet>>> ')
        if user_inp == 're-roll' or user_inp == '1':
            hand = roll_dice(hand)
            count += 1
        elif user_inp == 'my score' or user_inp == '3':
            print_scoresheet(scoresheet)
        elif user_inp == 'submit' or user_inp == '2':
            return update_scoresheet(scoresheet, hand)
    print("\n That was your last roll")
    print_scoresheet(scoresheet)
    return update_scoresheet(scoresheet, hand)


def submit_scoresheet(scoresheet: dict) -> dict:

    sum_of_nums = 0
    for combo in ["One's", "Two's", "Three's", "Four's", "Five's", "Six's"]:
        sum_of_nums += scoresheet[combo]
    if sum_of_nums >= 63:
        scoresheet["Bonus"] = 35
    else:
        scoresheet["Bonus"] = 0
    scoresheet['Total'] = sum(scoresheet.values())
    return scoresheet


def print_scoresheet(scoresheet: dict) -> None:
    print("-----------------\nOne's:\t{0}\nTwo's:\t{1}\nThree's:\t{2}\nFour's:\t{3}\nFive's:\t{4}\nSix's:\t{5}" \
          "\nThree of a Kind:\t{6}\nFour of a Kind:\t{7}\nFull House:\t{8}\nSmall Straight:\t{9}" \
          "\nLarge Straight:\t{10}\nChance:\t{11}\nYahtzee:\t{12}\n-----------------\n".format(
            scoresheet["One's"], scoresheet["Two's"], scoresheet["Three's"], scoresheet["Four's"],
            scoresheet["Five's"], scoresheet["Six's"], scoresheet["Three of a Kind"],
            scoresheet["Four of a Kind"], scoresheet["Full House"], scoresheet["Small Straight"],
            scoresheet["Large Straight"], scoresheet["Chance"], scoresheet["Yahtzee"]))


def init_scoresheet() -> dict:
    return {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
            "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
            "Large Straight": None, "Chance": None, "Yahtzee": None}


def process_winner(total1: int, total2: int) -> None:
    if total1 > total2:
        print(f'USER 1 won by {total1 - total2} points! Congratulations!')
    elif total1 < total2:
        print(f'USER 2 won by {total2 - total1} points! Congratulations!')
    else:
        print("Wow! After such long game both players scored the same amount of points! That's very rare!")


def roll_dice(hand: list) -> list:
    if 0 in hand:
        return [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
    else:
        user_inp = list(input('\nEnter the index of dice you would like to re-roll (1-6).'
                              ' The unselected dice will remain the same>>> ').replace(' ', ''))
        while not check_list(user_inp):
            user_inp = list(input('\nThe list of indices you entered is invalid. Valid dice numbers are 1-6'
                                  'Enter the index of dice you would'' like to re-roll.'
                                  ' The unselected dice will remain the same>>> ').replace(' ', ''))
        for index in user_inp:
            hand[int(index) - 1] = randint(1, 6)
        return hand


def print_hand(hand: list) -> None:
    if sorted(hand)[0] != sorted(hand)[4]:
        temp = '\t'
        for die in hand:
            temp += str(die) + '\t'
        print(f'\n---------------------------------------------------'
              f'\n---   Your current hand is:{temp}---\n---------------------------------------------------\n')
    else:
        temp = '\t'
        for die in hand:
            temp += str(die) + '\t'
        print(f'\n-----------------------------------------------------------------\n'
              f'---   Your current hand is:{temp}YAHTZEE! ◉_◉ ---'
              f'\n-----------------------------------------------------------------\n')


def check_list(list_of_indices: list) -> bool:
    if len(list_of_indices) > 5 or len(list_of_indices) < 1:
        return False
    for index in list_of_indices:
        if not index.isdigit():
            return False
        elif int(index) not in range(1, 6):
            return False
        elif list_of_indices.count(index) > 1:
            return False
    return True


def update_scoresheet(scoresheet: dict, hand: list) -> dict:
    print_hand(hand)

    user_choice = input(f'Please enter where you would like to deposit your hand of dice\n'
                        f'Available options: {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> ')
    while (user_choice not in POSSIBLE_COMBOS() or (user_choice == 'Yahtzee' and scoresheet['Yahtzee'] == 0) or
           scoresheet[user_choice] is not None):
        user_choice = input(f"\nThe choice is either invalid or you've already entered a number in that field.\n "
                            f"\nPlease enter where you would like to deposit your hand of dice"
                            f'\nAvailable options: {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> ')
    if user_choice in ["One's", "Two's", "Three's", "Four's", "Five's", "Six's"]:
        scoresheet[user_choice] = update_scoresheet_nums(user_choice, hand)
    elif user_choice == 'Yahtzee':
        if len(set(hand)) == 1:
            scoresheet[user_choice] = update_scoresheet_combo_yahtzee(scoresheet)
        else:
            scoresheet['Yahtzee'] = 0
    else:
        scoresheet[user_choice] = update_scoresheet_combo(user_choice, hand)
    return scoresheet


def update_scoresheet_nums(choice: str, hand: list) -> int:
    options = ["One's", "Two's", "Three's", "Four's", "Five's", "Six's"]
    return (options.index(choice) + 1) * hand.count(options.index(choice) + 1)


def update_scoresheet_combo(choice: str, hand: list) -> int:
    if choice == 'Three of a Kind' or choice == 'Four of a Kind' or choice == 'Chance':
        return sum(hand)
    elif choice == 'Full House':
        if len(set(hand)) == 2:
            return FULL_HOUSE_VALUE()
    elif choice == 'Small Straight':
        temp_str = ''
        for die in sorted(hand):
            temp_str += str(die)
        if ('2345' in temp_str) or ('1234' in temp_str) or ('3456' in temp_str):
            return SMALL_STRAIGHT_VALUE()
    elif choice == 'Large Straight':
        if sorted(hand) == [1, 2, 3, 4, 5] or sorted(hand) == [2, 3, 4, 5, 6]:
            return LARGE_STRAIGHT_VALUE()
    return NO_MATCH_VALUE()


def update_scoresheet_combo_yahtzee(scoresheet: dict) -> int:
    if scoresheet["Yahtzee"] is None:
        return 50
    return scoresheet['Yahtzee'] + 50


def main():
    yahtzee()


if __name__ == '__main__':
    main()
