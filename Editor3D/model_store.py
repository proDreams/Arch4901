from Editor3D.service import Point3D, Angle3D, Color


class Texture:
    pass


class Polygon:
    points: Point3D = []


class PolygonalModel:
    polygons: [Polygon]
    textures: [Texture]

    def __init__(self, textures: list[Texture]):
        self.textures = textures
        self.polygons = []


class Flash:
    location: Point3D
    angle: Angle3D
    color: Color
    power: float

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Camera:
    location: Point3D
    angle: Angle3D

    def rotate(self, angle: Angle3D):
        pass

    def move(self, point: Point3D):
        pass


class Scene:
    id_: int
    models: list[PolygonalModel]
    flashes: list[Flash]
    cameras: list[Camera] = []

    def __init__(self, id_, models: list[PolygonalModel], flashes: list[Flash], cameras: list[Camera]):
        self.id_ = id_

        if len(models) > 0:
            self.models = models
        else:
            raise ValueError("Должна быть одна модель")

        self.flashes = flashes

        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise ValueError("Должна быть одна камера")

    @staticmethod
    def method1(flash):
        return flash

    @staticmethod
    def method2(model, flash):
        return model or flash
