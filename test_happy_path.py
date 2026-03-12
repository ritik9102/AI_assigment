from app.engine.workflow_engine import WorkflowEngine

def test_happy_path():

    engine = WorkflowEngine("loan_approval")

    decision, rule = engine.process({"credit_score": 780})

    assert decision == "approve"
