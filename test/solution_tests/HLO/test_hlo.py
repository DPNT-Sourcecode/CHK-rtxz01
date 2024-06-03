from solutions.HLO import hello_solution


class TestHlo():
    def test_hlo(self):
        assert hello_solution.hello("John") == "Hello, John!"
        assert hello_solution.hello("Jim") == "Hello, Jim!"
        assert hello_solution.hello("James") == "Hello, James!"


