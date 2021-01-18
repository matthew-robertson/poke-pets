import csv
import json
from math import sqrt

fully_evolved_mons = [
'Venusaur',
'Charizard',
'Blastoise',
'Butterfree',
'Beedrill',
'Pidgeot',
'Raticate',
'Fearow',
'Arbok',
'Raichu',
'Raichu',
'Sandslash',
'Nidoqueen',
'Nidoking',
'Clefable',
'Ninetales',
'Wigglytuff',
'Vileplume',
'Parasect',
'Venomoth',
'Dugtrio',
'Persian',
'Golduck',
'Primeape',
'Arcanine',
'Poliwrath',
'Alakazam',
'Machamp',
'Victreebel',
'Tentacruel',
'Golem',
'Rapidash',
'Slowbro',
'Farfetch',
'Dodrio',
'Dewgong',
'Muk',
'Cloyster',
'Gengar',
'Hypno',
'Kingler',
'Electrode',
'Exeggutor',
'Marowak',
'Hitmonlee',
'Hitmonchan',
'Weezing',
'Kangaskhan',
'Seaking',
'Starmie',
'Mr',
'Jynx',
'Pinsir',
'Pinsir',
'Tauros',
'Gyarados',
'Lapras',
'Ditto',
'Vaporeon',
'Jolteon',
'Flareon',
'Omastar',
'Kabutops',
'Aerodactyl',
'Snorlax',
'Articuno',
'Zapdos',
'Moltres',
'Dragonite',
'Mewtwo',
'Mew',
'Meganium',
'Typhlosion',
'Feraligatr',
'Furret',
'Noctowl',
'Ledian',
'Ariados',
'Crobat',
'Lanturn',
'Xatu',
'Ampharos',
'Bellossom',
'Azumarill',
'Sudowoodo',
'Politoed',
'Jumpluff',
'Sunflora',
'Quagsire',
'Espeon',
'Umbreon',
'Slowking',
'Unown',
'Wobbuffet',
'Girafarig',
'Forretress',
'Dunsparce',
'Steelix',
'Granbull',
'Qwilfish',
'Scizor',
'Shuckle',
'Heracross',
'Ursaring',
'Magcargo',
'Corsola',
'Octillery',
'Delibird',
'Mantine',
'Skarmory',
'Houndoom',
'Kingdra',
'Donphan',
'Stantler',
'Smeargle',
'Hitmontop',
'Miltank',
'Blissey',
'Raikou',
'Entei',
'Suicune',
'Tyranitar',
'Lugia',
'Ho',
'Celebi',
'Sceptile',
'Blaziken',
'Swampert',
'Mightyena',
'Linoone',
'Beautifly',
'Dustox',
'Ludicolo',
'Shiftry',
'Swellow',
'Pelipper',
'Gardevoir',
'Masquerain',
'Breloom',
'Slaking',
'Ninjask',
'Shedinja',
'Exploud',
'Hariyama',
'Delcatty',
'Sableye',
'Mawile',
'Aggron',
'Medicham',
'Manectric',
'Plusle',
'Minun',
'Volbeat',
'Illumise',
'Swalot',
'Sharpedo',
'Wailord',
'Camerupt',
'Torkoal',
'Grumpig',
'Spinda',
'Flygon',
'Cacturne',
'Altaria',
'Zangoose',
'Seviper',
'Lunatone',
'Solrock',
'Whiscash',
'Crawdaunt',
'Claydol',
'Cradily',
'Armaldo',
'Milotic',
'Castform',
'Kecleon',
'Banette',
'Tropius',
'Chimecho',
'Absol',
'Glalie',
'Walrein',
'Huntail',
'Gorebyss',
'Relicanth',
'Luvdisc',
'Salamence',
'Metagross',
'Regirock',
'Regice',
'Registeel',
'Latias',
'Latios',
'Kyogre',
'Groudon',
'Rayquaza',
'Jirachi',
'Deoxys',
'Torterra',
'Infernape',
'Empoleon',
'Staraptor',
'Bibarel',
'Kricketune',
'Luxray',
'Roserade',
'Rampardos',
'Bastiodon',
'Wormadam',
'Mothim',
'Vespiquen',
'Pachirisu',
'Floatzel',
'Cherrim',
'Gastrodon',
'Ambipom',
'Drifblim',
'Lopunny',
'Mismagius',
'Honchkrow',
'Purugly',
'Skuntank',
'Bronzong',
'Chatot',
'Spiritomb',
'Garchomp',
'Lucario',
'Hippowdon',
'Drapion',
'Toxicroak',
'Carnivine',
'Lumineon',
'Abomasnow',
'Weavile',
'Magnezone',
'Lickilicky',
'Rhyperior',
'Tangrowth',
'Electivire',
'Magmortar',
'Togekiss',
'Yanmega',
'Leafeon',
'Glaceon',
'Gliscor',
'Mamoswine',
'Porygon',
'Gallade',
'Probopass',
'Dusknoir',
'Froslass',
'Rotom',
'Uxie',
'Mesprit',
'Azelf',
'Dialga',
'Palkia',
'Heatran',
'Regigigas',
'Giratina',
'Giratina',
'Cresselia',
'Phione',
'Manaphy',
'Darkrai',
'Shaymin',
'Shaymin',
'Arceus',
'Victini',
'Serperior',
'Emboar',
'Samurott',
'Watchog',
'Stoutland',
'Liepard',
'Simisage',
'Simisear',
'Simipour',
'Musharna',
'Unfezant',
'Zebstrika',
'Gigalith',
'Swoobat',
'Excadrill',
'Audino',
'Audino',
'Conkeldurr',
'Seismitoad',
'Throh',
'Sawk',
'Leavanny',
'Scolipede',
'Whimsicott',
'Lilligant',
'Basculin',
'Krookodile',
'Darmanitan',
'Maractus',
'Crustle',
'Scrafty',
'Sigilyph',
'Cofagrigus',
'Carracosta',
'Archeops',
'Garbodor',
'Zoroark',
'Cinccino',
'Gothitelle',
'Reuniclus',
'Swanna',
'Vanilluxe',
'Sawsbuck',
'Emolga',
'Escavalier',
'Amoonguss',
'Jellicent',
'Alomomola',
'Galvantula',
'Ferrothorn',
'Klinklang',
'Eelektross',
'Beheeyem',
'Chandelure',
'Haxorus',
'Beartic',
'Cryogonal',
'Accelgor',
'Stunfisk',
'Mienshao',
'Druddigon',
'Golurk',
'Bisharp',
'Bouffalant',
'Braviary',
'Mandibuzz',
'Heatmor',
'Durant',
'Hydreigon',
'Volcarona',
'Cobalion',
'Terrakion',
'Virizion',
'Tornadus',
'Thundurus',
'Reshiram',
'Zekrom',
'Landorus',
'Kyurem',
'Keldeo',
'Meloetta',
'Genesect',
'Chesnaught',
'Delphox',
'Greninja',
'Diggersby',
'Talonflame',
'Vivillon',
'Pyroar',
'Florges',
'Gogoat',
'Pangoro',
'Furfrou',
'Meowstic',
'Aegislash',
'Aromatisse',
'Slurpuff',
'Malamar',
'Barbaracle',
'Dragalge',
'Clawitzer',
'Heliolisk',
'Tyrantrum',
'Aurorus',
'Sylveon',
'Hawlucha',
'Dedenne',
'Carbink',
'Goodra',
'Klefki',
'Trevenant',
'Gourgeist',
'Avalugg',
'Noivern',
'Xerneas',
'Yveltal',
'Zygarde',
'Diancie',
'Hoopa',
'Volcanion',
'Decidueye',
'Incineroar',
'Primarina',
'Toucannon',
'Gumshoos',
'Vikavolt',
'Crabominable',
'Oricorio',
'Ribombee',
'Lycanroc',
'Wishiwashi',
'Toxapex',
'Mudsdale',
'Araquanid',
'Lurantis',
'Shiinotic',
'Salazzle',
'Bewear',
'Tsareena',
'Comfey',
'Oranguru',
'Passimian',
'Golisopod',
'Palossand',
'Pyukumuku',
'Silvally',
'Minior',
'Komala',
'Turtonator',
'Togedemaru',
'Mimikyu',
'Bruxish',
'Drampa',
'Dhelmise',
'Kommo',
'Tapu',
'Solgaleo',
'Lunala',
'Nihilego',
'Buzzwole',
'Pheromosa',
'Xurkitree',
'Celesteela',
'Kartana',
'Guzzlord',
'Necrozma',
'Magearna',
'Marshadow',
'Naganadel',
'Stakataka',
'Blacephalon',
'Zeraora',
'Melmetal',
'Rillaboom',
'Cinderace',
'Inteleon',
'Greedent',
'Corviknight',
'Orbeetle',
'Thievul',
'Eldegoss',
'Dubwool',
'Drednaw',
'Boltund',
'Coalossal',
'Flapple',
'Appletun',
'Sandaconda',
'Cramorant',
'Barraskewda',
'Toxtricity',
'Centiskorch',
'Grapploct',
'Polteageist',
'Hatterene',
'Grimmsnarl',
'Obstagoon',
'Perrserker',
'Cursola',
'Sirfetch',
'Mr',
'Runerigus',
'Alcremie',
'Falinks',
'Pincurchin',
'Frosmoth',
'Stonjourner',
'Eiscue',
'Indeedee',
'Morpeko',
'Copperajah',
'Dracozolt',
'Arctozolt',
'Dracovish',
'Arctovish',
'Duraludon',
'Dragapult',
'Zacian',
'Zamazenta',
'Eternatus',
'Urshifu',
'Zarude',
'Regieleki',
'Regidrago',
'Glastrier',
'Spectrier',
'Calyrex'
]

