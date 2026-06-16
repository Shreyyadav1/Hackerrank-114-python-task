from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, t, a):
        print(t)
        for x, y in a:
            print("->", x, ">", y)

    def handle_startendtag(self, t, a):
        print(t)
        for x, y in a:
            print("->", x, ">", y)

p = MyHTMLParser()
p.feed("\n".join(input() for _ in range(int(input()))))