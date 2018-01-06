import requests
from getpass import getpass
from BeautifulSoup import BeautifulSoup

def printStatus(res):
	if res.ok:
		print "OK " + str(res.status_code)
	else:
		print "ERROR " + str(res.status_code)

credentials = {
	"userid": '',
	"pwd": '',
	"timezoneOffset": -480
}

credentials['userid'] = raw_input("Username: ")
credentials['pwd'] = getpass("Password: ")

session_req = requests.session()
login_url = "https://sais.up.edu.ph/psp/ps/?cmd=login&languageCd=ENG"

# Login
print "Logging in"
res = session_req.post(
	login_url,
	data = credentials,
	headers = dict(referer = login_url)
)
printStatus(res)

# Connect to course title page
print "Opening course title pages"
url = "https://sais.up.edu.ph/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_BROWSE_CATLG_P.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_SS_CATALOG.HC_SSS_BROWSE_CATLG_P_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder&PortalActualURL=https%3a%2f%2fsais.up.edu.ph%2fpsc%2fps%2fEMPLOYEE%2fHRMS%2fc%2fSA_LEARNER_SERVICES.SSS_BROWSE_CATLG_P.GBL&PortalContentURL=https%3a%2f%2fsais.up.edu.ph%2fpsc%2fps%2fEMPLOYEE%2fHRMS%2fc%2fSA_LEARNER_SERVICES.SSS_BROWSE_CATLG_P.GBL&PortalContentProvider=HRMS&PortalCRefLabel=Browse%20Course%20Catalog&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fsais.up.edu.ph%2fpsp%2fps%2f&PortalURI=https%3a%2f%2fsais.up.edu.ph%2fpsc%2fps%2f&PortalHostNode=HRMS&NoCrumbs=yes&PortalKeyStruct=yes"

res = session_req.get(
	url,
	headers = dict(referer = url)
)
printStatus(res)

# Getting course titles
soup = BeautifulSoup(res.content)
table = soup.findAll('span', attrs = {'class': 'SSSHYPERLINKBOLD'})

for i in range(0, len(table)):
	table[i] = table[i].text.split(' - ')

print table
