import pickle
import json


class Plane:

    def __init__(self, plane_model, takeoff_time, landing_time, capacity, serial_number):
        self.plane_model = plane_model
        self.takeoff_time = takeoff_time
        self.landing_time = landing_time
        self.capacity = capacity
        self.serial_number = serial_number

    def takeoff(self):
        print(f'The plane takes off in {self.takeoff_time}')

    def landing(self):
        print(f'The plane will land in {self.landing_time}')

    def save(self):
        with open("plane.txt", "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(self):
        with open("plane.txt", "rb") as f:
            return pickle.load(f)

    def pack(self, filename, plane):
        objects = [plane]
        with open(filename, "w") as f:
            json.dump({f"{obj.__class__.__name__} {i}": obj.__dict__ for i, obj in enumerate(objects)}, f)

    @staticmethod
    def unpack(filename):
        with open(filename, "r") as f:
            new_plane = json.load(f)
            plane_list = []
            for i in range(len(new_plane)):
                name_class = list(new_plane.keys())[i].split()[0]
                obj_prop = list(new_plane.values())[i]
                new_obj = globals()[name_class](**obj_prop)
                plane_list.append(new_obj)
                return plane_list


airplane = Plane("Boeing", '13:45', '17:20', 200, 7300921)
airplane.pack('plane', airplane)
airplane.unpack('plane')
airplane.takeoff()
airplane.landing()

