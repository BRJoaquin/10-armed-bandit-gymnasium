from gymnasium.envs.registration import register

register(
    id="k_bandits_env/KBandits-v0",
    entry_point="k_bandits_env.envs:BanditEnv",
)
register(
    id="k_bandits_env/KBanditsGaussian-v0",
    entry_point="k_bandits_env.envs:BanditTenArmedGaussian",
)