with open('egg_groups.json') as eggless:
    temp_mons = json.load(eggless)
    eggless_mons = [mon['name'] for mon in temp_mons['pokemon_species']]

with open('pokemon.csv') as mons:
    diction = csv.DictReader(mons)
    # get rid of pokemon in the unidentified egg group. They can't breed. Yes this includes baby pokemon, but they'll be caught by their regular forms.
    # Get rid of ghosts too. I'm not about that. Fight me.
    mons = [pokemon for pokemon in diction if pokemon['name'] in fully_evolved_mons and pokemon['name'].lower() not in eggless_mons and pokemon['type1'] != 'ghost' and pokemon['type2'] != 'ghost' ]

# Adding in extra fields for pet valuations
for mon in mons:
    # Cast ints into ints
    mon['against_bug'] = float(mon['against_bug'])
    mon['against_dragon'] = float(mon['against_dragon'])
    mon['against_electric'] = float(mon['against_electric'])
    mon['against_fairy'] = float(mon['against_fairy'])
    mon['against_fight'] = float(mon['against_fight'])
    mon['against_fire'] = float(mon['against_fire'])
    mon['against_flying'] = float(mon['against_flying'])
    mon['against_ghost'] = float(mon['against_ghost'])
    mon['against_grass'] = float(mon['against_grass'])
    mon['against_ground'] = float(mon['against_ground'])
    mon['against_ice'] = float(mon['against_ice'])
    mon['against_normal'] = float(mon['against_normal'])
    mon['against_poison'] = float(mon['against_poison'])
    mon['against_psychic'] = float(mon['against_psychic'])
    mon['against_rock'] = float(mon['against_rock'])
    mon['against_steel'] = float(mon['against_steel'])
    mon['against_water'] = float(mon['against_water'])

    mon['attack'] = int(mon['attack'])
    mon['defense'] = int(mon['defense'])
    mon['sp_attack'] = int(mon['sp_attack'])
    mon['sp_defense'] = int(mon['sp_defense'])
    mon['hp'] = int(mon['hp'])
    mon['speed'] = int(mon['speed'])

    if len(mon['height_m']):
        mon['height_m'] = float(mon['height_m'])
    else:
        mon['height_m'] = 0
    if len(mon['weight_kg']):
        mon['weight_kg'] = float(mon['weight_kg'])
    else:
        mon['weight_kg'] = 0
    if len(mon['percentage_male']):
        mon['percentage_male'] = float(mon['percentage_male'])
    else:
        mon['percentage_male'] = 50 
    mon['pokedex_number'] = int(mon['pokedex_number'])
    mon['generation'] = int(mon['generation'])
    mon['is_legendary'] = not bool(mon['generation'])

    mon['base_egg_steps'] = int(mon['base_egg_steps'])
    mon['base_happiness'] = int(mon['base_happiness'])
    mon['capture_rate'] = int(mon['capture_rate'])
    mon['base_total'] = int(mon['base_total'])
    mon['experience_growth'] = int(mon['experience_growth'])
    
    # from PokemonDB stat combos, for determining danger to humans
    mon['type_danger'] = mon['against_normal']
    mon['sweeper_stat'] = max(mon['attack'], mon['sp_attack']) + mon['speed']
    mon['wall_stat'] = mon['hp'] + mon['defense'] + mon['sp_defense']
    mon['sp_tank_stat'] = mon['sp_attack'] + mon['sp_defense']
    mon['tank_stat'] = mon['attack'] + mon['defense']
    
    mon['bmr'] = (10.0 * mon['weight_kg']) + (6.25 * mon['height_m']*100) - 161 + mon['percentage_male']/100.0 * 166
    if mon['type1'] == 'fire' or mon['type2'] == 'fire':
        mon['bmr'] *= 4.0
    if mon['type1'] == 'electric' or mon['type2'] == 'electric':
        mon['bmr'] *= 2.0
    if mon['type1'] == 'ice' or mon['type2'] == 'ice':
        mon['bmr'] *= 0.25

