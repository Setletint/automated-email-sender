#from database.config import Database as db
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--mail')
@click.option('--password')
def changeConfig(mail,password):
        
        if(mail):
            try:
                with open('user-config.txt','r') as f:
                    userConfig = f.read().splitlines()
                    oldPass = userConfig[1]
                with open('user-config.txt', 'w') as f:
                    f.write(f'{mail}\n'+oldPass)
            except:
                with open('user-config.txt','w') as f:
                    f.write(f'{mail}\n')
                

cli.add_command(changeConfig)

if __name__ == '__main__':
    cli()