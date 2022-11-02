import random
import os
import time

class Blackjack():

    def __init__(self, player_hand, dealer_hand):
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand

    def prepare_deck():
        deck = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH',
                'AD','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD',
                'AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS',
                'AC','2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC']
        random.shuffle(deck)
        shuffled_deck = deck
        return shuffled_deck        
    
    def deal_card(player, deck):
        player.append(deck.pop())
        return player

    def show_hands(player, dealer):
        card_num = 0
        player_hand_string = ", ".join(player)
        dealer_hand_string = ""
        for card in dealer:
            if card_num == 0:
                dealer_hand_string += card
                card_num += 1
            else:
                dealer_hand_string += ", ??"
        return f"Your hand: {player_hand_string}\nDealer's hand: {dealer_hand_string}"

    def score_hand(hand):
        hand_value = 0
        for card in hand:
            if card[0] == 'A':
                hand_value += 1
            elif card[0] == '2':
                hand_value += 2
            elif card[0] == '3':
                hand_value += 3
            elif card[0] == '4':
                hand_value += 4
            elif card[0] == '5':
                hand_value += 5
            elif card[0] == '6':
                hand_value += 6
            elif card[0] == '7':
                hand_value += 7
            elif card[0] == '8':
                hand_value += 8
            elif card[0] == '9':
                hand_value += 9
            elif card[0] == 'T':
                hand_value += 10
            elif card[0] == 'J':
                hand_value += 10
            elif card[0] == 'Q':
                hand_value += 10
            elif card[0] == 'K':
                hand_value += 10
        return hand_value 

    def ace_check(hand):
        for card in hand:
            if card[0] == 'A':
                while True:
                    answer = input("Would you like to change your Ace value from 1 to 11?\n'Y' or 'N': ")
                    if answer.lower().strip() == 'y':
                        return 10
                    elif answer.lower().strip() == 'n':
                        return 0
                    else:
                        os.system("cls")
                        print("Invalid input, please try again")
        return 0

    def main():
        os.system("cls")
        print("-----Welcome to Blackjack!-----")
        while True:
            os.system("cls")
            answer = input("Would you like to Play or Quit?\n'P' or 'Q': ")
            if answer.lower().strip() == 'q':
                os.system("cls")
                print("Goodbye")
                break
            elif answer.lower().strip() == 'p':
                while True:
                    os.system("cls")
                    current_deck = Blackjack.prepare_deck() 
                    player_hand = []
                    dealer_hand = []
                    Blackjack.deal_card(dealer_hand, current_deck)
                    Blackjack.deal_card(player_hand, current_deck)
                    Blackjack.deal_card(dealer_hand, current_deck)
                    Blackjack.deal_card(player_hand, current_deck)
                    player_score = Blackjack.score_hand(player_hand)
                    dealer_score = Blackjack.score_hand(dealer_hand)
                    print(Blackjack.show_hands(player_hand, dealer_hand))
                    print(f'Your hand score is {player_score}!')
                    while True:
                        answer = input("Would you like to Hit, Stand, or Quit?\n'H', 'S' or 'Q': ")
                        if answer.lower().strip() == 'h':
                            os.system("cls")
                            Blackjack.deal_card(player_hand, current_deck)
                            player_score = Blackjack.score_hand(player_hand)
                            print(Blackjack.show_hands(player_hand, dealer_hand))
                            print(f'Your hand score is {player_score}!')
                            if player_score > 21:
                                time.sleep(2)
                                os.system("cls")
                                print("Bust!")
                                time.sleep(2)
                                break
                        elif answer.lower().strip() == 's':
                            os.system("cls")
                            print(Blackjack.show_hands(player_hand, dealer_hand))
                            print(f'Your hand score is {player_score}!')
                            player_score += Blackjack.ace_check(player_hand)
                            os.system("cls")
                            print(Blackjack.show_hands(player_hand, dealer_hand))
                            print(f'Your hand score is {player_score}!')
                            if player_score > 21:
                                time.sleep(2)
                                os.system("cls")
                                print("Bust!")
                                time.sleep(2)
                                break
                            while dealer_score < 17:
                                Blackjack.deal_card(dealer_hand, current_deck)
                                dealer_score = Blackjack.score_hand(dealer_hand)
                                os.system("cls")
                                print(Blackjack.show_hands(player_hand, dealer_hand))
                                print(f'Your hand score is {player_score}!')
                                time.sleep(2)
                            if player_score == dealer_score:
                                os.system("cls")
                                print("Tie, Dealer Wins!")
                                time.sleep(2)
                                break
                            elif dealer_score > 21:
                                os.system("cls")
                                print("Dealer Bust, Player Wins!")
                                time.sleep(2)
                                break
                            elif player_score > dealer_score:
                                os.system("cls")
                                print("Player Wins!")
                                time.sleep(2)
                                break
                            elif player_score < dealer_score:
                                os.system("cls")
                                print("Dealer Wins!")
                                time.sleep(2)
                                break
                        elif answer.lower().strip() == 'q':
                            break
                        else:
                            os.system("cls")
                            print("Invalid input, please try again")
                    break
                    
            else:
                os.system("cls")
                print("Invalid input, please try again")


Blackjack.main()