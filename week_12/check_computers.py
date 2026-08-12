def check_computers():
    computers = []  # initial value

   
    for number in range(5):

        status = input(f"Computer {number + 1} Status (A/U/M): ").upper()

        computers.append(status)

    return computers