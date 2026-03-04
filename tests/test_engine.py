from dockfleet.core.orchestrator import Orchestrator


def test_create_when_empty_state():
    desired = {
        "services": {
            "nginx": {"image": "nginx:latest"}
        }
    }

    state = {}

    orchestrator = Orchestrator()
    plan = orchestrator.generate_plan(desired, state)

    assert len(plan.to_create) == 1
    assert plan.to_create[0]["name"] == "nginx"
    assert len(plan.to_remove) == 0