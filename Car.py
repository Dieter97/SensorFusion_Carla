import os
import random
from time import sleep

import carla


class Car:

    def __init__(self, actor_filter, npc_count=10,map_name="Town04"):
        # Constants
        self._actor_filter = actor_filter
        self.actor_list = []

        # Connect to the carla server
        print("Connecting to Carla server...")
        self.client = carla.Client('192.168.1.137', 2000)
        self.client.set_timeout(10.0)  # seconds
        self.client.load_world(map_name)
        print("Connected!")
        self.world = self.client.get_world()
        self.map = self.world.get_map()
        self.count = npc_count

        # Spawn player with sensors
        self.spawn_ego()

        # Spawn random npc's
        self.spawn_npc(self.count)

        # Start the ros brige
        os.system('./startRosBridge.sh')

        # Keep alive
        while 1:
            sleep(10)

    def spawn_ego(self):
        # Spawn the player and vehicle
        vehicle = random.choice(self.world.get_blueprint_library().filter(self._actor_filter))
        vehicle.set_attribute('role_name', 'hero')
        spawn_points = self.map.get_spawn_points()
        spawn_point = random.choice(spawn_points) if spawn_points else carla.Transform()
        player = self.world.try_spawn_actor(vehicle, spawn_point)
        self.actor_list.append(player)

        # RGB Senors
        camera_bp = self.world.get_blueprint_library().find('sensor.camera.rgb')
        # camera_bp.set_attribute('sensor_tick', '1.0')
        camera_bp.set_attribute('image_size_x', '1344') #1344
        camera_bp.set_attribute('image_size_y', '376') #376
        transform = carla.Transform(carla.Location(x=1.8, z=2.5))
        camera = self.world.spawn_actor(camera_bp, transform, attach_to=player)
        self.actor_list.append(camera)

        # LiDAR
        lidar_bp = self.world.get_blueprint_library().find('sensor.lidar.ray_cast')
        # lidar_bp.set_attribute('sensor_tick', '1.0')
        lidar_bp.set_attribute('range', '10000')
        lidar_bp.set_attribute('channels', '16')
        lidar_bp.set_attribute('upper_fov', '15')
        lidar_bp.set_attribute('lower_fov', '-15')
        lidar_bp.set_attribute('rotation_frequency', '20')
        # lidar_bp.set_attribute('points_per_second', '300000')
        transform = carla.Transform(carla.Location(x=1.5, z=2.5))
        lidar = self.world.spawn_actor(lidar_bp, transform, attach_to=player)
        self.actor_list.append(lidar)

        player.set_autopilot(True)
        print("Ego (player) spawned!")

    def spawn_npc(self, npc_count):
        spawn_points = list(self.world.get_map().get_spawn_points())
        random.shuffle(spawn_points)

        """for spawn_point in spawn_points:
            if self.try_spawn_random_vehicle_at(spawn_point):
                npc_count -= 1
            if npc_count <= 0:
                break"""
        while npc_count > 0:
            sleep(0.1) # Delay between spawns
            if self.try_spawn_random_vehicle_at(random.choice(spawn_points)):
                npc_count -= 1

    def try_spawn_random_vehicle_at(self, transform):
        blueprints = self.world.get_blueprint_library().filter('vehicle.*')
        blueprint = random.choice(blueprints)
        if blueprint.has_attribute('color'):
            color = random.choice(blueprint.get_attribute('color').recommended_values)
            blueprint.set_attribute('color', color)
        blueprint.set_attribute('role_name', 'autopilot')
        vehicle = self.world.try_spawn_actor(blueprint, transform)
        if vehicle is not None:
            self.actor_list.append(vehicle)
            vehicle.set_autopilot()
            print('spawned %r at %s' % (vehicle.type_id, transform.location))
            return True
        return False

    def __del__(self):
        print('Destroying actors...')
        for actor in self.actor_list:
            actor.destroy()
        print('All done!')


if __name__ == "__main__":
    car = Car('vehicle.tesla.*', 5)
