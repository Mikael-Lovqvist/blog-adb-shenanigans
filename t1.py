import subprocess, shlex
from pathlib import Path
#http://www.temblast.com/ref/akeyscode.htm

python_app = 'org.qpython.qpy3/jackpal.androidterm.Term'

payload = Path('pl2.py').read_text()
script = f'exec({payload!r})'
quoted_payload = shlex.quote(script)

subprocess.call(('adb', 'shell', 'am', 'start', '-W', python_app))
subprocess.call(('adb', 'shell', 'input', 'text', quoted_payload))
subprocess.call(('adb', 'shell', 'input', 'keyevent', '66'))	#Return