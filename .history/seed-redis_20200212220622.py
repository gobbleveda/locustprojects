"""
Install the following requirements into your virtual environemnt 
`pip install click redis`
Usage:
To load data into redis
python redis_dump.py load [filepath]
To dump data into redis
python redis_dump.py dump [filepath] --search '*txt'
"""

from rejson import Client, Path
import logging

def main(action, filepath, search):
    rj = Client(host='localhost', port=6379, decode_responses=True)  # update your redis settings

    if action == 'dump':
        out = {}
        for key in r.scan_iter(search):
            out.update({key: r.get(key)})
        if len(out) > 0:
            try:
                with open(filepath, 'w') as outfile:
                    json.dump(out, outfile)
                    print('Dump Successful')
            except Exception as e:
                print(e)
        else:
            print("Keys not found")

    elif action == 'load':
        try:
            print('here......')
            usr = r.json.get('user');
            print(usr)
           
        except Exception as e:
            print('here is the error: ' + str(e))


if __name__ == '__main__':    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()