field_height = 6

def handle_hay():
	if can_harvest():
		harvest()

def handle_carrot():
	gt = get_ground_type()
	if can_harvest():
		harvest()
		if gt != Grounds.Soil:
				till()
		plant(Entities.Carrot)
	elif gt == Grounds.Soil:
		plant(Entities.Carrot)
		
def handle_pumpkin():
	gt = get_ground_type()
	if can_harvest():
		harvest()
		if gt != Grounds.Soil:
				till()
		plant(Entities.Pumpkin)
	elif gt == Grounds.Soil:
		plant(Entities.Pumpkin)

def handle_bush():
	if can_harvest():
		harvest()
		plant(Entities.Bush)
		
def handle_row(action, vertical_way, horizontal_way):
	for i in range(field_height):
		#print("handle row", i)
		action()
		if i != (field_height - 1):
			move(vertical_way)
		else:
			move(horizontal_way)
			

	

def handle_tree_row(_, vertical_way, horizontal_way, water):
	for i in range(field_height):
		if can_harvest():
			harvest()
		if (i % 2) != 0:
			plant(Entities.Tree)
			if water:
				use_item(Items.Water)
				use_item(Items.Fertilizer)
	
		if i != (field_height - 1):
			move(vertical_way)
		else:
			move(horizontal_way)
			

clear()

while True:
	
#main route
	handle_row(handle_pumpkin, North, East)
	
	handle_row(handle_pumpkin, South, East)
	
	handle_row(handle_pumpkin, North, East)
	
	handle_tree_row(handle_carrot, South, East, True)
	
	handle_row(handle_carrot, North, East)
	
	handle_tree_row(handle_hay, South, East, True)

	#return route

	#move(East)

	#move(North)

	
	

