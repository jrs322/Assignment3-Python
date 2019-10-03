def store_checkout(inventory_tuple_list, item_purchase_list):
    product_price_dict = {}
    total_price = 0
    if(len(inventory_tuple_list) != 0):
        for this_tuple in inventory_tuple_list:
            #print(this_tuple)
            name = this_tuple[0]
            #print(name)
            price = this_tuple[1]
            #print(price)
            product_price_dict.update({name:price})
        #print(product_price_dict)   
        if (len(item_purchase_list) != 0):
            for product in item_purchase_list:
                total_price = total_price + int(product_price_dict.get(product, 0))
        return total_price
    else:
        print("Invalid list len")
        return 0
    
def highest_frequency_count(item_list):
    count_dict = {}
    max_count = 0
    if (len(item_list) != 0):
        for item in item_list:
            found_item = count_dict.get(item, -1)
            print(found_item)
            if found_item == -1:
                count_dict.update({item: 1})
                if (1 > max_count):
                    max_count = 1
            else:
                prev_count = found_item
                prev_count = prev_count + 1
                if prev_count > max_count:
                    max_count = prev_count
                #print(str(item) + " , " + str(found_item))
                count_dict.update({str(item):prev_count})
        #print(count_dict)
        return max_count
    else:
        print("Empty List")
        return 0
        
