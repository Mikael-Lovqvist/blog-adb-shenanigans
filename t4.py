#This test transfers a whole python package
import subprocess, shlex, time
from pathlib import Path
#keycode table: http://www.temblast.com/ref/akeyscode.htm

python_app = 'org.qpython.qpy3/jackpal.androidterm.Term'
remote_payload_path = '/storage/emulated/0/qpython/packaged_payload/'
package_name = 'test_package'

local_package_path = Path('.') / package_name	#Assuming local path for now

final_remote_payload_path = Path(remote_payload_path) / package_name

payload = f'''

import sys
sys.path.append({remote_payload_path!r})
from {package_name} import some_module

'''.strip()

script = f'exec({payload!r})'
quoted_payload = shlex.quote(script)

#Remove any previous payload
subprocess.call(('adb', 'shell', 'rm', '-r', final_remote_payload_path))
#Transfer new payload
subprocess.call(('adb', 'push', local_package_path, final_remote_payload_path))

#Start python terminal
subprocess.call(('adb', 'shell', 'am', 'start', '-W', python_app))
#Input the payload that runs the final payload
subprocess.call(('adb', 'shell', 'input', 'text', quoted_payload))
#Terminate input with return
subprocess.call(('adb', 'shell', 'input', 'keyevent', '66'))

