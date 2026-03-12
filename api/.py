from fastapi import APIRouter
from app.engine.workflow_engine import WorkflowEngine
from app.models.request_model import WorkflowRequest

router = APIRouter()

@router.post("/workflow/start")
def start_workflow(req: WorkflowRequest):

    engine = WorkflowEngine(req.workflow)

    decision, rule = engine.process(req.data)

    return {
        "decision": decision,
        "rule_triggered": rule
    }
