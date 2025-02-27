# Useful Windows CMD Commands

- [Useful Windows CMD Commands](#useful-windows-cmd-commands)
  - [Basic Commands](#basic-commands)
  - [File \& Directory Management](#file--directory-management)
  - [System Information \& Diagnostics](#system-information--diagnostics)
  - [Disk \& Storage Management](#disk--storage-management)
  - [User Management](#user-management)
  - [Network Commands](#network-commands)
  - [Power Management](#power-management)
  - [Security \& Permissions](#security--permissions)
  - [Advanced Windows Commands](#advanced-windows-commands)
  - [Programming \& Development](#programming--development)
  - [Conclusion](#conclusion)

## Basic Commands

| Command | Description |

|---------|-------------|
| `help` | Displays a list of available commands. |
| `cls` | Clears the Command Prompt screen. |
| `exit` | Closes the Command Prompt. |
| `ver` | Displays the Windows version. |
| `color [attr]` | Changes the text and background color of CMD (e.g., `color 0A` for green text). |

## File & Directory Management

| Command | Description |

|---------|-------------|
| `dir` | Lists files and directories in the current folder. |
| `cd [path]` | Changes the current directory (e.g., `cd C:\Users`). |
| `cd ..` | Moves up one directory level. |
| `md [folder]` | Creates a new directory (e.g., `md NewFolder`). |
| `rd [folder]` | Removes an empty directory. |
| `del [file]` | Deletes a specific file (e.g., `del file.txt`). |
| `copy [source] [destination]` | Copies a file to another location (e.g., `copy C:\file.txt D:\`). |
| `move [source] [destination]` | Moves a file to another location. |
| `ren [oldname] [newname]` | Renames a file (e.g., `ren old.txt new.txt`). |

## System Information & Diagnostics

| Command | Description |

|---------|-------------|
| `tasklist` | Displays a list of running processes. |
| `taskkill /IM [process.exe] /F` | Terminates a process by name (e.g., `taskkill /IM notepad.exe /F`). |
| `taskkill /PID [pid] /F` | Terminates a process by its process ID. |
| `systeminfo` | Displays detailed information about the system. |
| `wmic cpu get name` | Shows the processor model. |
| `wmic os get Caption, Version` | Displays the OS name and version. |
| `wmic diskdrive get model, size` | Shows hard drive details. |
| `ipconfig` | Displays network configuration. |
| `ipconfig /all` | Shows all network information, including MAC addresses. |
| `ipconfig /release` | Releases the current IP address (for DHCP networks). |
| `ipconfig /renew` | Requests a new IP address (for DHCP networks). |
| `ping [hostname or IP]` | Checks the network connection to a server (e.g., `ping google.com`). |
| `tracert [hostname]` | Traces the path packets take to a destination (e.g., `tracert google.com`). |
| `netstat -ano` | Displays all active network connections and their associated processes. |
| `nslookup [domain]` | Finds the IP address of a domain (e.g., `nslookup google.com`). |

## Disk & Storage Management

| Command | Description |
|---------|-------------|
| `chkdsk /f` | Checks and repairs disk errors. |
| `chkdsk /r` | Finds and recovers bad sectors on a disk. |
| `diskpart` | Opens the Disk Partition tool. |
| `diskpart > list disk` | Lists available disks. |
| `diskpart > select disk [number]` | Selects a specific disk. |
| `diskpart > clean` | Deletes all partitions on the selected disk. |
| `diskpart > create partition primary` | Creates a primary partition on the selected disk. |
| `format [drive:] /fs:[filesystem]` | Formats a disk (e.g., `format D: /fs:NTFS`). |

## User Management

| Command | Description |
|---------|-------------|
| `whoami` | Displays the currently logged-in user. |
| `net user` | Lists all user accounts on the system. |
| `net user [username] /add` | Creates a new user (requires admin privileges). |
| `net user [username] /delete` | Deletes a user account (requires admin privileges). |
| `net localgroup administrators [username] /add` | Adds a user to the administrators group. |

## Network Commands

| Command | Description |
|---------|-------------|
| `arp -a` | Displays the system's ARP (Address Resolution Protocol) table. |
| `netsh wlan show profile` | Lists saved Wi-Fi networks. |
| `netsh wlan show profile name=[SSID] key=clear` | Displays Wi-Fi password for a saved network. |
| `netstat -r` | Displays the routing table. |
| `net view` | Lists shared resources on the network. |
| `net use [drive:] \\[computer]\\[share]` | Maps a network drive. |
| `net stop [service]` | Stops a network service. |
| `net start [service]` | Starts a network service. |

## Power Management

| Command | Description |
|---------|-------------|
| `shutdown /s /t [seconds]` | Shuts down the system after a set time (e.g., `shutdown /s /t 60`). |
| `shutdown /r /t [seconds]` | Restarts the system after a set time. |
| `shutdown /a` | Cancels a scheduled shutdown. |
| `powercfg /batteryreport` | Generates a battery usage report. |
| `powercfg /energy` | Analyzes power efficiency and generates a report. |

## Security & Permissions

| Command | Description |
|---------|-------------|
| `cipher /w:[drive:]` | Securely deletes data by overwriting it. |
| `attrib +h +s +r [file]` | Hides a file and makes it system-protected. |
| `attrib -h -s -r [file]` | Unhides a file. |
| `icacls [file] /grant [user]:[permission]` | Grants permissions to a file (e.g., `icacls file.txt /grant User:F`). |
| `icacls [file] /deny [user]:[permission]` | Denies permissions for a user. |

## Advanced Windows Commands

| Command | Description |
|---------|-------------|
| `sfc /scannow` | Scans and repairs corrupted system files. |
| `DISM /Online /Cleanup-Image /RestoreHealth` | Repairs the Windows image. |
| `bcdedit` | Manages the boot configuration data. |
| `msconfig` | Opens the System Configuration tool. |
| `gpupdate /force` | Forces a Group Policy update. |
| `regedit` | Opens the Windows Registry Editor. |
| `eventvwr` | Opens the Windows Event Viewer. |

## Programming & Development

| Command | Description |
|---------|-------------|
| `echo %PATH%` | Displays the system's environment variables. |
| `setx PATH "%PATH%;C:\\new\\path"` | Adds a new path to the system's PATH variable. |
| `assoc` | Displays file extension associations. |
| `assoc .txt=txtfile` | Changes file association (e.g., for `.txt` files). |
| `fc [file1] [file2]` | Compares two files line by line. |

## Conclusion

These commands help in managing files, networking, system performance, troubleshooting, and security tasks. If you're new to CMD, practice with basic commands first before using system-critical commands like `diskpart`, `bcdedit`, or `sfc`. Let me know if you need further explanations! 🚀
