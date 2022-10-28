import subprocess, shlex, time
from pathlib import Path
#keycode table: http://www.temblast.com/ref/akeyscode.htm

python_app = 'org.qpython.qpy3/jackpal.androidterm.Term'
payload_path = '/storage/emulated/0/qpython/payload.py'

payload = f'''

from pathlib import Path
exec(Path({payload_path!r}).read_text())

'''.strip()

script = f'exec({payload!r})'
quoted_payload = shlex.quote(script)

#Remove any previous payload
subprocess.call(('adb', 'shell', 'rm', payload_path))
#Transfer new payload
subprocess.call(('adb', 'push', 'payload.py', payload_path))

#Start python terminal
subprocess.call(('adb', 'shell', 'am', 'start', '-W', python_app))
#Input the payload that runs the final payload
subprocess.call(('adb', 'shell', 'input', 'text', quoted_payload))
#Terminate input with return
subprocess.call(('adb', 'shell', 'input', 'keyevent', '66'))

