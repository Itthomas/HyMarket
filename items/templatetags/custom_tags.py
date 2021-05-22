#from _typeshed import OpenBinaryModeUpdating
from django import template
import time

register = template.Library()

def get_name(var):
    name = var['quick_status']['productId']
    temp = name.replace('_', ' ')
    fixed = temp.title()
    if fixed == 'Log':
        fixed = 'Oak Log'
    elif fixed == 'Log:1':
        fixed = 'Spruce Log'
    elif fixed == 'Log:2':
        fixed = 'Birch Log'
    elif fixed == 'Log 2:1':
        fixed = 'Dark Oak Log'
    elif fixed == 'Log 2':
        fixed = 'Acacia Log'
    elif fixed == 'Log:3':
        fixed = 'Jungle Log'
    elif fixed == 'Sulphur':
        fixed = 'Gunpowder'
    elif fixed == 'Ink Sack:4':
        fixed = 'Lapis Lazuli'
    elif fixed == 'Ink Sack:3':
        fixed = 'Cocoa Beans'
    elif fixed == 'Huge Mushroom 2':
        fixed = 'Red Mushroom Block'
    elif fixed == 'Huge Mushroom 1':
        fixed = 'Brown Mushroom Block'

    #Oak Wood: "LOG"
    #Spruce Wood: "LOG:1"
    #Birch Wood: "LOG:2"
    #Dark Oak Wood: "LOG_2:1"
    #Acacia Wood: "LOG_2"
    #Jungle Wood: "LOG:3"
    #Gunpowder: "SULPHUR"
    #Lapis Lazuli: "INK_SACK:4"
    #Cocoa Beans: "INK_SACK:3"
    #Red Mushroom Block: "HUGE_MUSHROOM_2"
    #Brown Mushroom Block: "HUGE_MUSHROOM_1"

    return fixed

def get_buy_price(value):
    price = value['quick_status']['buyPrice']
    return round(price, 1)

def get_buy_amount(value):
    amount = value['quick_status']['buyOrders']
    return amount

def get_buy_volume(value):
    volume = value['quick_status']['buyVolume']
    return volume

def get_sell_price(value):
    price = value['quick_status']['sellPrice']
    return round(price, 1)

def get_sell_amount(value):
    amount = value['quick_status']['sellOrders']
    return amount

def get_sell_volume(value):
    volume = value['quick_status']['sellVolume']
    return volume

def get_auction_item(value):
    item = value['item_name']
    return item

def get_highest_bid(value):
    bid = value['highest_bid_amount']
    return bid

def get_baazar_link(value):
    item_id = value['quick_status']['productId']
    url = f'http://127.0.0.1:8000/baazar/details/{item_id}'
    return url

def make_pretty(value):
    pretty = value.title().replace('_', ' ')
    return pretty

def get_summary_price(value):
    price = value['pricePerUnit']
    return price

def get_summary_amount(value):
    amount = value['amount']
    return amount

def get_summary_orders(value):
    orders = value['orders']
    return orders

def get_auction_end(value):
    milliseconds = value['end'] - time.time() * 1000
    minutes = round(milliseconds/60000, 0)
    hours = int(minutes / 60 - (minutes % 60) / 60)
    minutes -= hours * 60
    time_string = f'{hours}h {int(minutes)}m'
    return time_string

def get_bids(value):
    bids = len(value['bids'])

def get_tier(value):
    tier = value['tier'].title()
    return tier

def get_starting_bid(value):
    starting_bid = value['starting_bid']
    return starting_bid

register.filter('get_name', get_name)
register.filter('get_buy_price', get_buy_price)
register.filter('get_buy_amount', get_buy_amount)
register.filter('get_buy_volume', get_buy_volume)
register.filter('get_sell_price', get_sell_price)
register.filter('get_sell_amount', get_sell_amount)
register.filter('get_sell_volume', get_sell_volume)
register.filter('get_auction_item', get_auction_item)
register.filter('get_highest_bid', get_highest_bid)
register.filter('get_baazar_link', get_baazar_link)
register.filter('make_pretty', make_pretty)
register.filter('get_summary_price', get_summary_price)
register.filter('get_summary_amount', get_summary_amount)
register.filter('get_summary_orders', get_summary_orders)
register.filter('get_auction_end', get_auction_end)
register.filter('get_bids', get_bids)
register.filter('get_tier', get_tier)
register.filter('get_starting_bid', get_starting_bid)