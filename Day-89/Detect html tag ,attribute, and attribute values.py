from html.parser import HTMLParser

# Custom parser
class MyHTMLParser(HTMLParser):

    # Handle start tags
    def handle_starttag(self, tag, attrs):

        # Print tag name
        print(tag)

        # Print attributes
        for name, value in attrs:
            print("->", name, ">", value)

    # Handle self-closing tags
    def handle_startendtag(self, tag, attrs):

        print(tag)

        for name, value in attrs:
            print("->", name, ">", value)


# Create parser object
parser = MyHTMLParser()

# Read number of lines
n = int(input())

# Store complete HTML
html = ""

for _ in range(n):
    html += input() + "\n"

# Parse HTML
parser.feed(html)