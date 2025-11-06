class Wallet:
    def __init__(self, price):
        self.price = price
        self.__list_of_cards = []

    def add_card(self, credit_card_obj):
        self.__list_of_cards.append(credit_card_obj)

    def show_cards(self):
        for card_obj in self.__list_of_cards:
            print(card_obj.card_number)


class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

cc_1 = CreditCard(23456899865)
cc_2 = CreditCard(356765433322)

wallet_1 = Wallet(50.60)

wallet_1.add_card(cc_1)
wallet_1.add_card(cc_2)

wallet_1.show_cards()