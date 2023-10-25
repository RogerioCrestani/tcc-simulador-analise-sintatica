def bottom_up_algorithm(action_table, goto_table, input):
    stack = ["0"]
    pointer = 0

    input_tape = input.split(" ")
    input_tape.append("$")

    # Detalhamento do passo a passo
    detailed_steps = [
        {
            "stepByStep": ["Inicio da analise"],
            "stack": stack[::-1].copy(),
            "input": input_tape.copy(),
            "pointer": pointer,
            "stepMarker": ["", ""],
        }
    ]

    run = True
    while run == True:
        # Label do passo a passo
        step_by_step = []

        action = ["", ""]
        transition = ["", ""]

        action[0] = int(stack[len(stack) - 1]) + 1
        action[1] = input_tape[pointer]

        action_movement = action_table[action[1]][action[0]].split("[")
        action_movement[0] = action_movement[0].strip()
        if action_movement[0] != "ACEITO" and "ERRO!":
            action_movement[1] = action_movement[1].strip("]")
            action_movement[1] = action_movement[1].strip()

        step_by_step.append(f"AÇÃO[{action[1]}, {action[0] - 1}] => {action_movement}")
        detailed_steps.append(
            {
                "stepByStep": step_by_step.copy(),
                "stack": stack[::-1].copy(),
                "input": input_tape.copy(),
                "pointer": pointer,
                "stepMarker": [f"{action[1]}", action[0] - 1],
            }
        )

        if action_movement[0][0] == "R":
            action_movement[1] = action_movement[1][:-1]
            reduce_div = action_movement[1].split(" ")
            qt_unstack = 2 * len(reduce_div[2:])

            for i in range(qt_unstack):
                stack.pop()

            step_by_step.append(f"Desempilhar {qt_unstack}")
            detailed_steps.append(
                {
                    "stepByStep": step_by_step.copy(),
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )

            transition[0] = int(stack[len(stack) - 1]) + 1
            transition[1] = reduce_div[0]
            goto_movement = goto_table[transition[1]][transition[0]]

            step_by_step.append(
                f"TRANSIÇÃO[{transition[1]}, {transition[0] - 1}] => {goto_movement}"
            )
            detailed_steps.append(
                {
                    "stepByStep": step_by_step.copy(),
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": [f"{transition[1]}", transition[0] - 1],
                }
            )
            if goto_movement[0] == "E":
                stack.append(reduce_div[0])
                stack.append(str(int(goto_movement[10])))
            else:
                break

            step_by_step.append(
                f"Empilhar {reduce_div[0]}, {str(int(goto_movement[10]))}"
            )
            detailed_steps.append(
                {
                    "stepByStep": step_by_step.copy(),
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )
            aux_step_action = [
                f"Reduzir: {action_movement[1]}",
                f"GOTO[{transition[0]},{transition[1]}] => {goto_movement}",
                f"Empilhar: {reduce_div[0]}, {str(int(goto_movement[10]))}",
            ]
        elif action_movement[0][0] == "E":
            print("teste")
            print(action_movement)
            print(action[1])
            stack.append(action[1])
            stack.append(action_movement[1])
            print(stack)

            step_by_step.append(f"Empilhar: {action[1]}, {action_movement[0][1]}")
            detailed_steps.append(
                {
                    "stepByStep": step_by_step.copy(),
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )

            aux_step_action = [f"Empilhar: {action[1]}, {action_movement[0][1]}"]
            pointer += 1
        elif action_movement[0][0] == "A":
            step_by_step.append(f"A entrada foi aceita!")
            detailed_steps.append(
                {
                    "stepByStep": step_by_step.copy(),
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )
            break
        elif action_movement[0] == "ERRO!":
            step_by_step.append(f"A entrada não está correta.")
            detailed_steps.append(
                {
                    "stepByStep": step_by_step.copy(),
                    "stack": stack[::-1].copy(),
                    "input": input_tape.copy(),
                    "pointer": pointer,
                    "stepMarker": ["", ""],
                }
            )
            break
        else:
            return {"Erro": "Houve um erro!"}
    return detailed_steps
