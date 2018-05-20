def currency_dict(row):
    max_supply = row.max_supply

    if row.max_supply is not None:
        max_supply = row.max_supply + "BTC"



    return{
        'rank':row.rank,
        'name':row.name,
        'market_cap':row.market_cap,
        'price':row.price,
        'volume_24':row.volume_24,
        'circulatory_supply':row.circulatory_supply,
        'change':row.change,
        'symbol':row.symbol,
        'max_supply':max_supply


    }