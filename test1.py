import os
import psutil
 
# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()
 
cpu_usage = (load15/os.cpu_count()) * 100
 
print("The CPU usage is : ", cpu_usage)

# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
