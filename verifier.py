def verify(intent, actions, allowed_action, max_amount):
    results = []

    for act in actions:
        if act["action"] != allowed_action:
            results.append((act, "BLOCKED"))
        elif act.get("amount", 0) > max_amount:
            results.append((act, "BLOCKED"))
        else:
            results.append((act, "ALLOWED"))

    return results
