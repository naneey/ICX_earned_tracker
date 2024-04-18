import csv
import time
import sys

from utils import *

result=[]


def calculate(start_block_height, end_block_height, prev_ICX=0):
    """Calculate ICX earned between start and end block heights."""
    print(f'Fetching IScore at: {start_block_height}')
    response = get_IScore(start_block_height)
    prep = get_PRep(start_block_height)
    
    bonded = int(prep['bonded'], 0) / EXA
    power = int(prep['power'], 0) / EXA
    iscore = int(response['iscore'], 0) / EXA
    ICX = iscore / ICX_MULTIPLIER
    time = get_timestamp(start_block_height)
    block_height = int(response['blockHeight'], 0)

    diff = ICX - prev_ICX if prev_ICX != 0 else 0
    if diff < 0:
        diff = ICX

    result.append([start_block_height, time, bonded, power, iscore, ICX, diff])

    prev_ICX = ICX

    prep_term = get_next_term(start_block_height)

    if prep_term < end_block_height:
        calculate(prep_term + 1, end_block_height, prev_ICX)


def save_result():
    """Save calculation result to a CSV file."""
    filename = f'{int(time.time())}_result.csv'
    print(f'Saving result in :{filename}')
    field_names = ['block height', 'timestamp', 'bond', 'power', 'iScore', 'ICX', 'earned']

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field_names)
        csvwriter.writerows(result)


if __name__ == "__main__":
    start_block_height = int(sys.argv[1])

    if len(sys.argv) > 2:
        end_block_height = int(sys.argv[2])
    else:
        end_block_height = get_current_block()

    calculate(start_block_height, end_block_height)
    save_result()
