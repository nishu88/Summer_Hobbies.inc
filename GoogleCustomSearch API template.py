#Python VERSION:::: 3.6

#Author

#From Github account : nishu88

#REFER ------  https://www.youtube.com/watch?v=NIfULfx4U88   -------

#install package for importing googleapiclient.discovery:::::: "google-api-python-client"

#Command on CMD =  "pip install --upgrade google-api-python-client"



import pprint

from googleapiclient.discovery import build


def main():
  
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  
  service = build("customsearch", "v1",
            developerKey="<Get your developer key from the website>")  #AIzaSyAWB6m_mp5nAyf1xRDH_qjgfFdv4kyzIDI

  res = service.cse().list(
      q='<Enter a Search Query here>', # Ex - who is the president of india
      cx='<Enter your own cx code here >',  # 014784489822264092926:0vfp8_3s7f0   
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()
