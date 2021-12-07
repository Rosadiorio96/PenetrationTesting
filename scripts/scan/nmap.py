import nmap3
from configEnviroment import * 

def nmap_scan(RHOST):

    if REAL == False:
        info = conf_host[RHOST]['INFO']
    else:
        host_ip = "192.168.1.28"
        nmap = nmap3.Nmap()
        v = nmap.nmap_version_detection(host_ip)
        info_macchina_vittima = v[host_ip]
        ports = info_macchina_vittima['ports']
        infoPorts=[]
        info = {}

        if 'osmatch' in info_macchina_vittima and info_macchina_vittima['osmatch']:
            info['os']='NOTO'
        else:

            OS = nmap.nmap_os_detection(host_ip)
            if host_ip in OS:
                OS = OS[host_ip]
                if 'osmatch' in OS and OS['osmatch']:
                    for e in OS['osmatch']:
                        if 'name' in e and e['name']:
                            info['os']=e['name']
                        else:
                            info['os']='UNKNOWN'
                else:
                    info['os']='UNKNOWN'
            else:
                info['os']='UNKNOWN'
        for p in ports:
            dict_port={}
            if 'portid' in p.keys():
                dict_port['port']=p['portid']
            else:
                dict_port['port']='UNKNOWN'

            if 'service' in p.keys() and 'product' in p['service']:
                dict_port['service']=p['service']['product']
            else:
                dict_port['service']='UNKNOWN'

            if 'service' in p.keys() and 'version' in p['service'].keys():
                dict_port['version']=p['service']['version']
            else:
                dict_port['version']='UNKNOWN'

            infoPorts.append(dict_port)

        info['ports']=infoPorts
        
    return info