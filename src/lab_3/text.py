def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    symbols = []
    for sym in text:
        if sym.isprintable() or sym == ' ':
            symbols.append(sym)
        else:
            sym = ' '
            symbols.append(sym)
    text = ''.join(symbols)
    text = text.strip()
    text = ' '.join(text.split())
    return text
print(normalize("ПрИвЕт\nМИр\t"))