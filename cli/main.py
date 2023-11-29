#from database.config import Database as db
import click

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
                
                

cli.add_command(changeConfig)

if __name__ == '__main__':
    cli()