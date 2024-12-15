
import Adafruit_DHT
from pydantic import BaseModel



class TempAndHumiditySensor(BaseModel):
    def configure(self, pin: int):
        self.pin = pin

    def measure(self) -> float | float:
        humidity, temperature = Adafruit_DHT.read(self.sensor_type, self.pin)
        return humidity, temperature 
    
    def register_device() -> str:
        response = requests.post(f"{BACKEND_URL}/register", json=DEVICE_INFO)
        print("Registration:", response.json())
        device_id = response.json()['device_id']
        return device_id
    
    def send_data():
        response = requests.post(f"{BACKEND_URL}/data", json=DATA)
        data = {"device_id": DEVICE_INFO['device_id'], "humidity": humidity}
        response = requests.post(f"{BACKEND_URL}/data", json=data)
        print("Data Sent:", response.json())