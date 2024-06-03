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
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("BBAAABB") == 220
        assert checkout_solution.checkout("CD") == 35
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEBB") == 80 + (45 - 30)
        assert checkout_solution.checkout("EEEEBB") == 80 + (45 - 60)


