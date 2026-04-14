def verify(intent, actions):
    results = []

    for act in actions:
        if act["action"] != intent["action"]:
            results.append((act, "BLOCKED"))
        else:
            results.append((act, "ALLOWED"))

    return results
