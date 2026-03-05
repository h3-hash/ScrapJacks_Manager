with open("index.html") as f:
    text = f.read()
    import re
    # Let's search for newConfig.suits inside setCrew block of applyShipChange
    start = text.find("const applyShipChange")
    end = text.find("};", start + 2000)
    print(text[start:end])
