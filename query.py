"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter(Brand.brand_id == 'ram').all()
# Answer: [<Brand brand_id=ram name=Rambler>]

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che')
"""Answer:
[<Model model_id=5 name=Corvette>,
 <Model model_id=6 name=Corvette>,
 <Model model_id=8 name=Corvette>,
 <Model model_id=10 name=Corvette>,
 <Model model_id=11 name=Corvette>,
 <Model model_id=13 name=Corvette>,
 <Model model_id=17 name=Corvette>,
 <Model model_id=20 name=Corvette>,
 <Model model_id=25 name=Corvette>,
 <Model model_id=27 name=Corvette>,
 <Model model_id=37 name=Corvette>,
 <Model model_id=38 name=Corvette>] """

# Get all models that are older than 1960.
q3 = db.session.query(Model).filter(Model.year > 1960).all() 
"""Answer:

[<Model model_id=22 name=Mini Cooper>,
 <Model model_id=23 name=Avanti>,
 <Model model_id=24 name=Tempest>,
 <Model model_id=25 name=Corvette>,
 <Model model_id=26 name=Grand Prix>,
 <Model model_id=27 name=Corvette>,
 <Model model_id=28 name=Avanti>,
 <Model model_id=29 name=Special>,
 <Model model_id=30 name=Mini>,
 <Model model_id=31 name=Mini Cooper S>,
 <Model model_id=32 name=Classic>,
 <Model model_id=33 name=E-Series>,
 <Model model_id=34 name=Avanti>,
 <Model model_id=35 name=Grand Prix>,
 <Model model_id=36 name=Corvair 500>,
 <Model model_id=37 name=Corvette>,
 <Model model_id=38 name=Corvette>,
 <Model model_id=39 name=Mustang>,
 <Model model_id=40 name=Galaxie>,
 <Model model_id=41 name=LeMans>,
 <Model model_id=42 name=Bonneville>,
 <Model model_id=43 name=Grand Prix>,
 <Model model_id=44 name=Fury>,
 <Model model_id=45 name=Avanti>,
 <Model model_id=46 name=Mini Cooper>,
 <Model model_id=47 name=Malibu>,
 <Model model_id=48 name=Outback>] """

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued != None)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all() 



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = Model.query.filter(Model.year == year).all()

    if models:
        for model in models:
            print(f'{model.name} {model.brand.name} {model.brand.headquarters}') 
            print()
    else:
        print("No models from that year in the database\n")

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    all_brands = Brand.query.all()

    for brand in all_brands:
        print(f'Brand: {brand.name}')
        if brand.models:
            for model in brand.models:
                print(f'Model: {model.name} {model.year}')
        else:
            print("None")
    print()

def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    all_brands = Brand.query.filter(Brand.name.ilike('%'+mystr+'%')).all()

    print(all_brands)

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass

