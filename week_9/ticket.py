def create_ticket():
    print("=== IT Helpdesk Ticket ===")

    student_name = input("Student Name : ")
    student_id = input("Student ID : ")
    issue = input("Issue : ")
    location = input("Location : ")

    priority = input("Priority (High/Medium/Low): ")

    # Assign technician
    if priority.lower() == "high":
        technician = "Ahmad"
    elif priority.lower() == "medium":
        technician = "Siti"
    else:
        technician = "Ali"

    status = "Pending"

    return (
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician,
        status
    )