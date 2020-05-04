import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('emailid', 'password')
conn.sendemail('sender's-emailid', 'receiver's-emailed', 'Subject: Test Email\n\nHey This is email shoot from a python program\n\n-Kanchan')
conn.quit()
