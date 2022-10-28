import subprocess, shlex, time
from pathlib import Path
#http://www.temblast.com/ref/akeyscode.htm

python_app = 'org.qpython.qpy3/jackpal.androidterm.Term'

payload = Path('pl2.py').read_text()
script = f'exec({payload!r})'
quoted_payload = shlex.quote(script)

subprocess.call(('adb', 'shell', 'am', 'start', '-W', python_app))
subprocess.call(('adb', 'shell', 'input', 'text', quoted_payload))
subprocess.call(('adb', 'shell', 'input', 'keyevent', '66'))	#Return

time.sleep(0.1)	#Wait a bit to make sure the command has been executed

subprocess.call(('adb', 'shell', 'cat', '/storage/emulated/0/qpython/remote-session.info'))
