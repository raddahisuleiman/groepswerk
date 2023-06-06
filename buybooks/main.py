import sys
sys.dont_write_bytecode = True
import os
from create import create_app

_basedir = os.path.abspath(os.path.dirname(__file__))


app = create_app()


if __name__ == "__main__":
    app.run()
    
    