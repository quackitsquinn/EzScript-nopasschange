
def pwsh(cmd: str) -> str:
    return subprocess.check_output([f'C:\\Windows\\System32\\powershell.exe {cmd}', '-c', cmd]).decode('utf-8')

users = open('users.txt', 'r').read().split("admin") # probably wrong

local_users = users[0].split('\n')
admin_users = users[1].split('\n')

actual_users = pwsh('Get-LocalUser').split('\n')

for user in use
