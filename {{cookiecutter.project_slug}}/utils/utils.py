import getopt


def usage():
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print('Usage: python use_agents.py -h --help: Prints this help message')

    '''
    Add help messages for more options here
    '''

    return

def process_args(args):
    try:
        opts, args = getopt.getopt(args, "hp:",
                                   [
                                       "help",
                                       "port"
                                   ])
    except getopt.GetoptError as err:
        print("Error: " + str(err))
        usage()
        exit(-1)

    '''
    All options to process must be added here
    only in alphabetical order, refer to elif
    '''
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            exit(-2)
        elif o in ("-p", "--port"):
            port = a
        else:
            assert False, "Invalid option: " + o + "provided!"

    ## Return whatever is used
    ## by functions in main()
    ## Else just return empty
    return port