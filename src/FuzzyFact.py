class FuzzyFact:
    """
    A class to represent a fuzzy fact, i.e. a fact or statement with a value of certainty in the range [-1, 1],
    where -1 means that the fact is a 100% not true, whereas a value of 1 means that the fact is a 100% true,
    finally, a value of 0 means ignorance or lack of knowledge in terms of the fact or statement considered.

    In specific, this application considers facts or statements about animals, therefore, the facts must match
    one of these next formats:
        * el animal tiene [attribute]
        * el animal es [adjective]
    Where both of these sentences are in spanish, and so must the objects created be.
    """

    def __init__(self, obj: str, atr: str, val: str, cv: float = 0):
        """
        Creates a new FuzzyFact object, from a fact or statement in the form of a three-part
        sentence whose parts are:
            * object
            * attribute
            * value
        Also, a certainty value can be assigned to the object as specified before.

        :param obj:     the object of the sentence
        :param atr:     the attribute in the sentence
        :param val:     the value in the sentence
        :param cv:      the certainty value, a float in the range [-1, 1], default value is 0
        """
        self.obj: str = obj
        self.atr: str = atr
        self.val: str = val
        self.cv: float = 0.0
        self.assign_cv(cv)

    def assign_cv(self, cv: float):
        """
        Assigns the certainty value to the FuzzyFact object. It makes sure the value is in the range [-1, 1]
        """
        assert -1 <= cv <= 1, 'Certainty value is not in the range [-1, 1]'
        self.cv: float = cv

    def __repr__(self):
        sentence = ' '.join([self.obj, self.atr, self.val])
        sentence = f'(({sentence}) {self.cv})'
        return sentence


if __name__ == "__main__":
    fact1 = FuzzyFact('el animal', 'tiene', 'pelo')
    fact1.assign_cv(0.9)

    print(fact1)
