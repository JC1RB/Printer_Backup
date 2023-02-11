import subprocess

result = subprocess.run(["date"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

current_time = result.stdout.decode().strip()
print("Current time is:", current_time)
