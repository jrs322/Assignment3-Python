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
        
