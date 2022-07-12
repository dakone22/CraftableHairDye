COLORS = [
    # dye_name, dye_id, paint_id
    ("Blonde", "Blonde", "Brown"),
    ("Black", "Black", "Black"),
    ("White", "White", "White"),
    ("Pink", "Pink", "Pink"),
    ("Yellow", "Yellow", "Yellow"),
    ("Red", "Red", "Red"),
    ("Strawberry Blonde", "Ginger", "Orange"),
    ("Light Brown", "LightBrown", "LightBrown"),
    ("Green", "Green", "Green"),
    ("Blue", "Blue", "Blue"),
]

FORMAT = """
    recipe Make{dye_name}HairDye
    {{
        Paint{paint_id}=2,
        Water=2,
        destroy WaterBottleEmpty/PopBottleEmpty/WhiskeyEmpty/BeerEmpty/WineEmpty2/RemouladeEmpty/MayonnaiseEmpty,

        Result:HairDye{dye_id},
        Time:30.0,
        NeedToBeLearn:False,
        AnimMode:Craft,
        Sound:MakePlaster,
    }}
"""

TRANSLATE_FORMAT = """    Recipe_Make{dye_name}HairDye = "Make {dye_name2} Hair Dye","""


for dye_name, dye_id, paint_id in COLORS:
    print(FORMAT.format(dye_name=dye_name.replace(' ', ''), dye_id=dye_id, paint_id=paint_id))

for dye_name, dye_id, paint_id in COLORS:
    print(TRANSLATE_FORMAT.format(dye_name=dye_name.replace(' ', ''), dye_name2=dye_name))
