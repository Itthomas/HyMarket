from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'home.html', context)

def baazar(request, search=None):
    data = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
    products = []
    for item in data['products'].values():
        if search == None:
            products.append(item)
        elif search.lower() in item['product_id'].lower():
            products.append(item)
    products.sort(key=item_sort)
    context = {
        'api': products
    }
    return render(request, 'baazar.html', context)

def item_sort(item):
    name = item['product_id']
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
    return fixed

def baazar_item(request, item_id=None):
    data = requests.get('https://api.hypixel.net/skyblock/bazaar').json()
    context = {
        'api': data['products'],
        'item': item_id,
        'sell_summary': data['products'][item_id]['sell_summary'],
        'buy_summary': data['products'][item_id]['buy_summary'],
        'quick_status': data['products'][item_id]['quick_status'],
        'sell_price': round(data['products'][item_id]['quick_status']['sellPrice'], 1),
        'sell_volume': data['products'][item_id]['quick_status']['sellVolume'],
        'sell_orders': data['products'][item_id]['quick_status']['sellOrders'],
        'buy_price': round(data['products'][item_id]['quick_status']['buyPrice'], 1),
        'buy_volume': data['products'][item_id]['quick_status']['buyVolume'],
        'buy_orders': data['products'][item_id]['quick_status']['buyOrders'],
    }
    return render(request, 'baazar_item.html', context)

def auction(request, search=None):
    r = requests.get('https://api.hypixel.net/skyblock/auctions').json()
    data = r['auctions']
    auctions = []
    for auction in data:
        if search == None:
            auctions.append(auction)
        elif search.lower() in auction['item_name'].lower():
            auctions.append(auction)
    auctions.sort(key=name_sort)
    context = {
        'api': auctions,
        'results': len(auctions)
    }
    return render(request, 'auction.html', context)

def name_sort(auction):
    return auction['item_name']