from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        # Bad inputs
        assert checkout_solution.checkout(True) == -1
        assert checkout_solution.checkout("ABC12D") == -1
        assert checkout_solution.checkout(["A", "B", True, "C"]) == -1
        # single item tests
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("G") ==  20
        assert checkout_solution.checkout("H") ==  10
        assert checkout_solution.checkout("I") ==  35
        assert checkout_solution.checkout("J") ==  60
        assert checkout_solution.checkout("K") ==  80
        assert checkout_solution.checkout("L") ==  90
        assert checkout_solution.checkout("M") ==  15
        assert checkout_solution.checkout("N") ==  40
        assert checkout_solution.checkout("O") ==  10
        assert checkout_solution.checkout("P") ==  50
        assert checkout_solution.checkout("Q") ==  30
        assert checkout_solution.checkout("R") ==  50
        assert checkout_solution.checkout("S") ==  30
        assert checkout_solution.checkout("T") ==  20
        assert checkout_solution.checkout("U") ==  40
        assert checkout_solution.checkout("V") ==  50
        assert checkout_solution.checkout("W") ==  20
        assert checkout_solution.checkout("X") ==  90
        assert checkout_solution.checkout("Y") ==  10
        assert checkout_solution.checkout("Z") ==  50
        # Multibuy tests
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("AAAA") == 180
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBBBB") == 120
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("KK") == 150
        assert checkout_solution.checkout("KKK") == 230
        assert checkout_solution.checkout("KKKK") == 300
        assert checkout_solution.checkout("KKKKK") == 380
        assert checkout_solution.checkout("KKKKKK") == 450
        assert checkout_solution.checkout("PPPPP") == 200
        assert checkout_solution.checkout("PPPPPP") == 250
        assert checkout_solution.checkout("PPPPPPP") == 300
        assert checkout_solution.checkout("PPPPPPPPPP") == 400
        assert checkout_solution.checkout("PPPPPPPPPPP") == 450
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("QQQQ") == 110
        assert checkout_solution.checkout("QQQQQQ") == 160
        assert checkout_solution.checkout("QQQQQQQ") == 190
        assert checkout_solution.checkout("VV") == 90
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("VVVV") == 180
        assert checkout_solution.checkout("VVVVV") == 220
        assert checkout_solution.checkout("VVVVVV") == 260
        # Multiprice tests
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("NNNMM") == 135
        assert checkout_solution.checkout("NNNNNNMM") == 240
        # Complex multiprice (mixed with multibuy)

        # buy x get y free tests
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("UUU") == 120
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("UUUUU") == 160
        assert checkout_solution.checkout("UUUUUU") == 240
        assert checkout_solution.checkout("UUUUUUU") == 200
        assert checkout_solution.checkout("UUUUUUUU") == 240



        #Mixed tests
        assert checkout_solution.checkout("ABCDEF") == 165
        assert checkout_solution.checkout("BBAAABB") == 220
        assert checkout_solution.checkout("CD") == 35
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665

"""
Past failed tests have been incorporeted to tests above, but it's worth keeping
track of my mistakes here.
"""

        # I don't think ths is the intended implementation. Buying 4 E gives you a further 15 discount
        # second revision of this, my assert may be incorrect due to my new understanding of how multiprice works
        # assert checkout_solution.checkout("EEBB") == 80 + (45 - 30)
        # My assumption before was incorrect, the correct expected result here was 160
        # assert checkout_solution.checkout("EEEEBB") == 160 + (45 - 60)
        # Tests that falied when I deployed:
        # assert checkout_solution.checkout("AAAAA") == 200 # Got 230
        # assert checkout_solution.checkout("AAAAAA") == 250 # Got 260
        # assert checkout_solution.checkout("AAAAAAA") == 300 # Got 310
        # Mistake was missing out the second added promo for the 5 purchase of A
        # assert checkout_solution.checkout("AAAAAAAA") == 330 # Got 350
        # assert checkout_solution.checkout("AAAAAAAAA") == 380 # Got 400
        # assert checkout_solution.checkout("EEEEBB") == 160 # Got 145
        # Error made in finding best discount for multi discount A
        # Error made in understanding of 2E one free B as documented above
        # assert checkout_solution.checkout("AAAAAEEBAAABB") == 455  # Got 470
        # assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665  # Got 695
        # 455 vs 470 result means I'm not calculating the 2B discount properly
        # This was due to a silly error in a =- b rather than  a = a - b, oops, should have function tested that!








