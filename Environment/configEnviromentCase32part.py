#CASO 2
PWD = 'zOI9TD7O'
LHOST = "192.168.1.18"
REAL = False
IP={}

conf_host = {
    'RHOST0': {
        'IP': "192.168.1.9" ,
        'INFO': {
            'os': 'UNKNOWN',
            'ports': [{
                    'port': '22',
                    'service': 'OpenSSH',
                    'version': '7.9p1 Debian 10+deb10u2'
                    }, 
                    {'port': '80',
                    'service': 'Apache httpd',
                    'version': '2.4.38'
                    }]},
        'VULN':{
            'Cve-2012-1823': -1,
            'Wordpress-Reflex': -1,
            'Wordpress-FileManager': 0,
            'Shellshock': -1
        },
        'Exploit':{
            'Exploit-ssh': -1,
            'Exploit-cve': -1,
            'Exploit-samba':-1,
            'Exploit-shellshock':-1,
            'Exploit-fileManager': 0,
            'Exploit-reflexGallery':-1,
            'Exploit-ftp':-1
        }
    },
    'RHOST1': {
        'IP': "192.168.1.53" ,
        'INFO':{
            'os': 'UNKNOWN', 
            'ports': [{
                'port': '22', 
                'service': 'OpenSSH', 
                'version': '6.0'
                }, 
                {'port': '80', 
                'service': 'Apache httpd', 
                'version': '2.2.21'
                }]},
        'VULN':{
            'Cve-2012-1823': -1,
            'Wordpress-Reflex': -1,
            'Wordpress-FileManager': -1,
            'Shellshock': 0
        },
        'Exploit':{
            'Exploit-ssh': -1,
            'Exploit-cve': -1,
            'Exploit-samba':-1,
            'Exploit-shellshock': 0,
            'Exploit-fileManager': -1,
            'Exploit-reflexGallery':-1,
            'Exploit-ftp':-1
        }
    },
    'RHOST2': {
        'IP': "192.168.1.16" ,
        'INFO':{
            'os': 'UNKNOWN', 
            'ports': [ 
                {'port': '80', 
                'service': 'Apache httpd', 
                'version': '2.4.29'
                }]},
        'VULN':{
            'Cve-2012-1823': -1,
            'Wordpress-Reflex': 0,
            'Wordpress-FileManager': -1,
            'Shellshock': -1
        },
        'Exploit':{
            'Exploit-ssh': -1,
            'Exploit-cve': -1,
            'Exploit-samba':-1,
            'Exploit-shellshock': -1,
            'Exploit-fileManager': -1,
            'Exploit-reflexGallery':0,
            'Exploit-ftp':-1
        }
    },
    'RHOST3': {
        'IP': "192.168.1.54" ,
        'INFO':{
            'os': 'UNKNOWN', 
            'ports': [ 
                {'port': '21', 
                'service': 'UNKNOWN', 
                'version': 'UNKNOWN'
                },
                {'port': '80', 
                'service': 'Apache httpd', 
                'version': '2.4.29'
                }]},
        'VULN':{
            'Cve-2012-1823': 0,
            'Wordpress-Reflex': -1,
            'Wordpress-FileManager': -1,
            'Shellshock': -1
        },
        'Exploit':{
            'Exploit-ssh': -1,
            'Exploit-cve': 0,
            'Exploit-samba':-1,
            'Exploit-shellshock': -1,
            'Exploit-fileManager': -1,
            'Exploit-reflexGallery':-1,
            'Exploit-ftp':-1
        }
    },
    'RHOST4': {
        'IP': "192.168.1.28" ,
        'INFO':{
            'os': 'UNKNOWN', 
            'ports': [
                {'port': '22', 
                'service': 'OpenSSH', 
                'version': '2.9p2'
                }, 
                {'port': '80', 
                'service': 'Apache httpd', 
                'version': '1.3.20'
                }, 
                {'port': '139', 
                'service': 'Samba smbd', 
                'version': 'UNKNOWN'
                }]},
        'VULN':{
            'Cve-2012-1823': -1,
            'Wordpress-Reflex': -1,
            'Wordpress-FileManager': -1,
            'Shellshock': -1
        },
        'Exploit':{
            'Exploit-ssh': -1,
            'Exploit-cve': -1,
            'Exploit-samba': 0,
            'Exploit-shellshock': -1,
            'Exploit-fileManager': -1,
            'Exploit-reflexGallery':-1,
            'Exploit-ftp':-1
        }
    },
    'RHOST5': {
        'IP': "192.168.1.25" ,
        'INFO':{
            'os': 'UNKNOWN', 
            'ports': [
                {'port': '22', 
                'service': 'OpenSSH', 
                'version': '2.9p2'
                }, 
                {'port': '21', 
                'service': 'UNKNOWN', 
                'version': 'UNKNOWN'
                }]},
        'VULN':{
            'Cve-2012-1823': -1,
            'Wordpress-Reflex': -1,
            'Wordpress-FileManager': -1,
            'Shellshock': -1
        },
        'Exploit':{
            'Exploit-ssh': 0,
            'Exploit-cve': -1,
            'Exploit-samba': -1,
            'Exploit-shellshock': -1,
            'Exploit-fileManager': -1,
            'Exploit-reflexGallery':-1,
            'Exploit-ftp':-1
        }
    },
     'RHOST6': {
        'IP': "192.168.1.55" ,
        'INFO':{
            'os': 'UNKNOWN', 
            'ports': [
                {'port': '21', 
                'service': 'UNKNOWN', 
                'version': 'UNKNOWN'
                }]},
        'VULN':{
            'Cve-2012-1823': -1,
            'Wordpress-Reflex': -1,
            'Wordpress-FileManager': -1,
            'Shellshock': -1
        },
        'Exploit':{
            'Exploit-ssh': -1,
            'Exploit-cve': -1,
            'Exploit-samba': -1,
            'Exploit-shellshock': -1,
            'Exploit-fileManager': -1,
            'Exploit-reflexGallery':-1,
            'Exploit-ftp':0
        }
    },

}

