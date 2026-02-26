#5.Uzdevums.
# Label; MountPoint; TotalSize (MB); Used (%)
partitions = [
"System;/;50000;85",
"Data;/home;150000;40",
"Cache;/tmp;5000;10",
"Backup;/mnt/backup;500000;92",
"USB-Drive;/media/usb;16000;0",
"Logs;/var/log;10000;95",
"Database;/var/lib/mysql;80000;70",
"Shared;/mnt/shared;200000;15",
"Win-System;/mnt/win;100000;90",
"Recovery;/recovery;2000;98"
]
mount = input("ievadiet montējuma punktu:")
anime = False
for p in partitions:
    dala = p.split(";")
    label = dala[0]
    mount2 = dala[1]
    if mount == mount2:
        print(label)
        anime = True
        break
    if not anime:
        print("Nav atrasts")
        #man ķipa strādā un tai pašā laikā nestrādā...


