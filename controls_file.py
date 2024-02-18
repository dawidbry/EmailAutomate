import csv

class Control:
    """There are needed this information to send the request:
    control number, email address of control owner, control name, requested documentation,
    date of delivery of documents, period for which documentation is requested"""
    def __init__(self, control_number, email_control_owner, control_name, documentation, date, period):
        self.control_number = control_number
        self.email_control_owner = email_control_owner
        self.control_name = control_name
        self.documentation = documentation
        self.date = date
        self.period = period

    def __str__(self):
        return f"control_number: {self.control_number}"

# There are needed information to sending emails in this csv file
csv_file_path = r'C:\Users\dawid\PycharmProjects\EmailAutomate\controls.csv'

def load_controls_from_csv(csv_file_path):
    controls = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            control = Control(
                control_number=row['control_number'],
                email_control_owner=row['email_control_owner'],
                control_name=row['control_name'],
                documentation=row['documentation'],
                date=row['date'],
                period=row['period']
            )
            controls.append(control)
    return controls

# to check the correctness of downloading data from the csv file
controls = load_controls_from_csv(csv_file_path)
for control in controls:
    print(control)
