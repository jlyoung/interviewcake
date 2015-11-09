def get_products_of_all_ints_except_at_index(intlist):
	results = []
	for idx, val in enumerate(intlist):
		results.append(reduce(lambda x,y: x*y, intlist[:idx], 1) * reduce(lambda x,y: x*y, intlist[idx+1:], 1))
	return results

intlist = [1, 7, 3, 4]
print get_products_of_all_ints_except_at_index(intlist)

intlist = [1, 0, 3, 4]
print get_products_of_all_ints_except_at_index(intlist)