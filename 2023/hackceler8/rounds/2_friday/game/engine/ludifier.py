# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
from components.wall import Wall


class FakeSize:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class FakeCoord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ludifier:
    def __init__(self, map):
        self.map = map
        logging.info(self.map)
        logging.info(self.map.size)
        self.max_x = map.size[0]
        self.max_y = map.size[1]

        self.counter = 0
        # Ticks between new walls, lower is faster
        self.advancement_speed = 30
        self.wall_width = self.map.tile_size[0]

    def tick(self):
        self.counter += 1
        if not self.counter % self.advancement_speed:
            logging.debug(
                f"Adding a new wall at {self.counter // self.advancement_speed * self.wall_width}")
            w = Wall(FakeCoord(self.counter // self.advancement_speed * self.wall_width,
                               10000),
                     FakeSize(self.wall_width, 10000),
                     "killawall")
            return w

