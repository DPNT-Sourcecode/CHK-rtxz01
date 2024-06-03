from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout(True) == -1
        assert checkout_solution.checkout("ABC12D") == -1
        assert checkout_solution.checkout(["A", "B", True, "C"]) == -1
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAA") == 130




