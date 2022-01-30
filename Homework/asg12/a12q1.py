import sys as SYS
import smtplib, ssl

    #TODO: Send email here

#email = sagartemporaryaddress S@ggers6
def getFiles(dirPath):
    pass
def sendMail():
    port = 465  # For SSL
    password = "S@ggers6"
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sagartemporaryaddress@gmail.com", password)
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "my@gmail.com"
    password = input("Type your password and press enter: ")
    # Create a secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 
def main():
    mainPath = "H:\\"
    ARGS = SYS.argv

if __name__ == '__main__':
    main()

"""http://216.58.192.142/"""