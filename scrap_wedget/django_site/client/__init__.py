def table_dict(row):


    return{
        'rank':row.rank,
        'name':row.name,
        'market_cap':row.market_cap,
        'price':row.price,
        'volume_24':row.volume_24,
        'circulatory_supply':row.circulatory_supply.replace('&nbsp',' '),
        'change':row.change.replace('&nbsp',' ')


    }