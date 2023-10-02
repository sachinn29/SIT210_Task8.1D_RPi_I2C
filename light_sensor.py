import smbus
import time

# Define the I2C address of the light sensor
light_sensor_address = 0x23

# Define some constants for the sensor modes
low_power_mode = 0x00
high_power_mode = 0x01
reset_command = 0x07
one_time_high_res_mode = 0X23 

# Create an SMBus object for I2C communication
i2c_bus = smbus.SMBus(1)

# Function to calculate light intensity from sensor data
def calculate_light_intensity(data):
    # Combine the two bytes of sensor data to get the intensity
    result = ((data[1] + (256 * data[0])) / 1.2)
    return result

# Function to read light intensity from the sensor
def read_light_intensity():
    # Read the sensor data in ONE_TIME_HIGH_RES_MODE
    sensor_data = i2c_bus.read_i2c_block_data(light_sensor_address, one_time_high_res_mode)
    # Calculate the light intensity from the sensor data
    intensity = calculate_light_intensity(sensor_data)
    return intensity
 
# Main function to continuously read and print light intensity
def main():
    while True:
        lux = read_light_intensity()
        print(lux)

        # Determine the light level and print a corresponding message
        if lux >= 1200:
            print("Too bright")
        elif 700 <= lux < 1199:
            print("Bright")
        elif 300 <= lux < 699:
            print("Medium")    
        elif 50 <= lux < 299:
            print("Dark")
        elif lux < 49:
            print("Too Dark")
        
        # Wait for 0.5 seconds before taking another reading
        time.sleep(0.5)

# Call the main function to start reading the light sensor
main()
