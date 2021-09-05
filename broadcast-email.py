import smtplib
import getpass
import re


def get_domain(email):
    match = re.search('@', email)
    n = match.start()

    match2 = re.search('.com', email)
    m = match2.start()

    s = email[n + 1:m]
    return s


def send_mails(contents):
    global smtp_obj, email
    print("Please use APP PASSWORD if using GMAIL ")
    print()
    print()

    while (True):
        try:
            email = input("Email ID :")
            password = input("Password : ")
            print()
            print("Please wait while we establish a secure connection.....")
            print("\n")
            s = get_domain(email)
            smtp_obj = smtplib.SMTP('smtp.' + s + '.com', 587)
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.login(email, password)

        except:
            print("Some error occurred.Please re-enter your email and password.")
            continue

        else:
            print("Connected to your mail server.")
            break
    print()
    print()

    subject = input("SUBJECT : ")
    print()
    message = input("MESSAGE : ")

    msg = 'Subject: ' + subject + '\n' + message

    try:
        for i in contents:
            smtp_obj.sendmail(email, i, msg)

    except:
        print("Some error occurred. ")

    else:

        smtp_obj.quit()

        print()
        print("Emails sent. ")


def get_email():
    file_name = input("Enter file name(if file present in same folder as program) or file path : ")
    with open(file_name, mode='r') as f:
        contents = f.readlines()

    print()
    print()

    send_mails(contents)


def main():
    get_email()


if __name__ == '__main__':
    main()
