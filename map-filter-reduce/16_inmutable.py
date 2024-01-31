items = [
    {
        "product" : "camisa",
        "price"   : 100
    },
    {
        "product" : "pantalones",
        "price"   : 300
    },
    {
        "product" : "pantalones 2",
        "price"   : 200
    }
]

prices = list(map(lambda item: item["price"], items))
print(prices)

def add_taxes(item):
    item = item.copy()
    item["taxes"] = item["price"] * .19
    item["total"] = item["price"] + item["taxes"]
    return item


print(items)
list(map(add_taxes, items))
print(items)



