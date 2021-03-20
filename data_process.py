import os

file_path = "logfile_2020_03_19_09_31_56.txt"
Name_list = ['ACCE','GYRO','MAGN','PRES','AHRS']
SensorTimestamp = float(1470242.430)
SensorTimestamp1 = float(1470222.644)
list_WIFI = []
list_GNSS = []

def openFile(SensorTimestamp,SensorTimestamp1):
    with open(file_path,'r') as f:
        for lines in f.readlines():
            if '%' in lines:
                continue
            else:
                line_list = lines.strip('\n').split(';')
                if str(line_list[0]) in Name_list:
                    num = float(line_list[2])
                    if num < SensorTimestamp:
                        SensorTimestamp = num
                if str(line_list[0]) =='WIFI':
                    num = float(line_list[2])
                    if num < SensorTimestamp1:
                        SensorTimestamp1 = num
    return SensorTimestamp,SensorTimestamp1


def WIFI(SensorTimestamp_WIFI):
    with open(file_path,'r') as f:
        for lines in f.readlines():
            if '%' in lines:
                continue
            else:
                line_list = lines.strip('\n').split(';')
            if str(line_list[0]) == 'WIFI':
                line_list_wifi = line_list[4].split(':')
                Mac_BSSID = ''.join(line_list_wifi)
                Mac_BSSID = '0x' + Mac_BSSID
                Mac_BSSID = int(Mac_BSSID, 16)
                list_wifi = []
                list_wifi.append((float(line_list[2])-SensorTimestamp_WIFI))
                list_wifi.append(Mac_BSSID)
                list_wifi.append(line_list[-1])
                list_WIFI.append(list_wifi)
    with open("wifi.txt", 'w') as f:
        for list_wifi in list_WIFI:
            f.write(str(list_wifi))
            f.write('\n')
        f.close()

def GNSS():
    with open(file_path, 'r') as f:
        for lines in f.readlines():
            if '%' in lines:
                continue
            else:
                line_list = lines.strip('\n').split(';')
                if str(line_list[0]) == 'GNSS':
                    list_GNSS.append(line_list)
    with open("GNSS.txt", 'w') as f:
        for line_gnss in list_GNSS:
            f.write(str(line_gnss))
            f.write('\n')
    f.close()

#def IMU():














if __name__ == "__main__":

    min_five, min_WIFi = openFile(SensorTimestamp,SensorTimestamp1)
    print(min_WIFi)
    WIFI(min_WIFi)
    GNSS()




