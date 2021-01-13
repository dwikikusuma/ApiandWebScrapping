# POKEMON
# https://pokeapi.co/

import requests

# url =  
try:
    poke = input("Pokemon Name: ").lower()
    url = f" https://pokeapi.co/api/v2/pokemon/{poke}"
    data = requests.get(url)
    output = data.json()

    #print(output)
    print("===============")
    print(f"Name: {output['forms'][0]['name']}")
    # HP
    # print(f"{output['stats'][0]['stat']['name']}: {output['stats'][0]['base_stat']}")
    # #attack
    # print(f"{output['stats'][1]['stat']['name']}: {output['stats'][1]['base_stat']} ")
    # #defense
    # print(f"{output['stats'][2]['stat']['name']}: {output['stats'][2]['base_stat']} ")
    # #speed
    # print(f"{output['stats'][5]['stat']['name']}: {output['stats'][5]['base_stat']} ")

    # munculin semua stat sp attack & defense
    stat_len = len(output['stats'])
    #print(stat_len)
    for i in range(stat_len):
        stat = f"{output['stats'][i]['stat']['name']}: {output['stats'][i]['base_stat']}"
        stat_dp = stat.replace("-"," ")
        print(stat_dp)
        #print(f"{output['stats'][i]['stat']['name']}: {output['stats'][i]['base_stat']}")

    #type
    print(f"Type: {output['types'][0]['type']['name']} ")

    # pic url
    pic_url = output['forms'][0]['url']
    #print(pic_url)
    data_pic = requests.get(pic_url)
    out_pic = data_pic.json()
    print(f"image link: {out_pic['sprites']['front_default']}")
    #print(f"Image")

    #abilities
    limit = len(output['abilities'])

    #print(limit)
    print("Abilities:")
    for i in range(limit):
        ability = output['abilities'][i]['ability']['name']
        ability_dp = ability.replace("-"," ")
        print(f"- {ability_dp}:")
        #print(f"-{output['abilities'][i]['ability']['name']}")

        #ability desc
        ability_desc = f"https://pokeapi.co/api/v2/ability/{ability}/"
        data_ability_desc = requests.get(ability_desc)
        out_ad = data_ability_desc.json()
        ad_dp = (out_ad['effect_entries'][1]['effect'])
        #slicing sampai .
        #ad = ad_dp.split(".")[0]
        print(ad_dp)
        print(" ")

    # ability descritpipn
 
except:
    print("Pokemon Doesn't Exsist")

