from ticket import create_ticket
from display import display_ticket
def main():

    ticket = create_ticket()

    priority = ticket[4]

    if priority.lower() in ["high", "medium", "low"]:
        display_ticket(*ticket)
    else:
        print("Invalid Priority Level!")


if __name__ == "__main__":
    main()