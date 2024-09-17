import wmi
import psutil
import speedtest

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

print('OS Name: {0}'.format(os_name))
print('OS Version: {0}'.format(os_version))
print('CPU: {0}'.format(proc_info.Name))
print('RAM: {0} GB'.format(system_ram))
print('Graphics Card: {0}'.format(gpu_info.Name))

print("Number of cores in system", psutil.cpu_count())
print("\nNumber of physical cores in system",)
 
print(psutil.sensors_battery())

obj_Disk = psutil.disk_usage('/')

print (obj_Disk.total / (1024.0 ** 3))
print (obj_Disk.used / (1024.0 ** 3))
print (obj_Disk.free / (1024.0 ** 3))
print (obj_Disk.percent)

memory_info = psutil.virtual_memory()

print("\nMemory Information:")
print(f"Total Memory: {memory_info.total} bytes")
print(f"Available Memory: {memory_info.available} bytes")
print(f"Used Memory: {memory_info.used} bytes")
print(f"Memory Utilization: {memory_info.percent}%")

# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))

speed_test = speedtest.Speedtest()

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

download_speed = bytes_to_mb(speed_test.download())
print("Your Download speed is", download_speed, "MB")
upload_speed = bytes_to_mb(speed_test.upload())
print("Your Upload speed is", upload_speed, "MB")

