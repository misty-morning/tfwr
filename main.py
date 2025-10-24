field_height = get_world_size()

field_map = [
	[
		Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, 
	]
]

def moiser(water):
	if water and get_water() < 0.9:
		use_item(Items.Water)

def handle_hay(i, water, fertilize):
	moiser(water)
	if can_harvest():
		harvest()

def handle_carrot(i, water, fertilize):
	moiser(water)
	gt = get_ground_type()
	if can_harvest():
		harvest()
		if gt != Grounds.Soil:
				till()
		plant(Entities.Carrot)
	elif gt == Grounds.Soil:
		plant(Entities.Carrot)
		if fertilize:
			use_item(Items.Fertilizer)
		
def handle_pumpkin(i, water, fertilize):
	moiser(water)
	if can_harvest():
		harvest()

		# if get_entity_type() == Entities.Pumpkin:
		# 	print(measure(South))
		# 	if measure() > 3:
		# 		harvest()
		# 	print("no harvest")
		# else:
		# 	harvest()
		
		
	if get_ground_type() != Grounds.Soil:
			till()

	if get_ground_type() == Grounds.Soil:
		plant(Entities.Pumpkin)
		if fertilize:
			use_item(Items.Fertilizer)

def handle_bush(i, water, fertilize):
	moiser(water)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
		
def handle_trees(i, water, fertilize):
	# moiser(water)
	if can_harvest():
		harvest()
	if (i % 2) != 0:
		plant(Entities.Tree)
		if water:
			use_item(Items.Water)
		if fertilize:
			use_item(Items.Fertilizer)

def handle_row(action, vertical_way, horizontal_way, water, fertilize):
	for i in range(field_height):
		#print("handle row", i)
		action(i, water, fertilize)
		if i != (field_height - 1):
			move(vertical_way)
		else:
			move(horizontal_way)

clear()

change_hat(Hats.Wizard_Hat)

while True:
	
#main route
	handle_row(handle_pumpkin, North, East, True, True)
	
	handle_row(handle_pumpkin, South, East, True, True)
	
	handle_row(handle_pumpkin, North, East, True, True)
	
	handle_row(handle_pumpkin, South, East, True, True)
	
	handle_row(handle_carrot, North, East, True, False)
	
	handle_row(handle_trees, South, East, True, False)
	
	handle_row(handle_carrot, North, East, True, False)
	
	handle_row(handle_trees, South, East, True, False)

	handle_row(handle_carrot, North, East, True, False)
	
	handle_row(handle_trees, South, East, True, False)
	
	handle_row(handle_carrot, North, East, True, False)
	
	handle_row(handle_trees, South, East, True, False)
	

	#return route

	#move(East)

	#move(North)

	
	

