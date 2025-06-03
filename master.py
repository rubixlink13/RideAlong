import api
from mount import Mount

def generate(BEARER_TOKEN):
    master = []
    add_achievement_mounts(BEARER_TOKEN, master)
    add_encounter_mounts(BEARER_TOKEN, master)
    return master

def add_achievement_mounts(BEARER_TOKEN, master):
    pass

def add_encounter_mounts(BEARER_TOKEN, master):
    pass
