while(True):
    n = int(input())
    if(n == 0): exit()

    deck = list(range(1, n+1))
    deck = deck[::-1] # reverse
    discated_cards = []
    discated_cards_str = ''

    while(len(deck) > 1):
        # print(deck)
        # print(discated_cards)
        discated_cards.append(deck.pop())
        poped = deck.pop()
        deck.insert(0, poped)

    # print(discated_cards)
    
    for i, card in enumerate(discated_cards, start=1):
        if(i < len(discated_cards)): discated_cards_str += str(card) + ', '
        else: discated_cards_str += str(card)
    
    print('Discarded cards:', discated_cards_str)
    print('Remaining card:', deck[0])