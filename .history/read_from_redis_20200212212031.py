from rejson import Client, Path

def main():
    rj = Client(host='localhost', port=6379, decode_responses=True)
    obj = {
       'answer': 42,
       'arr': [None, True, 3.14],
       'truth': {
           'coord': 'out there'
       }
    }
    
    rj.jsonset('obj', Path.rootPath(), obj)

   # Get something
    print 'Is there anybody... {}?'.format(
       rj.jsonget('obj', Path('.truth.coord'))
    )

if __name__ == '__main__':    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()