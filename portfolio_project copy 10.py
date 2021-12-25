import random  # Portfolio Project, Balckjack 21, Kevin Vilay 10/12/2021


class dealer:

    def __init__(self):

        self.card_stack = []

        self.dealer_card1 = random.randint(1, 13)

        self.card_stack.append(self.dealer_card1)

        print("\n>>>>>>>>>>>       Dealer's card 1<> ",
              self.dealer_card1, "       <<<<<<<<<\n")

        self.dealer_score = self.dealer_card1

        self.dealer_card2 = ""

    def dealer_moves(self):

        card_count = 2

        while self.dealer_score < 22:

            add_card = input(">>> DEALER currently has a total of " +
                             str(self.dealer_score) + "     h - Hit or s - Stay?  ")

            if add_card == 'h':

                another_card = random.randint(1, 13)

                self.card_stack.append(another_card)

                self.dealer_score += another_card

                print("<>  Card ", card_count, " is: ", another_card,  "  Dealer cards stack = ",
                      self.card_stack,  "\n\n                  Dealer hand total: ", self.dealer_score, "\n")

                card_count += 1

            if self.dealer_score > 21:
                print("                Dealer is Busted ! ...", self.dealer_score)
                break

            if add_card == 's':

                break

        print(">>>               Dealer's Total = ", self.dealer_score)
        print("")


class player:

    def __init__(self):

        self.card_stack = []

        self.player_turn = random.randint(1, 13)

        self.player_card1 = self.player_turn

        self.card_stack.append(self.player_card1)

        print("<>                Player's card 1<> ", self.player_card1)

        self.player_card2 = random.randint(1, 13)

        self.card_stack.append(self.player_card2)

        print("<>                Player's card 2<> ", self.player_card2, "\n")

        self.player_score = self.player_card1 + self.player_card2
        print("<>                Player's total = ",
              self.player_score, "\n")

    def player_moves(self):

        add_card = ''

        card_count = 2

        while self.player_score < 22:

            add_card = input("<>      PLAYER currently has: " +
                             str(self.player_score) + "      h - Hit or     s - Stay?  ")

            if add_card == 'h':

                another_card = random.randint(1, 13)

                self.card_stack.append(another_card)

                self.player_score += another_card

                print("<> Your card ", card_count, " is: ", another_card, " PLAYER Cards Stack : ",
                      self.card_stack,   "\n\n                  PLAYER hand total: ", self.player_score, "\n")

                card_count += 1

            if add_card == 's':    # This will trigger DEALER to make the next move by returning True

                return True


class game:

    def __init__(self):

        self.dealer_turn = False

    def the_game(self, this_player, this_dealer):

        # Trigger player class.player_move , player also makes the move, return True if player is 's' for "stay"

        self.dealer_turn = this_player.player_moves()

        if self.dealer_turn:     # if player chose to stay 's', this will let the DEALER to make more moves

            print("\n>>>                 Dealer's NEXT move                <<< ")

            this_dealer.dealer_moves()

        if this_dealer.dealer_score < 22:

            if this_player.player_score < 22:

                if this_player.player_score == this_dealer.dealer_score:

                    print(" <><><><>   Tie Game !    <><><><> ", this_player.player_score, "  ==  ",
                          this_dealer.dealer_score, "\n")

                if this_player.player_score > this_dealer.dealer_score:

                    print(" *** You won ! ...your score =", this_player.player_score,
                          " Dealer = ", this_dealer.dealer_score, "\n")

                if this_player.player_score < this_dealer.dealer_score:

                    print("            You lost! ... your score = ", this_player.player_score,
                          " Dealer = ", this_dealer.dealer_score, "\n")

            else:
                print("\n ************* You are BUSTED ! Your score is ",
                      this_player.player_score, "... it's OVER 21 ! :  ****************", "\n")

        else:
            print("<>             *** You Won ! Dealer is Busted ! Dealer score: ",
                  this_dealer.dealer_score, " ... which is OVER  21\n")


def playgame_now():

    this_dealer = dealer()

    this_player = player()

    this_play = game()

    this_play.the_game(this_player, this_dealer)


play_game = ''

while play_game != 'q':

    print("\n     ======================= Balckjack 21 =========================\n")
    playgame_now()
    play_game = input("Press y for new game or 'q' to quit!")
