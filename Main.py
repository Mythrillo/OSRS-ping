import subprocess
import re


def ping(host):

    out = subprocess.check_output(host, False)

    timestr = re.compile("Average = [0-9]+ms").findall(str(out))
    a = re.compile("[0-9][0-9][0-9]|[0-9][0-9]").findall(str(timestr))
    if len(a) == 0:
        return 9999
    else:
        return int(a[0])


lowest_latency = 9999
best_world = 9999
for world in range(1, 231):
    command= "ping -n 3 " + "oldschool" + str(world) + ".runecsape.com"
    latency = ping(command)
    print("Average ping for world " + str(300 + world) + " is " + str(latency) + "ms")
    if latency < lowest_latency:
        lowest_latency = latency
        best_world = world + 300
print("The best world is " + str(best_world) + " with " + str(lowest_latency) + "ms")
