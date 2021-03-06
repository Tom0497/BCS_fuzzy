from src.FuzzyFact import FuzzyFact
from typing import List


class FuzzyRule:
    """
    A class to represent a rule in the backward chainer algorithm (BCA). A rule is an object that contains
    an identifier, premises and conclusions, both premises and conclusions are represented by FuzzyFact objects.
    In the same manner as an inference system, a rule uses the certainty value of each premise to compute the
    certainty value of each conclusion.

    It's important to notice that premises of a rule are facts whose certainty value is unknown, therefore a
    system of questions is required to determine it.
    """

    def __init__(self, rule_id: str, premises: List[FuzzyFact], conclusions: List[FuzzyFact]):
        """
        Creates a new FuzzyRule object, from a set of premises and a set of conclusions, both in a List format.
        Also, an identifier must be passed in a string format, this feature becomes useful when using a FuzzyBaseRule
        object.

        :param rule_id:         an string to identify the rule, e.g 'R1'
        :param premises:        List of FuzzyFacts whose certainty value is not known.
        :param conclusions:     List of FuzzyFacts that take it certainty value depending on the premises.
        """
        self.rule_id: str = rule_id
        self.premises: List[FuzzyFact] = premises
        self.conclusions: List[FuzzyFact] = conclusions


if __name__ == "__main__":
    premise_1 = FuzzyFact('el animal', 'tiene', 'pelo')

    conclusion_1 = FuzzyFact('el animal', 'es', 'mamifero', 0.8)
    conclusion_2 = FuzzyFact('el animal', 'es', 'ave', -1.0)
    conclusion_3 = FuzzyFact('el animal', 'es', 'leche', -1.0)

    r1_premises = [premise_1]
    r1_conclusions = [conclusion_1, conclusion_2, conclusion_3]

    rule_1 = FuzzyRule('R1', r1_premises, r1_conclusions)
