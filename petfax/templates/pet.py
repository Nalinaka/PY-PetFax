from flask import (Blueprint, render_template)
import json 

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)


@bp.route('/<int:index>')
def show_pet (index): 
        return render_template('pets/index.html', pets=pets)


@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)




#below code did not work - my solution for this section:

# def index():
#     if index:
#         print(index)
#         newpet={}
#         for pet in pets:
#             if pet['pet_id'] == index:
#                 newpet = pet
#             print(newpet)

#     return render_template('showpet.html', pet=pets)




    # if id:
    #     print(id)
    #     newpet={}
    #     for pet in pets:
    #         if pet['pet_id'] == int(id):
    #             newpet = pet
    #         print(newpet)

    #     return render_template('showpet.html', pet=newpet)
    # else:
    #     return render_template('index.html', pets=pets)
    

    #     pet = [p for p in pets if p['pet_id'] == int(id)]
    #     return(id)
    #     #
    # return render_template('showpet.html', pet=pet[0])

    # return render_template('index.html', pets=pets)




