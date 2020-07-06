from src.FuzzyRule import FuzzyRule


class FuzzyBaseRule:
    """
    A class to represent the base of rules for a backward chainer algorithm. Basically, it contains a
    set of conditional expressions which defines the knowledge in the problem's domain.

    """

    def __init__(self):
        self.rules: dict = {}

    def add_rule(self, rule: FuzzyRule):
        pass

