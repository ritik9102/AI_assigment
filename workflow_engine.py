import yaml
from app.engine.rule_engine import RuleEngine

class WorkflowEngine:

    def __init__(self, workflow):

        with open("config/workflows.yaml") as f:

            workflows = yaml.safe_load(f)

        self.rules = workflows[workflow]["rules"]

    def process(self, data):

        rule_engine = RuleEngine(self.rules)

        decision, rule = rule_engine.evaluate(data)

        return decision, rule
