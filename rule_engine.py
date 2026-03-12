class RuleEngine:

    def __init__(self, rules):

        self.rules = rules

    def evaluate(self, data):

        for rule in self.rules:

            condition = rule["condition"]

            if eval(condition, {}, data):

                return rule["action"], condition

        return "manual_review", "no_rule_matched"
