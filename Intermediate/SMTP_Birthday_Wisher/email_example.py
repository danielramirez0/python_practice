import smtplib

# each email service has security features (usually Allow less secure apps) which need to be set correctly for the SMTP service to work
example_email = "example@gmail.com"
example_password = "abcd1234()"

# can use traditional open/close() format
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.do_stuff()
# connection.close()

# or use with keyword like files
# each provider has a unique smtp address (smtp.mail.yahoo.com)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # start TLS connection
    connection.login(user=example_email, password=example_password)
    connection.sendmail(
        from_addr=example_email,
        to_addrs="another_email@yahoo.com",
        msg="Subject: Hello\n\nThis is the body of message"
    )
