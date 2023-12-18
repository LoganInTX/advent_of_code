import re
import math
from collections import Counter

total = total2 = 0

cards = {'A': 'D', 'K': 'C', 'Q': 'B', 'J': 'A', 'T': '9', '9': '8', '8': '7', '7': '6', '6': '5', '5': '4', '4': '3', '3': '2', '2': '1'}
results = {'5Kind': 7, '4Kind': 6, 'FullHouse': 5, '3Kind': 4, '2Pair': 3, 'Pair': 2, 'HighCard': 1}

with open('./2023/day7_input.txt') as f:
    data = f.read().splitlines()
    
hands = []
for d in data:
    hand, bid = d.split()
    hands.append({'hand': hand,'bid': int(bid)})


def get_hand_type(hand):
    hand_count = Counter(hand)
    if len(hand_count) == 1:
        return '5Kind'
    elif len(hand_count) == 2:
        if 4 in hand_count.values():
            return '4Kind'
        elif 3 in hand_count.values():
            return 'FullHouse'
    elif len(hand_count) == 3:
        if 3 in hand_count.values():
            return '3Kind'
        elif 2 in hand_count.values():
            return '2Pair'
    elif len(hand_count) == 4:
        return 'Pair'
    else:
        return 'HighCard'
    

def get_hand_type_joker(hand, type):
    if hand['hand'] == 'JJQK9':
        print(hand)
    hand_count = Counter(hand['hand'])
    if hand_count.get('J', 0) in (0, 5):
        return type
    elif hand_count.get('J') == 1:
        if hand.get('type') == 'HighCard':
            return 'Pair'
        elif hand.get('type') == 'Pair':
            return '3Kind'
        elif hand.get('type') == '3Kind':
            return '4Kind'
        elif hand.get('type') == '4Kind':
            return '5Kind'
        elif hand.get('type') == '2Pair':
            return 'FullHouse'
    elif hand_count.get('J') == 2:
        if hand.get('type') == 'Pair':
            return '3Kind'
        elif hand.get('type') == '2Pair':
            return '4Kind'
        elif hand.get('type') == 'FullHouse':
            return '5Kind'
        elif hand.get('type') == '2Pair':
            return '4Kind'
    elif hand_count.get('J') == 3:
        if hand.get('type') == '3Kind':
            return '4Kind'
        elif hand.get('type') == 'FullHouse':
            return '5Kind'
    elif hand_count.get('J') == 4:
        return '5Kind'


for hand in hands:
    hand_type = get_hand_type(hand.get('hand'))
    hand['type'] = hand_type
    hand_value = results.get(hand_type, 0)
    hand['value'] = hand_value

# print(hands)


def custom_sort(hand):
    a = hand.get('value')
    b = ''
    for card in hand.get('hand'):
        b += cards.get(card)
    return (a, int(b, 16))
    

ordered_hands = sorted(hands, key=custom_sort)
# print(ordered_hands)

for i, hand in enumerate(ordered_hands):
    total += hand.get('bid') * (i + 1)

print(f'Part 1: {total}')
cards['J'] = '0'

for hand in ordered_hands:
    hand_before = dict.copy(hand)
    hand_type = get_hand_type_joker(hand, hand.get('type'))
    hand_value = results.get(hand_type, 0)
    hand['type'] = hand_type
    hand['value'] = hand_value
    # if 'J' in hand.get('hand', ''):
        # print(hand['hand'], hand_before['type'], hand['type'])

reordered_hands = sorted(ordered_hands, key=custom_sort)

# for h1, h2 in zip(ordered_hands, reordered_hands):
    # print(h1.get('hand'), h1.get('type'), h2.get('hand'), h2.get('type'))

for hand in reordered_hands:
    if hand['hand'] == 'JJQK9':
        print(hand)

for i, hand in enumerate(reordered_hands):
    total2 += hand.get('bid') * (i + 1)

print(f'Part 2: {total2}')
