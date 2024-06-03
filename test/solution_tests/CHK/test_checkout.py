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
        assert checkout_solution.checkout("ABCDE") == 155
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBAAABB") == 220
        assert checkout_solution.checkout("CD") == 35
        assert checkout_solution.checkout("EEB") == 80
        # I don't think ths is the intended implementation. Buying 4 E gives you a further 15 discount
        assert checkout_solution.checkout("EEBB") == 80 + (45 - 30)
        assert checkout_solution.checkout("EEEEBB") == 160 + (45 - 60)
        # Tests that falied when I deployed:
        assert checkout_solution.checkout("AAAAA") == 200 # Got 230
        assert checkout_solution.checkout("AAAAAA") == 250 # Got 260
        assert checkout_solution.checkout("AAAAAAA") == 300 # Got 310




