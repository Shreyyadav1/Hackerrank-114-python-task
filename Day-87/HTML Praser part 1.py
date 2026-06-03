from html.parser import HTMLParser

# Create custom parser
class MyHTMLParser(HTMLParser):

    # Start tag
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)

        for name, value in attrs:
            print("->", name, ">", value)

    # End tag
    def handle_endtag(self, tag):
        print("End   :", tag)

    # Empty tag
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)

        for name, value in attrs:
            print("->", name, ">", value)


# Create parser object
parser = MyHTMLParser()

# Read number of lines
n = int(input())

# Feed HTML code line by line
for _ in range(n):
    parser.feed(input())