from car_app.abstract_class import Car, IFuelStation, ICarWash


class PickUp(Car, IFuelStation, ICarWash):
    load_capacity: int

    def __init__(self, brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity,
                 load_capacity):
        super().__init__(brand, model, color, body_type, wheel_count, fuel_type, transmission_type, engine_capacity)
        self.load_capacity = load_capacity

    @staticmethod
    def sweep_street():
        print('Подмееетаааееем, вжух, вжух)')

    def refill(self):
        print('Заправляемся, бульк)')
