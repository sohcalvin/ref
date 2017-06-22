

def
from ftplib import FTP
ftp = FTP('lssinh009.sin.sap.corp')     # connect to host, default port
ftp.login(user='', passwd='')                     # user anonymous, passwd anonymous@

# >>> ftp.cwd('debian')               # change into "debian" directory
ftp.retrlines('LIST')           # list directory contents


# >>> ftp.retrbinary('RETR README', open('README', 'wb').write)
# '226 Transfer complete.'
# >>> ftp.quit()
