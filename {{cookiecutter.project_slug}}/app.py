# Standard module imports
import sys
from waitress import serve

# Project module imports
from utils.utils import process_args
from config.config import app


def main(argumentList):
    port = process_args(args=argumentList)
    
    serve(app=app, port=port)

    return

if __name__ == '__main__':
    main(argumentList=sys.argv[1:])