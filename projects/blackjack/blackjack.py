from art import logo
import random





def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return("It is a draw!")
    elif dealer_score == 0:
        return("Dealer BlackJack you lose!")
    elif player_score == 0:
        return("BlackJack you win!")
    elif player_score > 21:
        return("You went over! You lose!")
    elif dealer_score > 21:
        return("Dealer went over, YOU WIN!")
    elif player_score > dealer_score:
        return("You win!")
    else:
        return("You lose!")





def draw_card():
    deck = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(deck)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        player_score = 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)



def blackjack():
    print(50 * "\n")
    print(logo)

    player_hand = []
    player_score = -1

    dealer_hand = []
    dealer_score = -1

    gameover = False

    for x in range(2):

        player_hand.append(draw_card())
        dealer_hand.append(draw_card())
    

    while not gameover:

        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your hand {player_hand} and score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            gameover = True

        else:
            should_user_draw = input(f"Do you want another card 'y' or 'n'")
            if should_user_draw == "y":
                player_hand.append(draw_card())
            
            else:
                gameover = True

    while dealer_hand != 0 and dealer_score < 17:
        dealer_hand.append(draw_card())
        dealer_score = sum(dealer_hand)

    print(f"Your final hand is {player_hand} and your score: {player_score}")
    print(f"Dealer's final hand is {dealer_hand} and dealer score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of BlackJack? type 'y' or 'n': ") == "y":
    blackjack()

asd



