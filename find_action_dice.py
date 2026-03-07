with open("index.html") as f:
    text = f.read()
    start = text.find("Action Dice Pool")
    if start != -1:
        start = text.rfind("<div", 0, start)
        end = text.find("<!-- END of Action Dice Pool -->", start)
        if end == -1:
            end = text.find("</div>", start + 3000)
        print(text[start:end])
