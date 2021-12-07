from scripts.scan.nmap import *
from .Action import *
from .State3 import *

class State:
    os = {}
    os['OS'] = {}

    ports = {}
    ports['PORTE']={}

    services = {}
    services['SERVIZI']={}

    vulnerabilities = {}
    vulnerabilities['VULNERABILITA']={}

    vectorState = StateVector()
   

    def generete_initial_state(self):
        
        self.os['OS']= 'UNKNOWN'

        self.ports['PORTE']['P80']='UNKNOWN'
        self.ports['PORTE']['P6667']='UNKNOWN'
        self.ports['PORTE']['P21']='UNKNOWN'
        self.ports['PORTE']['P139']='UNKNOWN'

        self.services['SERVIZI']['IRCD']='UNKNOWN'
        self.services['SERVIZI']['ftp']='UNKNOWN'
        self.services['SERVIZI']['samba']='UNKNOWN'
        self.services['SERVIZI']['apache_httpd']='UNKNOWN'
       
        self.vulnerabilities['VULNERABILITA']['cve-2012-1823'] = 'UNKNOWN'
        self.vulnerabilities['VULNERABILITA']['wordpress-reflex-gallery'] = 'UNKNOWN'
        self.vulnerabilities['VULNERABILITA']['shellshock'] = 'UNKNOWN'
        self.vulnerabilities['VULNERABILITA']['wordpress-file-manager'] = 'UNKNOWN'
        self.vulnerabilities['VULNERABILITA']['IRCD'] = 'UNKNOWN'
        self.vulnerabilities['VULNERABILITA']['SAMBA'] = 'UNKNOWN'
        self.vulnerabilities['VULNERABILITA']['FTP'] = 'UNKNOWN'

        self.compromised = False

    def __init__(self):
        self.generete_initial_state()

    def config_os(self, info_host=None):
        if info_host !=None:
            self.os['os'] = info_host['os']
        else:
            self.os['os'] = 'UNKNOWN'
        self.vectorState.vectorizeOS(self.os)

    def get_os(self):
        return self.os
    

    def config_ports(self, infos=None):
        if infos != None:
            for port in infos['ports']:
                if '6667' in port['port']:
                    self.ports['PORTE']['P6667']='OPEN'
                elif '80' in port['port']:
                    self.ports['PORTE']['P80']='OPEN'
                elif '21' in port['port']:
                    self.ports['PORTE']['P21']='OPEN'
                elif '139' in port['port']:
                    self.ports['PORTE']['P139']='OPEN'

            if self.ports['PORTE']['P6667'] !='OPEN':
                self.ports['PORTE']['P6667']='CLOSED'

            if self.ports['PORTE']['P80'] !='OPEN':
                self.ports['PORTE']['P80']='CLOSED'

            if self.ports['PORTE']['P139'] !='OPEN':
                self.ports['PORTE']['P139']='CLOSED'

            if self.ports['PORTE']['P21'] !='OPEN':
                self.ports['PORTE']['P21']='CLOSED'
        
        else:
            self.ports['PORTE']['P6667']='UKNOWN'
            self.ports['PORTE']['P80']='UKNOWN'
            self.ports['PORTE']['P21']='UKNOWN'
            self.ports['PORTE']['P139']='UKNOWN'
        self.vectorState.vectorizePortInfo(self.ports)
        
    def get_ports(self):
        return self.ports

    def config_services(self, infos=None):
        if infos != None:
            for port in infos['ports']:
                if '6667' in port['port'] and 'UnrealIRCD' in port['service']:
                    self.services['SERVIZI']['IRCD']='OPEN'
                elif '21' in port['port'] and 'ftp' in port['service']:
                    self.services['SERVIZI']['ftp']='OPEN'  
                elif '139' in port['port'] and 'Microsoft Windows netbios-ssn' in port['service']:
                    self.services['SERVIZI']['samba']='OPEN'
                elif '80' in port['port'] and 'Apache' in port['service']:
                    self.services['SERVIZI']['apache_httpd']='OPEN'
            
            if self.services['SERVIZI']['IRCD'] !='OPEN':
                self.services['SERVIZI']['IRCD']='CLOSED'

            if  self.services['SERVIZI']['ftp'] !='OPEN':
                self.services['SERVIZI']['ftp']='CLOSED'

            if  self.services['SERVIZI']['samba'] !='OPEN':
                self.services['SERVIZI']['samba']='CLOSED'

            if self.services['SERVIZI']['apache_httpd'] !='OPEN':
                self.services['SERVIZI']['apache_httpd']='CLOSED'
            
        else:
            self.services['SERVIZI']['IRCD']='UNKNOWN'
            self.services['SERVIZI']['ftp']='UNKNOWN' 
            self.services['SERVIZI']['samba']='UNKNOWN'
            self.services['SERVIZI']['apache_httpd']='UNKNOWN'
        self.vectorState.vectorizeService(self.services) 
    
    def config_vulnerabilities(self, actionResult):
        vuln = actionResult.infoResult()['servicesVuln']
        result = actionResult.infoResult()['success']
        self.vulnerabilities['VULNERABILITA'][vuln] = result
        self.vectorState.vectorizevuln(vuln, result) 


    def get_vulnerabilities(self):
        return self.vulnerabilities

    def get_services(self):
        return self.services

    def set_initial_state(self, RHOST_IP):
        """info_host = nmap_scan(RHOST_IP)
        self.config_ports(info_host)
        self.config_services(info_host)
        self.config_os(info_host)"""
        
        self.config_ports()
        self.config_services()
        self.config_os()

    def get_state(self, action, action_result):
        if action.is_exploit()==True:
            print("Exploit")
        elif action.is_scanVuln()==True:
            print("Is Scan action")

    def set_compromised(self, value):
        if value == 0:
            self.compromised = True
            self.vectorState.vectorizeCompromised(True)
        elif value == -1:
            self.compromised = False
            self.vectorState.vectorizeCompromised(False)
        else:
            pass
    
    def get_compromised(self):
        return self.compromised
