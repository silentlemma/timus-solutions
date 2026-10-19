"""Usage: gen.py SEED MODE; random,exhaustive,chain,bounce_dense,check_only,clone_only,clone_fan,bounce_checks,numeric_checks."""

import random
import sys

MAXIMUM = 500000
TRACE_DEPTH = 4
SMALL_PROGRAMS = 2
MAX_ENTITIES = 2


def apply(state, command, programs):
    parts = command.split()
    operation, entity = parts[0], int(parts[1]) - 1
    assert 0 <= entity < len(state)
    learned, redo = state[entity]
    if operation == "learn":
        program = int(parts[2])
        assert 1 <= program <= programs and program not in learned
        learned.append(program)
        redo.clear()
    elif operation == "rollback":
        assert learned
        redo.append(learned.pop())
    elif operation == "relearn":
        assert redo and redo[-1] not in learned
        learned.append(redo.pop())
    elif operation == "clone":
        state.append((learned.copy(), redo.copy()))
    else:
        assert operation == "check"
        return str(learned[-1]) if learned else "basic"
    return None


def interpret(programs, commands):
    state, answers = [([], [])], []
    for command in commands:
        answer = apply(state, command, programs)
        if answer is not None:
            answers.append(answer)
    return answers


def exhaustive():
    traces = []

    def visit(state, commands):
        if len(commands) == TRACE_DEPTH:
            traces.append(commands)
            return
        options = []
        for i, (learned, redo) in enumerate(state, 1):
            options.append(f"check {i}")
            options.extend(
                f"learn {i} {p}" for p in range(1, SMALL_PROGRAMS + 1) if p not in learned
            )
            if learned:
                options.append(f"rollback {i}")
            if redo:
                options.append(f"relearn {i}")
            if len(state) < MAX_ENTITIES:
                options.append(f"clone {i}")
        for command in options:
            changed = [(a.copy(), r.copy()) for a, r in state]
            apply(changed, command, SMALL_PROGRAMS)
            visit(changed, commands + [command])

    visit([([], [])], [])
    commands, entities = [], 1
    for trace in traces:
        commands.append("clone 1")
        entities += 1
        mapping = {1: entities}
        local = [([], [])]
        for command in trace:
            parts = command.split()
            translated = parts[0] + " " + str(mapping[int(parts[1])])
            if parts[0] == "learn":
                translated += " " + parts[2]
            commands.append(translated)
            apply(local, command, SMALL_PROGRAMS)
            if parts[0] == "clone":
                entities += 1
                mapping[len(local)] = entities
        # Reveal every learned and redo element, so unobserved history errors cannot hide.
        for i, (learned, redo) in enumerate(local, 1):
            target = mapping[i]
            commands.append(f"check {target}")
            while redo:
                commands.extend((f"relearn {target}", f"check {target}"))
                learned.append(redo.pop())
            while learned:
                commands.extend((f"rollback {target}", f"check {target}"))
                learned.pop()
    assert len(commands) <= MAXIMUM
    return SMALL_PROGRAMS, commands, len(traces)


def generate(seed, mode):
    if mode == "exhaustive":
        programs, commands, _ = exhaustive()
        return programs, commands
    if mode == "random":
        rng = random.Random(seed)
        programs, state, commands = rng.randint(1, 12), [([], [])], []
        for _ in range(1200):
            entity = rng.randrange(len(state))
            learned, redo = state[entity]
            available = [p for p in range(1, programs + 1) if p not in learned]
            kinds = ["check"] * 3
            if available:
                kinds.extend(["learn"] * 3)
            if learned:
                kinds.extend(["rollback"] * 3)
            if redo:
                kinds.extend(["relearn"] * 3)
            if len(state) < 40:
                kinds.append("clone")
            kind = rng.choice(kinds)
            command = f"{kind} {entity + 1}"
            if kind == "learn":
                command += f" {rng.choice(available)}"
            commands.append(command)
            apply(state, command, programs)
        return programs, commands
    count = MAXIMUM
    if mode == "chain":
        commands = [f"learn 1 {p}" for p in range(1, count + 1)]
    elif mode == "bounce_dense":
        commands = ["learn 1 1"] + ["rollback 1", "relearn 1"] * ((count - 2) // 2) + ["check 1"]
    elif mode == "check_only":
        commands = ["check 1"] * count
    elif mode == "numeric_checks":
        commands = [f"learn 1 {count}"] + ["check 1"] * (count - 1)
    elif mode == "clone_only":
        commands = ["clone 1"] * count
    elif mode == "clone_fan":
        depth, copies = 200000, 100000
        commands = [f"learn 1 {p}" for p in range(1, depth + 1)] + ["clone 1"] * copies
        for entity in range(2, copies + 2):
            commands.extend((f"rollback {entity}", f"check {entity}"))
    else:
        assert mode == "bounce_checks"
        commands = (
            ["learn 1 1"]
            + ["rollback 1", "check 1", "relearn 1", "check 1"] * 124999
            + ["check 1"] * 3
        )
    assert len(commands) == count
    return count, commands


def render(programs, commands):
    return f"{len(commands)} {programs}\n" + "\n".join(commands) + "\n"


if __name__ == "__main__":
    sys.stdout.write(render(*generate(int(sys.argv[1]), sys.argv[2])))
