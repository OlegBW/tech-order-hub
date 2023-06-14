from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import click
'''

Implements the database management functionality, creates a session with the database 


Functions:

init_db()
shutdown_session()
cli_init_db()
init_app() 

'''

print('Import database')

engine = create_engine('sqlite:////tmp/hub.db',echo=True)

db_session = scoped_session(
    sessionmaker(autocommit=False,
                autoflush=False,
                bind=engine)
    )

Base = declarative_base()
Base.query = db_session.query_property()

def init_db(add_fixtures = False):
    'initializes the database using the imported models'

    from . import models
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    if add_fixtures:
        from . import fixtures
        db_session.add_all(fixtures.create_products_fixtures())
        db_session.commit()

def shutdown_session(exception=None):
    'Disconnects a session from the database'

    db_session.remove()

@click.command('init-db')
@click.option('--add-fixtures', is_flag = True, help='Loads the initial data')
def cli_init_db(add_fixtures):
    'Initializes the database when using the init-db console command'

    init_db(add_fixtures)
    click.echo(click.style('Initialized the database', fg='green'))
    if add_fixtures:
        click.echo(click.style('Added fixtures', fg='green'))

def init_app(app):
    'Sets the database session to be broken when the application context is destroyed, adds the init-db console command to the application'

    app.teardown_appcontext(shutdown_session)
    app.cli.add_command(cli_init_db)