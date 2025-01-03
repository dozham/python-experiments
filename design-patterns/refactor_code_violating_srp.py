## Refactor the following code:
# class UserManager:
#     def create_user(self, name, email):
#         print(f"Creating user: {name}, {email}")
#         # Code to save user to a database
#
#     def send_welcome_email(self, email):
#         print(f"Sending welcome email to {email}")
#         # Code to send email

# This follows the SRP (single-responsibility principle) I suppose
class UserManager:
    def create_user(self, name: str, email: str):
        print(f"Creating user with name={name} and email={email}")

class EmailSender:
    def send_email(self, email: str):
        print(f"Sending email to address {email}")


