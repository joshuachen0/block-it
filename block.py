import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

def block(url):
    '''
    Description:
        block(url): Adds a URL to be blocked to the Windows hosts file
    Input(s):
        url: The URL to be blocked as a string
    Output(s):
        --NONE--
    '''
    ip_address = '127.0.0.1'
    hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, 'a') as hosts:
        entry = '\n' + ip_address + ' ' + url
        hosts.writelines(entry)

def main():
    '''
    Description:
        main(): Seeks user input of URL and calls block(url) with this URL
    Input(s):
        --NONE--
    Output(s):
        --NONE--
    '''
    print('WARNING: This script cannot unblock blocked sites. You will have to do so manually.')
    url = raw_input('URL of website to be blocked: ')
    block(url)

if __name__ == '__main__':
    # hosts file requires administrator privileges to be edited
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
        # Run the script
        main()
        sys.exit(0)
