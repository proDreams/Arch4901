# Переписать код SpeedCalculation в соответствии с Open-Closed Principle:

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    @abstractmethod
    def calculate_allowed_speed(self):
        pass


class Car(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.8


class Bus(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.6


class SpeedCalculation:
    @staticmethod
    def calculate_allowed_speed(vehicle):
        return vehicle.calculate_allowed_speed()
