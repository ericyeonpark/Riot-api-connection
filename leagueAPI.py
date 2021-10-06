from riotwatcher import LolWatcher, ApiError
import pandas as pd
from os import getenv

# global variables
# api_key = getenv('riot_api')
api_key = 'RGAPI-cb5df38f-1f55-4f2b-951d-e36e88d6f5d9'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Doublelift')
print(me)

# Return the rank status for Doublelift
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)