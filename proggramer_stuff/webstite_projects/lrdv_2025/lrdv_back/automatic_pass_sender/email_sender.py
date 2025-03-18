from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from password_maker import pas_gen
import sys
from email.utils import parseaddr

# TODO: Change before uploading for security reasons
# DO NOT TOUCH!!!!!

def is_valid_email(email):
    return "@" in email and "." in email and parseaddr(email)[1] == email

def send_mail(email_trim, parola_noua):
    if not is_valid_email(email_trim):
        print("Invalid email address. Email not sent.")
        return  # Stop execution if email is invalid

    pass_app = "ldbv ceko fsvt hrfn"

    smpt = smtplib.SMTP('smtp.gmail.com', 587)
    smpt.ehlo()
    smpt.starttls()
    smpt.login("pricopcristian188@gmail.com", pass_app)

    mes = MIMEMultipart()
    mes['To'] = email_trim
    mes['From'] = 'pricopcristian188@gmail.com'
    mes['Subject'] = "No reply"

    text = "Bun venit la LRDV. Aceasta este parola dumneavoastră, vă rugăm să o notați. În caz de pierdere, NU o puteți recupera: " + parola_noua
    mes.attach(MIMEText(text, 'plain'))

    smpt.sendmail("pricopcristian188@gmail.com", email_trim, mes.as_string())
    smpt.quit()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        send_mail(sys.argv[1], sys.argv[2])
    else:
        print("No email provided.")
