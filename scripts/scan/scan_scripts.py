from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
from configEnviroment import *
import json
import re
import subprocess 
from packaging.version import parse

""""
Wordpress_scan is a function that return:
-1 if it is not vulnerable
0 if the host is file manager vulnerable
1 if the host is wp-reflex vulnerabile
"""

def wordpress_scan_fileManager(host_name):
    if REAL == False:
        return conf_host[host_name]['VULN']['Wordpress-FileManager']
    else:
        RHOST = conf_host[host_name]['IP']
        find = False
        try:
            webpage = urlopen("http://"+ RHOST + "/wordpress")
            find = True
        except Exception as e:
            print("")


        if find==False:
            try:
                webpage = urlopen("http://"+ RHOST + "/blog")
            except Exception as e:
                #print("Error")
                return -1

        soup = BeautifulSoup(webpage, "lxml")

        val = soup.find('meta', attrs={'name':'generator'})
        if "WordPress" in val['content']:
            versionW = val['content'].split(" ")[1]
            versionW = versionW.split(".")
        else:
            return -1

        if find == True:    
            batcmd = "wpscan --url http://"+ RHOST + "/wordpress --plugins-detection aggressive"
        else:
            batcmd = "wpscan --url http://"+ RHOST + "/blog --plugins-detection aggressive"
        result = subprocess.check_output(batcmd, shell=True)
        result2 = result.decode("utf-8")
        plugins = result2.split("Checking Plugin Versions (via Passive and Aggressive Methods)")
        p = plugins[1]
        fileManager = p.split(" wp-file-manager")
        if len(fileManager)>1:
            versionF = fileManager[1].split('Version: ')
            versionNumber = versionF[1].split(' ')
            #print(versionNumber[0])
            v = versionNumber[0]
            if parse(v) < parse('6.8.0') and parse(v) >= parse('6.0.0'):
                #print("It is wp-file-manager vulnerable")
                return 0
            else:
                return -1

        return -1


def wordpress_scan_Reflex_Gallery(host_name):
    if REAL == False:
        return conf_host[host_name]['VULN']['Wordpress-Reflex']
    else:
        RHOST = conf_host[host_name]['IP']
        find = False
        try:
            webpage = urlopen("http://"+ RHOST + "/wordpress")
            find = True
        except Exception as e:
            print("")

        if find==False:
            try:
                webpage = urlopen("http://"+ RHOST + "/blog")
            except Exception as e:
                #print("Error")
                return -1

        soup = BeautifulSoup(webpage, "lxml")

        val = soup.find('meta', attrs={'name':'generator'})
        if "WordPress" in val['content']:
            versionW = val['content'].split(" ")[1]
            versionW = versionW.split(".")
        else:
            return -1

        if find == True:    
            batcmd = "wpscan --url http://"+ RHOST + "/wordpress --plugins-detection aggressive"
        else:
            batcmd = "wpscan --url http://"+ RHOST + "/blog --plugins-detection aggressive"
        result = subprocess.check_output(batcmd, shell=True)
        result2 = result.decode("utf-8")
        plugins = result2.split("Checking Plugin Versions (via Passive and Aggressive Methods)")
        p = plugins[1]
        wp_reflex =  p.split(" reflex-gallery")
        if len(wp_reflex)>1:
            version = wp_reflex[1].split('Version: ')
            versionNumber = version[1].split(' ')
            if versionNumber[0]=='3.1.3':
                #print("It is WP reflex vulnerable")
                return 0
        return -1
    
    
    
def shellshock_scan(host_name):
    if REAL == False:
        return conf_host[host_name]['VULN']['Shellshock']
    else:
        RHOST = conf_host[host_name]['IP']
        try:
            webpage = urlopen("http://"+ RHOST)
        except Exception as e:
            return -1

        soup = BeautifulSoup(webpage, "lxml")
        val = soup.findAll('script', text=re.compile("/cgi-bin"))
        if len(val)==0:
            #print("Not vulnerable")
            return -1
        else:
            #print("It is vulnerable")
            return 0


def php_scan(host_name):
    if REAL == False:
        return conf_host[host_name]['VULN']['Cve-2012-1823']
    else:
        RHOST = conf_host[host_name]['IP']
        try:
            batcmd = "curl -I http://"+ RHOST +"/index.php"
            result = subprocess.check_output(batcmd, shell=True).decode("utf-8")
        except subprocess.CalledProcessError as e:
            #print(e.output)
            return -1
        v = result.split("X-Powered-By: PHP/")
        if len(v) == 1 :
            #print("It is not php-cgi vulnerable")
            return -1
        version = v[1].split("-")
        if parse(version[0]) < parse("5.3.12") or parse(version[0]) == parse("5.4.1") or parse(version[0]) == parse("5.4.0"):
            #print("It is php-cgi vulnerable")
            return 0


def samba_scan(host_name):
    if REAL == False:
        return conf_host[host_name]['VULN']['SambaVuln']
    else:
        pass


def scan_IRCD(host_name):
    if REAL == False:
        return conf_host[host_name]['VULN']['UnrealIRCD']
    else:
        pass

def scan_vsftp(host_name):
    if REAL == False:
        return conf_host[host_name]['VULN']['vsFTPd']
    else:
        pass