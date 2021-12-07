from scripts.exploit.exploits_script import *
from scripts.scan.scan_scripts import *
from scripts.scan.nmap import *

doneNmap = False
done = False

def generate_action(id):
    if id == 0:
        return Exploit(0, "IRCD", 'unknown', 1, 1)
    if id == 1:
        return Exploit(1, "php", 'unknown', 1, 1)
    if id == 2:
        return Exploit(2, "samba", 'unknown', 1, 1)
    if id == 3:
        return Exploit(3, "shellshock", 'unknown', 1, 1)
    if id == 4:
        return Exploit(4, "wordpressFileManager", 'unknown', 1, 1)
    if id == 5:
        return Exploit(5, "wordpressReflexGallery", 'unknown', 1, 1)
    if id == 6:
        return Exploit(6, "ftp", 'unknown', 1, 1)
    if id == 7:
        return scanVuln(7, "php", 'unknown', 1, 1)
    if id == 8:
        return scanVuln(8, "wordpressReflexGallery", 'unknown', 1, 1)
    if id == 9:
        return scanVuln(9, "wordpressFileManager", 'unknown', 1, 1)
    if id == 10:
        return scanVuln(10, "shellshock", 'unknown', 1, 1)
    if id == 11:
        return scanVuln(11, "scanNmap", 'unknown', 1, 1)
    if id == 12:
        return scanVuln(12, "scanSamba", 'unknown', 1, 1)
    if id == 13:
        return scanVuln(13, "scanftp", 'unknown', 1, 1)
    if id == 14:
        return scanVuln(14, "scanIRCD", 'unknown', 1, 1)
    

def load_action_list():
    action_list = []
    action_list.append(Exploit(0,"ssh", 'unknown', 1, 1))
    action_list.append(Exploit(1, "php", 'unknown', 1, 1))
    action_list.append(Exploit(2, "samba", 'unknown', 1, 1))
    action_list.append(Exploit(3, "shellshock", 'unknown', 1, 1))
    action_list.append(Exploit(4, "wordpressFileManager", 'unknown', 1, 1))
    action_list.append(Exploit(5, "wordpressReflexGallery", 'unknown', 1, 1))
    action_list.append(Exploit(6, "ftp", 'unknown', 1, 1))
    action_list.append(scanVuln(7, "php", 'unknown', 1, 1))
    action_list.append(scanVuln(8, "wordpressReflexGallery", 'unknown', 1, 1))
    action_list.append(scanVuln(9, "wordpressFileManager", 'unknown', 1, 1))
    action_list.append(scanVuln(10, "shellshock", 'unknown', 1, 1))
    action_list.append(scanVuln(11, "scanNmap", 'unknown', 1, 1))
    action_list.append(scanVuln(12, "scanSamba", 'unknown', 1, 1))
    action_list.append(scanVuln(13, "scanftp", 'unknown', 1, 1))
    action_list.append(scanVuln(14, "scanIRCD", 'unknown', 1, 1))
    return action_list

    
class Action:
    def __init__(self, id, cost, prob):
        self.id = id
        self.cost = cost
        self.prob = prob

    def is_exploit(self):
        return isinstance(self, Exploit)
    
    def is_scanVuln(self):
        return isinstance(self, scanVuln)

class Exploit(Action):
    def __init__(self, id, service, os, cost, prob):
        super().__init__(id=id,
        cost=cost,
        prob=prob)

        self.os = os
        self.service = service
    
    def executeExploit(self, host_name):
        global done

        if self.id == 0:
            print("Get brute force attack ssh")
            return IRCD_exploit(host_name)
        elif self.id == 1:
            print("Get php cgi injectio")
            return php_exploit(host_name)
        elif self.id == 2:
            print("Get samba")
            return exploit_samba(host_name)
        elif self.id == 3:
            print("Get shellshock")
            return shellshock(host_name)
        elif self.id == 4:  
            print("Get wordpress")  
            return wordpress_exploit(host_name)
            
        elif self.id == 5:
            print("Get wp reflex")
            return wp_reflex(host_name)
        elif self.id == 6:
            print("Get brute force attack ftp")
            return ftp_exploit(host_name)
        else:
            print("Error")

        

class scanVuln(Action):
    def __init__(self, id,  service, os, cost, prob):
        super().__init__(id=id,
        cost=cost,
        prob=prob)

        self.os = os
        self.service = service


    def executeScan(self, host_name):
        if self.id == 7:
            print("Scan vuln CVE-2012-1823")
            return php_scan(host_name)
        elif self.id == 8:
            print("Scan vuln Wordpress Reflex Gallery")
            return wordpress_scan_Reflex_Gallery(host_name)
        elif self.id == 9:
            print("Scan vuln Wordpress File Manager")
            done = True
            return wordpress_scan_fileManager(host_name)
        elif self.id == 10:
            print("Scan vuln shellshock")
            return shellshock_scan(host_name)
        elif self.id == 11:
            print("Scansione totale")
            return nmap_scan(host_name)
        elif self.id == 12:
            print("Samba scan")
            return samba_scan(host_name)
            input()
        elif self.id == 13:
            print("Scansione VSFTP")
            return scan_vsftp(host_name)
        elif self.id == 14:
            print("Scansione IRCD")
            return scan_IRCD(host_name)
        else:
            print("Error")

    def returnVulnerabilities(self):
        if self.id == 7:
            return "cve-2012-1823"
        elif self.id ==8:
            return "wordpress-reflex-gallery"
        elif self.id == 9:
            return "wordpress-file-manager"
        elif self.id == 10:
            return "shellshock"
        elif self.id == 12:
            return "SambaVuln"
        elif self.id == 13:
            return "vsFTPd"
        elif self.id == 14:
            return "UnrealIRCD" 
        else:
            return -1

class ActionResult:
    def __init__(self, success, action):
        self.success = success
        self.action = action
    
    def infoResult(self):
        if self.action.is_exploit()==True:
            if self.success == -1 :
                return dict(success="Fallito", serviceAttached=self.action.id)
            else:
                return dict(success="Successo", serviceAttached=self.action.id)
        elif self.action.is_scanVuln()==True:
            vuln = self.action.returnVulnerabilities()
            if self.success == -1:
                return dict(success="False", servicesVuln=vuln)
            elif self.success == 0:
                return dict(success="True", servicesVuln=vuln)