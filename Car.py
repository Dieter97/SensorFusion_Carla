import random
from time import sleep

import carla


class Car:

    def __init__(self,actor_filter):
        # Constants
        self._actor_filter = actor_filter
        self.actor_list = []

        # Connect to the carla server
        print("Connecting to Carla server...")
        self.client = carla.Client('192.168.1.116', 2000)
        self.client.set_timeout(10.0)  # seconds
        print("Connected!")
        self.world = self.client.get_world()
        self.map = self.world.get_map()

        # Spawn the player and vehicle
        vehicle = random.choice(self.world.get_blueprint_library().filter(self._actor_filter))
        vehicle.set_attribute('role_name', 'hero')
        spawn_points = self.map.get_spawn_points()
        spawn_point = random.choice(spawn_points) if spawn_points else carla.Transform()
        player = self.world.try_spawn_actor(vehicle, spawn_point)
        self.actor_list.append(player)

        # RGB Senors
        camera_bp = self.world.get_blueprint_library().find('sensor.camera.rgb')
        #camera_bp.set_attribute('sensor_tick', '1.0')
        transform = carla.Transform(carla.Location(x=1.8, z=2.5))
        camera = self.world.spawn_actor(camera_bp, transform, attach_to=player)
        self.actor_list.append(camera)

        # LiDAR
        lidar_bp = self.world.get_blueprint_library().find('sensor.lidar.ray_cast')
        #lidar_bp.set_attribute('sensor_tick', '1.0')
        lidar_bp.set_attribute('range', '10000')
        lidar_bp.set_attribute('channels', '16')
        lidar_bp.set_attribute('upper_fov', '15')
        lidar_bp.set_attribute('lower_fov', '-15')
        #lidar_bp.set_attribute('points_per_second', '300000')
        transform = carla.Transform(carla.Location(x=1.8, z=2.5))
        lidar = self.world.spawn_actor(lidar_bp, transform, attach_to=player)
        self.actor_list.append(lidar)

        player.set_autopilot(True)

        while(1):
            sleep(1)

    def __del__(self):
        print('destroying actors')
        for actor in self.actor_list:
            actor.destroy()
        print('done.')


if __name__ == "__main__":
    car = Car('vehicle.bmw.*')