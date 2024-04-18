from pprint import pprint
import json
import datetime
import time
from iconsdk.builder.call_builder import CallBuilder

from const import *


def int_to_hex(int_val):
    return hex(int_val)

def call_tx(contract,method,params):
    call = CallBuilder()\
        .from_('hx0000000000000000000000000000000000000000')\
        .to(contracts[contract])\
        .method(method)\
        .params(params)\
        .build()
    response = icon_service.call(call)
    return response

def call_tx_with_height(contract,method,params,height):
    hex_height =  int_to_hex(height)
    call = CallBuilder()\
        .from_('hx0000000000000000000000000000000000000000')\
        .to(contracts[contract])\
        .method(method)\
        .params(params)\
        .height(hex_height)\
        .build()
    response = icon_service.call(call)
    return response

def get_current_block():
    """Get the current block height."""
    response = call_tx('system', 'getIISSInfo', {})
    return int(response.get('blockHeight'), 16)


def get_next_term(height):
    """Get the block height of the next IISS calculation."""
    response = call_tx_with_height('system', 'getIISSInfo', {}, height)
    return int(response.get('nextCalculation'), 16)


def get_IScore(height):
    """Get the IScore at the given block height."""
    params = {'address': 'hx231a795d1c719b9edf35c46b9daa4e0b5a1e83aa'}
    result = call_tx_with_height('system', 'queryIScore', params, height)
    return result


def get_PRep(height):
    """Get the P-Rep information at the given block height."""
    params = {'address': 'hx231a795d1c719b9edf35c46b9daa4e0b5a1e83aa'}
    result = call_tx_with_height('system', 'getPRep', params, height)
    return result


def get_block(block_no):
    """Get the block information for the given block number."""
    return icon_service.get_block(block_no)


def get_timestamp(block_no):
    """Convert block timestamp to human-readable format."""
    unix_timestamp = get_block(block_no)['time_stamp'] / 1000000
    human_date = datetime.datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return human_date
