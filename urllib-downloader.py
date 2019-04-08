import urllib.request
print ("REMEMBER you only can download ONE file with this program.")
print ("This means that you should change the name of the downloaded file every time you download sth")
url = input("enter the url of the file: ")
path = ("D:\download.CHANGE")
print ("your download is beginning...")
urllib.request.urlretrieve(url, path)
print ("Done :)")