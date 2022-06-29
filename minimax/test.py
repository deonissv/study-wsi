from game import *


def test_depth():
    test_values = [1,2,3,5]
    print('depth test, 1st evalutain algorithm')
    print('-'*41)
    print(f'|{"w/b":^7}|' + ''.join([f'{x:^7}|' for x in test_values]))
    for w in test_values:
        test_results = []
        for b in test_values:
            test_results.append(bot_game(w, b, evaluate, evaluate))
        print('-'*41)
        print(f'|{w:^7}|' + ''.join([f'{x:^7}|' for x in test_results]))
    print('-'*41)

def test_eval(depth):
    a = 15
    test_values = [evaluate, evaluate_alt1, evaluate_alt2, evaluate_alt3]
    print(f'evalutain algorithms test, depth = {depth}')
    print('-'*81)
    print(f"|{'w/b' : ^15}|" + ''.join([f'{x.__name__: ^15}|' for x in test_values]))
    for w in test_values:
        test_results = []
        for b in test_values:
            test_results.append(bot_game(depth, depth, w, b))
        print('-'*81)
        print(f'|{w.__name__:^15}|' + ''.join([f'{x:^15}|' for x in test_results]))
    print('-'*81)

def main():
    test_depth()
    test_eval(3)

if __name__ == "__main__":
    main()


# Czy gracz sterowany przez AI zachowuje się rozsądnie z ludzkiego punktu widzenia? Jeśli nie to co jest nie tak?
#     Zachowanie AI może mieć jakiś sens, Trudno powiedzieć, że decyzje AI są rozsądne.
#     Poziom takiego przeciwnika jest porównuwalny z początkujączym graczem-człowiekiem.

# Jak widać w tabeli poniżej, wyniki są porównywalne, czyli ani zmiana głębokości, ani funkcji heurystycznej
# nie ma większego wpływu na wyniki. Biały wygrywa prawie zawsze, bo ma pierwszy ruch

# depth test, 1st evalutain algorithm
# -----------------------------------------
# |  w/b  |   1   |   2   |   3   |   5   |
# -----------------------------------------
# |   1   | blue  | white | draw  | draw  |
# -----------------------------------------
# |   2   | white | draw  | draw  | draw  |
# -----------------------------------------
# |   3   | white | white | white | white |
# -----------------------------------------
# |   5   | white | white | white | draw  |
# -----------------------------------------

# evaluation algorithms test, depth = 3
# ---------------------------------------------------------------------------------
# |      w/b      |   evaluate    | evaluate_alt1 | evaluate_alt2 | evaluate_alt3 |
# ---------------------------------------------------------------------------------
# |   evaluate    |     white      |    white     |     white     |     draw      |
# ---------------------------------------------------------------------------------
# | evaluate_alt1 |     white      |    white     |     white     |     draw      |
# ---------------------------------------------------------------------------------
# | evaluate_alt2 |     draw      |     white     |     draw      |     blue      |
# ---------------------------------------------------------------------------------
# | evaluate_alt3 |     draw      |     white     |     draw      |     draw      |
# ---------------------------------------------------------------------------------
