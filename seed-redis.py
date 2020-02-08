"""
Install the following requirements into your virtual environemnt 
`pip install click redis`
Usage:
To load data into redis
python redis_dump.py load [filepath]
To dump data into redis
python redis_dump.py dump [filepath] --search '*txt'
"""

import click
import redis
import json
import logging
import os


@click.command()
@click.argument('action')
@click.argument('filepath')
@click.option('--search', help="Key search patter. eg `*txt`")
def main(action, filepath, search):
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)  # update your redis settings
    cache_timeout = None
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
            with open(filepath) as f:
                data = json.load(f)
                for key in data:
                    r.set(key, data.get(key), cache_timeout)
                print('Data loaded into redis successfully')
        except Exception as e:
            print(e)


if __name__ == '__main__':    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()