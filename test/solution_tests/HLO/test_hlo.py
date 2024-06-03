from solutions.HLO import hello_solution


class TestSum():
    def test_sum(self):
        assert hello_solution.hello.compute("John") == "Hello, John!"

    def test_sum_one(self):
        assert hello_solution.hello.compute("Jim") == "Hello, Jim!"

    def test_sum_two(self):
        assert hello_solution.hello.compute("James") == "Hello, James!"



