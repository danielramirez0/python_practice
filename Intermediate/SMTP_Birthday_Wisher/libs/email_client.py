import smtplib as s

def send_email(target, cred, subject, message):
    with s.SMTP(cred.hostname) as client:
            client.starttls()
            client.login(user=cred.username, password=cred.password)
            client.sendmail(
                from_addr=cred.username,
                to_addrs=target,
                msg=f"Subject:{subject}\n\n{message}"
            )