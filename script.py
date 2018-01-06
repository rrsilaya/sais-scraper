import requests, constants, utils, spinner, time
from bs4 import BeautifulSoup
from getpass import getpass

# Constants
spinner = spinner.Spinner();
url = constants.Url();
session_req = requests.session();

credentials = {
  'userid': '',
  'pwd': '',
  'request_id': '1103954795815962967'
}

# Login
credentials['userid'] = input("Email: ");
credentials['pwd'] = getpass("Password: ");

spinner.start('Logging in');
res = session_req.post(
  url.LOGIN,
  data = credentials,
  headers = dict(referer = url.LOGIN)
);
spinner.stop();
utils.printStatus(res);