import nyckel


credentials = nyckel.Credentials("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")
nyckel.invoke("hair-types-identifier", "your_image_url", credentials)
                