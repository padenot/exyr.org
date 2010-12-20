from flaskext.script import Manager, Server
from . import app, builder


manager = Manager(app, with_default_commands=False)

# I prefer shorter names
manager.add_command('run', Server())

@manager.command
def build(serve=False):
    """Builds the static version of the website."""
    urls = builder.build()
    print 'Built %i files.' % len(urls)
    if serve:
        builder.serve()

@manager.shell
def shell_context():
    from . import app, pages, builder
    return locals()


if __name__ == '__main__':
    manager.run()
