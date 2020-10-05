import subprocess

def ping(ip):
    try:
        subprocess.check_output(["ping", "-c", "3","-i", "1",  ip])
        return True                      
    except subprocess.CalledProcessError:
        return False

print ping('localhost')
print ping('10.23.23.23')

