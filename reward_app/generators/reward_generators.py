from reward_app.abstracts.abstract_classes import ItemFabric
from reward_app.rewards import reward_classes as reward


class GoldGenerator(ItemFabric):
    rarity = 3

    def create_item(self):
        return reward.Gold()


class GemGenerator(ItemFabric):
    rarity = 1

    def create_item(self):
        return reward.Gem()


class WeaponGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return reward.Weapon()


class ArmourGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return reward.Armour()


class PotionGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return reward.Potion()


class ExpGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return reward.Exp()


class JewerlyGenerator(ItemFabric):
    rarity = 10

    def create_item(self):
        return reward.Jewerly()
