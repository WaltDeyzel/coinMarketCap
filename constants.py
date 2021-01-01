class Constants:
    table = "cmc-table-row"
    
    number = "cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank"
    link = "cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"
    tag = "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol"
    price = "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"
    marketcap = "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap"
    change1h = "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h"
    change24h = "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h"
    change7d = "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d"

    fmt = '{:<2} {:<3} {:<22} {:<13} {:<10} {:<17} {:<13} {:<7} {:<7}'
    currency = 'R '
    stripes = '-------------------------------------------------------------------------------------------------------'
    heading = fmt.format(' ','NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'VOLUME', 'V/MC', 'SUPPLY')
    numberOfElements = 20