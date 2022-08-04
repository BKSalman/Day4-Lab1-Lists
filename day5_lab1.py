list = [5, 4, 17, 19, 30, 2, 7, 10, 45]

count = 0
largest = 0

for item in list:
		count += item
		if item > largest:
				largest = item

even_numbers = [item for item in list if item % 2 == 0]

sliced_list = list[:5] # if "element" meant as "index" this will be [:6]

print(f"count: {count} largest: {largest} even numbers: {even_numbers} sliced list: {sliced_list}")
