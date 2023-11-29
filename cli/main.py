import click
import smtplib
from email.mime.text import MIMEText
import sys
sys.path.insert(0,"..")
from database.config import Database

@click.group()
def cli():
    pass

@click.command()
@click.option('--mail', help="Enter your email with 2 factor athentication")
@click.option('--password', help="You need to get a Google 2 factor authentication code")
def changeConfig(mail,password):
        
        if(mail):
            try:
                with open('user-config.txt','r') as f:
                    userConfig = f.read().splitlines()
                    oldPassword = userConfig[1]
                with open('user-config.txt', 'w') as f:
                    f.write(f'{mail}\n'+oldPassword)
            except:
                with open('user-config.txt','w') as f:
                    f.write(f'{mail}\n')
        
        if(password):
            try:
                with open('user-config.txt','r') as f:
                    userConfig = f.read().splitlines()
                    oldMail = userConfig[0]
                with open('user-config.txt', 'w') as f:
                    f.write(f'{oldMail}\n{password}')
            except:
                with open('user-config.txt','w') as f:
                    f.write(f'\n{password}')

@click.command()
@click.option('--name', prompt="Input user name", help='Name of user that will be added to DB')
@click.option('--mail', prompt='Input user email', help='Email of user that will be added to DB')
def addUser(name,mail):
    conn = Database()
    Database.insertNewUser(conn, name, mail)
          
@click.command()
@click.option('--mail', prompt='Input user email', help='Email of user that will be deleted from DB')
def deleteUser(mail):
    conn = Database()
    Database.deleteUser(conn, mail)
                      
@click.command()
@click.option('-s','--subject', prompt='Subject')
@click.option('-m','--message', prompt='Message')
def send(subject,message):
    conn = Database()
    reciever = conn.getAllEmails()
    try:
        with open('user-config.txt','r') as f:
                    userConfig = f.read().splitlines()
                    mail = userConfig[0]
                    password = userConfig[1]
    except:
        print('Must config. To config run `python main.py changeconfig`')
        return
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = mail
    

    msg['To'] = ', '.join([str(i) for i in reciever])
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(mail, password)
        smtp_server.sendmail(mail, reciever, msg.as_string())
            
    print("Message has been sent!")


cli.add_command(changeConfig)
cli.add_command(addUser)
cli.add_command(deleteUser)
cli.add_command(send)

if __name__ == '__main__':
    cli()