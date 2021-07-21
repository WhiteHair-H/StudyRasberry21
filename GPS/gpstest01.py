import serial

def GPS_Info():
   global NMEA_buff
   global lat_in_degrees
   global long_in_degrees
   nmea_time = []
   nmea_latitude = []
   nmea_longitude = []
   nmea_time = NMEA_buff[0]                    #extract time from GPGGA string
   nmea_latitude = NMEA_buff[1]                #extract latitude from GPGGA string
   nmea_longitude = NMEA_buff[3]               #extract longitude from GPGGA string
   
   print("NMEA Time: ", nmea_time,'\n')
   print("NMEA Latitude:", nmea_latitude,"NMEA Longitude:", nmea_longitude,'\n')
   
   lat = float(nmea_latitude)                  #convert string into float for calculation
   longi = float(nmea_longitude)               #convertr string into float for calculation
   
   lat_in_degrees = convert_to_degrees(lat)    #get latitude in degree decimal format
   long_in_degrees = convert_to_degrees(longi) #get longitude in degree decimal format

#convert raw NMEA string into degree decimal format  
def convert_to_degrees(raw_value):
   decimal_value = raw_value/100.00
   degrees = int(decimal_value)
   mm_mmmm = (decimal_value - int(decimal_value))/0.6
   position = degrees + mm_mmmm
   position = "%.4f" %(position)
   return position

gpgga_info = "GNGGA,"
# ser = Serial('COM9',9600) #윈도우
ser = serial.Serial('/dev/ttyS0', 9600) #라즈베리파이
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0

try:
   while True:
       if ser.readable():
           res = ser.readline()
           rec_data = res.decode()[:len(res)-1]
           #print(res.decode()[:len(res)-1])
           # print(rec_data)
           GPGGA_data_available = rec_data.find(gpgga_info)
           if (GPGGA_data_available > 0):
               GPGGA_buffer = rec_data.split(gpgga_info,1)[1]
               NMEA_buff = (GPGGA_buffer.split(','))
               # print(NMEA_buff)
               GPS_Info()
except KeyboardInterrupt:
   print('GPS terminated')