too_big = [pokemon for pokemon in mons if pokemon['height_m'] > 1.6]
mons = [pokemon for pokemon in mons if pokemon['height_m'] <= 1.6]

# Normalize the data
stats_to_normalize = ['sweeper_stat', 'experience_growth', 'speed', 'base_happiness', 'type_danger', 'bmr', 'capture_rate', 'base_egg_steps']
def _calculateMedians(pokemon):
    medians = {}
    for stat in stats_to_normalize:
        orderedMons = sorted(pokemon, key=lambda mon: mon[stat])
        middle = float(len(orderedMons))/2
        if middle % 2 != 0:
            medians[stat] = (orderedMons[int(middle - 0.5)][stat])
        else:
            medians[stat] = (
                float(orderedMons[int(middle)][stat] +
                      orderedPlayers[int(middle-1)][stat])/2)

    return medians

def _calculateStdDevs(pokemon, medians):
    deviations = {}

    for stat in stats_to_normalize:
        runningTotal = 0
        for mon in pokemon:
            runningTotal+= (mon[stat] - medians[stat]) **2
        deviations[stat] = (sqrt(runningTotal/len(pokemon)))
    return deviations

def _centerPokemon(pokemon, medians, sdevs):
    for stat in stats_to_normalize:
        for mon in pokemon:
            mon['c_'+stat] = (mon[stat] - medians[stat])/sdevs[stat]
    return pokemon

medians = _calculateMedians(mons)
sdevs = _calculateStdDevs(mons, medians)
normalizedPokes = _centerPokemon(mons, medians, sdevs)

# Calculate the final results
for mon in mons:
    exercise_needs = (mon['c_speed'] + mon['c_experience_growth'])/2

    mon['pet_suitability'] = (mon['c_sweeper_stat'] + mon['c_type_danger'] + exercise_needs + -mon['c_base_happiness'] + mon['c_bmr'] + -mon['c_capture_rate'])/6
# Use the against_normal, against_fighting, and against_psychic traits to determine our danger to them, generally?

mons.sort(key=lambda mon: mon['pet_suitability'])
print("%s: %s" % (mons[0]['name'], mons[0]['pet_suitability']))
print("%s: %s" % (mons[-1]['name'], mons[-1]['pet_suitability']))
names = [mon['name'] for mon in mons]
print(names)
