from rejson import Client, Path

def main():
    rj = Client(host='localhost', port=6379, decode_responses=True)
    

if __name__ == '__main__':    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()