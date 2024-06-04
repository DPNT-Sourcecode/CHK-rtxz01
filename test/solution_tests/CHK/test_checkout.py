from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout(True) == -1
        assert checkout_solution.checkout("ABC12D") == -1
        assert checkout_solution.checkout(["A", "B", True, "C"]) == -1
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10
        "G": {KEY_SINGLECOST: 20, },
        "H": {KEY_SINGLECOST: 10, },
        "I": {KEY_SINGLECOST: 35, },
        "J": {KEY_SINGLECOST: 60, },
        "K": {KEY_SINGLECOST: 80, },
        "L": {KEY_SINGLECOST: 90, },
        "M": {KEY_SINGLECOST: 15, },
        "N": {KEY_SINGLECOST: 40, },
        "O": {KEY_SINGLECOST: 10, },
        "P": {KEY_SINGLECOST: 50, },
        "Q": {KEY_SINGLECOST: 30, },
        "R": {KEY_SINGLECOST: 50, },
        "S": {KEY_SINGLECOST: 30, },
        "T": {KEY_SINGLECOST: 20, },
        "U": {KEY_SINGLECOST: 40, },
        "V": {KEY_SINGLECOST: 50, },
        "W": {KEY_SINGLECOST: 20, },
        "X": {KEY_SINGLECOST: 90, },
        "Y": {KEY_SINGLECOST: 10, },
        "Z": {KEY_SINGLECOST: 50, },
        assert checkout_solution.checkout("ABCDEF") == 165
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBAAABB") == 220
        assert checkout_solution.checkout("CD") == 35
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40


        # I don't think ths is the intended implementation. Buying 4 E gives you a further 15 discount
        # second revision of this, my assert may be incorrect due to my new understanding of how multiprice works
        # assert checkout_solution.checkout("EEBB") == 80 + (45 - 30)
        # My assumption before was incorrect, the correct expected result here was 160
        # assert checkout_solution.checkout("EEEEBB") == 160 + (45 - 60)
        # Tests that falied when I deployed:
        assert checkout_solution.checkout("AAAAA") == 200 # Got 230
        assert checkout_solution.checkout("AAAAAA") == 250 # Got 260
        assert checkout_solution.checkout("AAAAAAA") == 300 # Got 310
        # Mistake was missing out the second added promo for the 5 purchase of A
        assert checkout_solution.checkout("AAAAAAAA") == 330 # Got 350
        assert checkout_solution.checkout("AAAAAAAAA") == 380 # Got 400
        assert checkout_solution.checkout("EEEEBB") == 160 # Got 145
        # Error made in finding best discount for multi discount A
        # Error made in understanding of 2E one free B as documented above
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455  # Got 470
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665  # Got 695
        # 455 vs 470 result means I'm not calculating the 2B discount properly
        # This was due to a silly error in a =- b rather than  a = a - b, oops, should have function tested that!




