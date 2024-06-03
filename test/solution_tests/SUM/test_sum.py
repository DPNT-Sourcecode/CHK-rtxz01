from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_one(self):
        assert sum_solution.compute(5, 5) == 3

    def test_sum_two(self):
        assert sum_solution.compute(10000, 10) == 3



