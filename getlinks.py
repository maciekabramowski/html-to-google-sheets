from html.parser import HTMLParser
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials-hemp.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Hemplinks').sheet1

index = 1

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs): 
        global index
        global sheet
        #ha = open("hemplinks.txt", "a")       
        if tag == 'a':            
            for name, value in attrs:
                if name == "href":
                    #print (name, "=", value)
                    #ha.write(str(value) + "\r\n")
                    row = [str(value), name]
                    sheet.insert_row(row, index)
                    index = index + 1


def main():
    parser = MyHTMLParser()
    f = open("hemplinks.html", encoding="utf8")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)    

if __name__ == "__main__":
    main()