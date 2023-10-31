from Editor3D.model_store import PolygonalModel, Scene, Camera, Flash


class IModelChangedObserver:
    def apply_update_model(self):
        pass


class IModelChanger:
    def notify_change(self, sender):
        pass


class ModelStore(IModelChanger):
    models: list[PolygonalModel]
    scenes: list[Scene]
    flashes: list[Flash]
    cameras: list[Camera]
    _change_observers = list[IModelChangedObserver]

    def __init__(self, change_observer: list[IModelChangedObserver]) -> None:
        self.models = [PolygonalModel(None)]
        self.scenes = [Scene(0, self.models, self.flashes, self.cameras)]
        self.flashes = [Flash()]
        self.cameras = [Camera()]
        self._change_observers = change_observer

    def get_scene(self, id_):
        for scene in self.scenes:
            if scene.id_ == id_:
                return scene

    def notify_change(self, sender: IModelChanger):
        pass
