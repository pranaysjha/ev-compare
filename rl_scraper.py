from requests_html import HTMLSession

def rl_symbols(symbol: str) -> list:
    url = 'https://finance.yahoo.com/quote/' + symbol + '/company-insights?p=' + symbol
    session = HTMLSession()
    r = session.get(url)
    print(r)

    symbols = []
    insights = r.html.find("#Lead-5-CompanyInsights-Proxy", first=True)
    insights_elems = insights.find('a')
    for elem in insights_elems:
        class_content = list(elem.attrs.get('class'))
        if class_content.count('rl-card') > 0:
            symbol = elem.attrs.get('title')
            symbols.append(symbol)

    [print(symbol) for symbol in symbols]
    return symbols