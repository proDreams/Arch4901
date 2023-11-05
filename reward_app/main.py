from random import randint

from reward_app.generators import reward_generators as gen

TURNS = 20

REWARDS_GENERATORS = [gen.GoldGenerator(),
                      gen.GemGenerator(),
                      gen.WeaponGenerator(),
                      gen.ArmourGenerator(),
                      gen.PotionGenerator(),
                      gen.ExpGenerator(),
                      gen.JewerlyGenerator()]

ranked_rewards = [reward for reward in REWARDS_GENERATORS for _ in range(reward.rarity)]

for i in range(TURNS):
    ranked_rewards[randint(0, len(ranked_rewards) - 1)].create_item().open()
