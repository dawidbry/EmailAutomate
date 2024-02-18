import win32com.client as client
from controls_file import controls

for control in controls:
    outlook = client.Dispatch('Outlook.Application')
    message = outlook.CreateItem(0)
    message.Display()
    message.To = control.email_control_owner
    message.Subject = f'2023 Year End Audit - {control.control_number} - {control.control_name}'
    message.CC = 'eric.mcdonald@internalaudit.com;jessica.novak@internalaudit.com'
    message.HTMLBody = f"""
        <div>
            <p style='font-family: "Calibri";font-size=14'>
                Hi {control.name},
                <br>
                <br>
                Internal Audit is currently starting annual SOX testing and we are reaching out to you
                regarding the following control:
                <br>
                {control.control_name} - {control.control_name}.
                <br>
                <br>
                For this, we kindly request you to provide the following documents for <b>{control.period}</b>:
                    <p style='margin-left: 20px'>• {control.documentation}</p>
                We would like to have the requested information by <b>{control.date}</b>.
                Please advise in case you are not able to meet that.
                <br>
                <br>
                Please do not hesitate to contact me or audit manager if you have any questions.
                <br>
                <br>
                Thank you for your help.
                <br>
                <br>
                Best regards,
                <br>
                Dawid Brygier 
                <br>
                Internal Auditor
            </p>
        </div>       
        """

# below is the code for automatic sending:
    # mail.Send()
