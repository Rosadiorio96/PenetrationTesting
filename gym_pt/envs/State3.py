from scripts.scan.nmap import *
from .Action import *
import numpy as np

class StateVector:
    
    def __init__(self):
        self.vector = np.full(shape=18, fill_value=-1)


    def generate_initial_vector(self):
        self.vector = np.full(shape=18, fill_value=-1)
        
    def vectorizeOS(self, os):
        print(os['os'])
        if 'UNKNOWN' in os['os']:
            self.vector[0] = -1
            self.vector[1] = -1
        elif 'Linux' in os['os']:
            self.vector[0]=0
            self.vector[1] = 1
        else:
            self.vector[0] = 1
            self.vector[1] = 0


    def vectorizePortInfo(self, porte):
        print(porte)
        if porte['PORTE']['P6667'] == 'OPEN':
            self.vector[2] = 1
        elif porte['PORTE']['P6667'] == 'CLOSED':
            self.vector[2] = 0
        else:
            self.vector[2] = -1

        if porte['PORTE']['P80'] == 'OPEN':
            self.vector[3] = 1
        elif porte['PORTE']['P80'] == 'CLOSED':
            self.vector[3] = 0
        else:
            self.vector[3] = -1
        
        if porte['PORTE']['P21'] == 'OPEN':
            self.vector[4] = 1
        elif porte['PORTE']['P21'] == 'CLOSED':
            self.vector[4] = 0
        else:
            self.vector[4] = -1

        if porte['PORTE']['P139'] == 'OPEN':
            self.vector[5] = 1
        elif porte['PORTE']['P139'] == 'CLOSED':
            self.vector[5] = 0
        else:
            self.vector[5] = -1

    def getShape(self):
        return self.vector.shape[0]

    def vectorizeService(self, services):
        if services['SERVIZI']['IRCD']=='OPEN':
            self.vector[6] = 1
        elif services['SERVIZI']['IRCD']=='CLOSED':
            self.vector[6] = 0
        else:
            self.vector[6] = -1

        if services['SERVIZI']['ftp']=='OPEN':
            self.vector[7] = 1
        elif services['SERVIZI']['ftp']=='CLOSED':
            self.vector[7] = 0
        else:
            self.vector[7] = -1

        if services['SERVIZI']['samba']=='OPEN':
            self.vector[8] = 1
        elif services['SERVIZI']['samba']=='CLOSED':
            self.vector[8] = 0
        else:
            self.vector[8] = -1

        if services['SERVIZI']['apache_httpd']=='OPEN':
            self.vector[9] = 1
        elif services['SERVIZI']['apache_httpd']=='CLOSED':
            self.vector[9] = 0
        else:
            self.vector[9] = -1

    def vectorizevuln(self, vuln, result):
        if vuln == "cve-2012-1823":
            self.vector[10] = int(result=='True')
        elif vuln ==  "wordpress-reflex-gallery":
            self.vector[11] = int(result=='True')
        elif vuln == "wordpress-file-manager":
            self.vector[12] = int(result=='True')
        elif vuln == "shellshock":
            self.vector[13] = int(result=='True')
        elif vuln == "UnrealIRCD":
            self.vector[14] = int(result=='True')
        elif vuln == "vsFTPd":
            self.vector[15] = int(result=='True')
        elif vuln == "SambaVuln":
            self.vector[16] = int(result=='True')  
        

    def vectorizeCompromised(self, val):
        if val == True:
            self.vector[17]=1
        else:
            self.vector[17]=0