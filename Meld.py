from itertools import permutations

def get_melds(cmbs):
    melds = []

    while len(cmbs) > 0:
        curr_cmb = cmbs.pop()
        if is_meld(curr_cmb):
            melds.append(curr_cmb)
            cmbs = [cmb for cmb in cmbs for card in curr_cmb if card not in cmb]

    if len(melds) == 0:
        return None
    else:
        return melds

def is_meld(cmb):
    meld_rank = cmb[0][0]
    meld_suit = cmb[0][1]

    for card in cmb:
        rank = card[0]
        suit = card[1]
        if rank != meld_rank:
            is_rank_meld = False
            break
        else:
            is_rank_meld = True

    if is_rank_meld:
        return is_rank_meld

    for idx in range(len(cmb)):
        card = cmb[idx]
        rank = card[0]
        suit = card[1]
        if suit != meld_suit:
            is_suit_meld = False
            break
        else:
            if idx == 0:
                continue
            else:
                prev_card = cmb[idx - 1]
                if calculate_rank(prev_card) + 1 == calculate_rank(card):
                    is_suit_meld = True
                else:
                    is_suit_meld = False
                    break

    return is_suit_meld
        
def calculate_rank(card):
    rank = card[0]
    if rank == "A":
        return 1
    elif rank == "T":
        return 10
    elif rank == "K":
        return 11
    elif rank == "Q":
        return 12
    elif rank == "J":
        return 13
    else:
        return int(rank)

def main():
    stash_deck = ['3H', 'TH', '7H', '3S', 'AS', 'JH', 'QH', 'AH', 'AD', 'KH']
    cmb_3 = list(permutations(stash_deck, 3))
    res = get_melds(cmb_3)
    print(res)

main()
