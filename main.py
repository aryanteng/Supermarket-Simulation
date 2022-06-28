def show_menu():
   return '''=================================================
                   MY BAZAAR
=================================================
Hello! Welcome to my grocery store!
Following are the products available in the shop:

-------------------------------------------------
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
  0  | T-shirt     | Apparels     | 500
  1  | Trousers    | Apparels     | 600
  2  | Scarf       | Apparels     | 250
  3  | Smartphone  | Electronics  | 20,000
  4  | iPad        | Electronics  | 30,000
  5  | Laptop      | Electronics  | 50,000
  6  | Eggs        | Eatables     | 5
  7  | Chocolate   | Eatables     | 10
  8  | Juice       | Eatables     | 100
  9  | Milk        | Eatables     | 45
------------------------------------------------
'''


def get_regular_input():
    print('''
-------------------------------------------------
ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------''')
    regular_input = input('Enter the item codes (space-separated): ')
    regular_input_list = regular_input.split()
    regular_input_quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(regular_input_list)):
        if regular_input_list[i] == '0':
            regular_input_quantities[0] += 1
        elif regular_input_list[i] == '1':
            regular_input_quantities[1] += 1
        elif regular_input_list[i] == '2':
            regular_input_quantities[2] += 1
        elif regular_input_list[i] == '3':
            regular_input_quantities[3] += 1
        elif regular_input_list[i] == '4':
            regular_input_quantities[4] += 1
        elif regular_input_list[i] == '5':
            regular_input_quantities[5] += 1
        elif regular_input_list[i] == '6':
            regular_input_quantities[6] += 1
        elif regular_input_list[i] == '7':
            regular_input_quantities[7] += 1
        elif regular_input_list[i] == '8':
            regular_input_quantities[8] += 1
        elif regular_input_list[i] == '9':
            regular_input_quantities[9] += 1

    return regular_input_quantities


def get_bulk_input():
    print('''
-------------------------------------------------
ENTER ITEM AND QUANTITIES
-------------------------------------------------''')
    bulk_input_list = []
    while True:
        bulk_input = input('Enter code and quantity (leave blank to stop): ')
        bulk_input_list += bulk_input.split()

        if bulk_input == '':
            print('Your order has been finalized.')
            break

        if bulk_input[0] == "0" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added", bulk_input[2:10:1], "T-shirts")
        elif bulk_input[0] == "1" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added", bulk_input[2:10:1], "Trousers")
        elif bulk_input[0] == "2" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added", bulk_input[2:10:1], "Scarf")
        elif bulk_input[0] == "3" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added" ,bulk_input[2:10:1], "Smartphone")
        elif bulk_input[0] =="4" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added" ,bulk_input[2:10:1],"iPad")
        elif bulk_input[0] =="5" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added" ,bulk_input[2:10:1],"Laptop")
        elif bulk_input[0] =="6" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added" ,bulk_input[2:10:1],"Eggs")
        elif bulk_input[0] =="7" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added" ,bulk_input[2:10:1],"Chocolate")
        elif bulk_input[0] =="8" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added" ,bulk_input[2:10:1],"Juice")
        elif bulk_input[0] =="9" and bulk_input[2] != "-" and bulk_input[2] != "0" and bulk_input[1] != 0:
            print("You added" ,bulk_input[2:10:1],"Milk")

        elif bulk_input[0] != '0' and bulk_input[0] != '1' and bulk_input[0] != '2' and bulk_input[0] != '3' and bulk_input[0] != '4' and bulk_input[0] != '5' and bulk_input[0] != '6' and bulk_input [0] != '7' and bulk_input [0] != '8' and bulk_input [0] != '9' and bulk_input[2] != '-' or bulk_input[2] != '0':
            print("Invalid Code. Try Again")

        elif bulk_input[2] == '-' or bulk_input[2] == '0':
            print("Invalid quantity.  Try Again")

        else:
            print("Invalid code and quantity. Try Again")


    bulk_input_quantites = [0,0,0,0,0,0,0,0,0,0]

    bulk_input_list = [int(i) for i in bulk_input_list]

    for i in range(0,len(bulk_input_list),2):
        if bulk_input_list[i]==0:
            bulk_input_quantites[0] += bulk_input_list[i+1]
        if bulk_input_list[i]==1:
            bulk_input_quantites[1] += bulk_input_list[i+1]
        if bulk_input_list[i]==2:
            bulk_input_quantites[2] += bulk_input_list[i+1]
        if bulk_input_list[i]==3:
            bulk_input_quantites[3] += bulk_input_list[i+1]
        if bulk_input_list[i]==4:
            bulk_input_quantites[4] += bulk_input_list[i+1]
        if bulk_input_list[i]==5:
            bulk_input_quantites[5] += bulk_input_list[i+1]
        if bulk_input_list[i]==6:
            bulk_input_quantites[6] += bulk_input_list[i+1]
        if bulk_input_list[i]==7:
            bulk_input_quantites[7] += bulk_input_list[i+1]
        if bulk_input_list[i]==8:
            bulk_input_quantites[8] += bulk_input_list[i+1]
        if bulk_input_list[i]==9:
            bulk_input_quantites[9] += bulk_input_list[i+1]

    return bulk_input_quantites


def print_order_details(quantities):
    print('''

-------------------------------------------------
ORDER DETAILS
-------------------------------------------------''')
    n = 1
    if quantities[0] > 0:
        print('[',n,'] T-shirt x ',quantities[0],' = Rs 500 *',quantities[0],'=',quantities[0]*500)
        n += 1
    if quantities[1] > 0:
        print('[',n,'] Trousers x ',quantities[1],' = Rs 600 * ',quantities[1], ' = Rs', quantities[1]*600)
        n += 1
    if quantities[2] > 0:
        print('[', n, ']', ' Scarf x ',quantities[2], '= Rs 250 * ',quantities[2], ' = Rs',quantities[2]*250)
        n += 1
    if quantities[3] > 0:
        print('[', n, ']', ' Smartphone x ',quantities[3], '= Rs 20000 * ',quantities[3], ' = Rs',quantities[3]*20000)
        n += 1
    if quantities[4] > 0:
        print('[', n, ']', ' iPad x ',quantities[4], '= Rs 30000 * ',quantities[4], ' = Rs', quantities[4]*30000)
        n += 1
    if quantities[5] > 0:
        print('[', n, ']', ' Laptop x ',quantities[5], '= Rs 50000 * ',quantities[5], ' = Rs', quantities[5]*50000)
        n += 1
    if quantities[6] > 0:
        print('[', n, ']', ' Eggs x ',quantities[6], '= Rs 5 * ',quantities[6], ' = Rs', quantities[6]*5)
        n += 1
    if quantities[7] > 0:
        print('[', n, ']', ' Chocolate x ',quantities[7], '= Rs 10 * ',quantities[7], ' = Rs', quantities[7]*10)
        n += 1
    if quantities[8] > 0:
        print('[', n, ']', ' Juice x ',quantities[8], '= Rs 100 * ',quantities[8], ' = Rs', quantities[8]*100)
        n += 1
    if quantities[9] > 0:
        print('[', n, ']', ' Milk x ',quantities[9], '= Rs 45 * ',quantities[9], ' = Rs', quantities[9]*45)
        n += 1


def calculate_category_wise_cost(quantities):
    print('''
-------------------------------------------------
CATEGORY-WISE COST
-------------------------------------------------''')
    apparels_cost = 0
    electronics_cost = 0
    eatables_cost = 0
    if quantities[0] > 0 or quantities[1] > 0 or quantities[2] > 0:
        apparels_cost = int(500*quantities[0] + 600*quantities[1] + 250*quantities[2])
    if quantities[3] > 0 or quantities[4] > 0 or quantities[5] > 0:
        electronics_cost = int(20000*quantities[3] + 30000*quantities[4] + 50000*quantities[5])
    if quantities[6] > 0 or quantities[7] > 0 or quantities[8] > 0 or quantities[9] > 0:
        eatables_cost = int(5*quantities[6] + 10*quantities[7] + 100*quantities[8] + 45*quantities[9])

    category_wise_cost = (apparels_cost, electronics_cost, eatables_cost)
    return category_wise_cost


def get_discount(cost, discount_rate):
    return int(cost*discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print('''
-------------------------------------------------
DISCOUNTS
-------------------------------------------------''')
    apparels_discount_cost=0
    apparels_discount=0
    electronics_discount_cost=0
    electronics_discount=0
    eatables_discount_cost=0
    eatables_discount=0
    if apparels_cost >= 2000:
        apparels_discount=get_discount(apparels_cost, 0.10)
        apparels_discount_cost=apparels_cost-apparels_discount
    if electronics_cost >= 25000:
        electronics_discount = get_discount(electronics_cost,0.10)
        electronics_discount_cost=electronics_cost-electronics_discount
    if eatables_cost >= 500:
        eatbles_discount = get_discount(eatables_cost,0.10)
        eatables_discount_cost= eatables_cost-eatbles_discount
    total_discount = (apparels_discount_cost, electronics_discount_cost, eatables_discount_cost)
    return total_discount


def get_tax(cost, tax):
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    print('''
-------------------------------------------------
TAX
-------------------------------------------------''')
    apparels_tax = 0
    electronics_tax = 0
    eatables_tax = 0

    if apparels_cost > 0:
        apparels_tax = get_tax(apparels_cost, 0.10)
        print('[APPAREL] ', f'{apparels_cost} * 0.10 = Rs ', apparels_tax)

    if electronics_cost > 0:
        electronics_tax = get_tax(electronics_cost, 0.15)
        print('[ELECTRONICS] ', f'{electronics_cost} * 0.15 = Rs ', electronics_tax)
    if eatables_cost > 0:
        eatables_tax = get_tax(eatables_cost,0.05)
        print('[EATABLES] ', f'{eatables_cost} * 0.05 = Rs ',eatables_tax)

    total_tax = apparels_tax + electronics_tax + eatables_tax
    total_cost = apparels_cost+electronics_cost+eatables_cost

    total_cost_including_tax = total_cost+total_tax

    tax = (total_cost_including_tax, total_tax)
    return tax


def apply_coupon_code(total_cost):
    print('''
-------------------------------------------------
COUPON CODE
-------------------------------------------------''')
    tag = 0
    while tag == 0:
        coupon_code = input('Enter coupon code (else leave blank): ')
        if coupon_code == 'CHILL50' and total_cost >= 50000:
            total_coupon_discount = total_cost * 0.50
            if total_coupon_discount > 10000:
                total_coupon_discount = 10000
            total_cost_after_coupon_discount = total_cost - total_coupon_discount
            print(f'[CHILL50] min(10000,{total_cost} * 0.50) =', total_coupon_discount)
            coupon = (total_cost_after_coupon_discount, total_coupon_discount)
            tag += 1
        elif coupon_code == 'HELLE25' and total_cost >= 25000:
            total_coupon_discount = total_cost * 0.25
            if total_coupon_discount > 5000:
                total_coupon_discount = 5000
            total_cost_after_coupon_discount = total_cost - total_coupon_discount
            print(f'[HELLE25] min(5000,{total_cost} * 0.25) =', total_coupon_discount)
            coupon = (total_cost_after_coupon_discount,total_coupon_discount)
            tag += 1
        elif coupon_code == "":
            total_cost_after_coupon_discount = total_cost
            total_coupon_discount = 0

            coupon = (total_cost_after_coupon_discount, total_coupon_discount)
            tag += 1
        else:
            print('Invalid coupon code. Try again.')
    return coupon


def main():
    print(show_menu())
    tag = 0
    while tag == 0:
        user_input = input('Would you like to buy in bulk? (y or Y / n or N): ')
        if user_input.upper() == 'Y':
            bulk_input_quantities = get_bulk_input()

            print_order_details(bulk_input_quantities)

            apparels_cost,electronics_cost,eatables_cost=calculate_category_wise_cost(bulk_input_quantities)

            if apparels_cost > 0:
                print("Apparels = Rs", apparels_cost)
            if electronics_cost > 0:
                print("Electronics= Rs", electronics_cost)
            if eatables_cost > 0:
                print("Eatables= Rs", eatables_cost)

            apparels_discount_cost, electronics_discount_cost,eatables_discount_cost=calculate_discounted_prices(apparels_cost,electronics_cost,eatables_cost)
            total_cost=apparels_cost+eatables_cost+electronics_cost
            total_discount = 0
            if apparels_cost >= 2000:
                total_cost=apparels_discount_cost
                apparels_discount=apparels_cost-apparels_discount_cost
                total_discount = apparels_discount
                print('[APPAREL] ', f'Rs {apparels_cost} - Rs {apparels_discount} = ','Rs ',apparels_discount_cost)

                if apparels_cost >= 2000 and electronics_cost >= 25000:
                    total_cost=apparels_discount_cost+electronics_discount_cost
                    electronics_discount=electronics_cost-electronics_discount_cost
                    total_discount = apparels_discount+electronics_discount
                    print('[ELECTRONICS] ',f'Rs{electronics_cost} - Rs{electronics_discount} = ','Rs ',electronics_discount_cost)

                    if apparels_cost >= 2000 and electronics_cost >= 25000 and eatables_cost >= 500:
                        total_cost =apparels_discount_cost+electronics_discount_cost+eatables_discount_cost
                        eatables_discount=eatables_cost-eatables_discount_cost
                        total_discount = apparels_discount+eatables_discount+electronics_discount
                        print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)

                elif apparels_cost >= 2000 and eatables_cost >= 500:
                    eatables_discount=eatables_cost-eatables_discount_cost
                    total_discount = apparels_discount+eatables_discount
                    print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)
                    total_cost =eatables_discount_cost+apparels_discount_cost

            elif electronics_cost >=25000:
                total_cost=electronics_discount_cost
                electronics_discount=electronics_cost-electronics_discount_cost
                print('[ELECTRONICS] ',f'Rs{electronics_cost} - Rs{electronics_discount} = ','Rs ',electronics_discount_cost)
                total_discount = electronics_discount
                if electronics_cost >=  25000 and eatables_cost >= 500:
                    eatables_discount=eatables_cost-eatables_discount_cost
                    print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)
                    total_discount = eatables_discount+electronics_discount
                    total_cost = electronics_discount_cost+eatables_discount_cost
            elif eatables_cost >= 500:
                eatables_discount=eatables_cost-eatables_discount_cost
                print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)
                total_cost=eatables_discount_cost
                total_discount = eatables_discount






            if total_discount>0:
                print('TOTAL DISCOUNT = Rs ', total_discount)
                print('TOTAL COST = Rs ',total_cost)
                total_cost_including_tax,total_tax = calculate_tax(apparels_discount_cost,electronics_discount_cost,eatables_discount_cost)
                print("TOTAL TAX = Rs ",total_tax)
                print("TOTAL COST = Rs ",total_cost_including_tax)
            else:
                print('TOTAL DISCOUNT = Rs 0')
                print("TOTAL COST = Rs",total_cost)

                total_cost_including_tax,total_tax =calculate_tax(apparels_cost, electronics_cost, eatables_cost)
                print("TOTAL TAX = Rs ",total_tax)
                print("TOTAL COST = Rs ",total_cost_including_tax)


            total_cost_after_coupon_discount,total_coupon_discount=apply_coupon_code(total_cost_including_tax)

            if total_coupon_discount > 0:
                print("TOTAL COUPON DISCOUNT = Rs",total_coupon_discount)
                print("TOTAL COST = Rs" ,total_cost_after_coupon_discount)
            else:
                print("TOTAL COUPON DISCOUNT = Rs 0")
                print("TOTAL COST = Rs" ,total_cost_after_coupon_discount)
                print("Thank you for visiting!")


            tag += 1
        elif user_input.upper() == 'N':
            regular_input_quantities = get_regular_input()

            print_order_details(regular_input_quantities)

            apparels_cost,electronics_cost,eatables_cost=calculate_category_wise_cost(regular_input_quantities)

            if apparels_cost>0:
                print("Apparels = Rs",apparels_cost)
            if electronics_cost>0:
                print("Electronics= Rs",electronics_cost)
            if eatables_cost>0:
                print("Eatables= Rs",eatables_cost)

            apparels_discount_cost,electronics_discount_cost,eatables_discount_cost=calculate_discounted_prices(apparels_cost,electronics_cost,eatables_cost)

            total_cost=apparels_cost+eatables_cost+electronics_cost
            total_discount = 0


            if apparels_cost >= 2000:
                total_cost=apparels_discount_cost
                apparels_discount=apparels_cost-apparels_discount_cost
                total_discount = apparels_discount
                print('[APPAREL] ', f'Rs {apparels_cost} - Rs {apparels_discount} = ','Rs ',apparels_discount_cost)

                if apparels_cost >= 2000 and electronics_cost >= 25000:
                    total_cost=apparels_discount_cost+electronics_discount_cost
                    electronics_discount=electronics_cost-electronics_discount_cost
                    total_discount = apparels_discount+electronics_discount
                    print('[ELECTRONICS] ',f'Rs{electronics_cost} - Rs{electronics_discount} = ','Rs ',electronics_discount_cost)

                    if apparels_cost >= 2000 and electronics_cost >= 25000 and eatables_cost >= 500:
                        total_cost =apparels_discount_cost+electronics_discount_cost+eatables_discount_cost
                        eatables_discount=eatables_cost-eatables_discount_cost
                        total_discount = apparels_discount+eatables_discount+electronics_discount
                        print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)

                elif apparels_cost >= 2000 and eatables_cost >= 500:
                    eatables_discount=eatables_cost-eatables_discount_cost
                    total_discount = apparels_discount+eatables_discount
                    print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)
                    total_cost =eatables_discount_cost+apparels_discount_cost

            elif electronics_cost >=25000:
                total_cost=electronics_discount_cost
                electronics_discount=electronics_cost-electronics_discount_cost
                print('[ELECTRONICS] ',f'Rs{electronics_cost} - Rs{electronics_discount} = ','Rs ',electronics_discount_cost)
                total_discount = electronics_discount
                if electronics_cost >=  25000 and eatables_cost >= 500:
                    eatables_discount=eatables_cost-eatables_discount_cost
                    print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)
                    total_discount = eatables_discount+electronics_discount
                    total_cost = electronics_discount_cost+eatables_discount_cost
            elif eatables_cost >= 500:
                eatables_discount=eatables_cost-eatables_discount_cost
                print('[EATABLES] ',f'Rs{eatables_cost} - Rs{eatables_discount} = ','Rs ',eatables_discount_cost)
                total_cost=eatables_discount_cost
                total_discount = eatables_discount

            if total_discount > 0:
                print('TOTAL DISCOUNT = Rs ', total_discount)
                print('TOTAL COST = Rs ',total_cost)
                total_cost_including_tax,total_tax = calculate_tax(apparels_discount_cost,electronics_discount_cost,eatables_discount_cost)
                print("TOTAL TAX = Rs ",total_tax)
                print("TOTAL COST = Rs ",total_cost_including_tax)
            else:
                print('TOTAL DISCOUNT = Rs 0')
                print("TOTAL COST = Rs",total_cost)

                total_cost_including_tax,total_tax = calculate_tax(apparels_cost, electronics_cost, eatables_cost)
                print("TOTAL TAX = Rs ",total_tax)
                print("TOTAL COST = Rs ",total_cost_including_tax)
            total_cost_after_coupon_discount, total_coupon_discount=apply_coupon_code(total_cost_including_tax)
            if total_coupon_discount > 0:
                print("TOTAL COUPON DISCOUNT = Rs",total_coupon_discount)
                print("TOTAL COST = Rs" ,total_cost_after_coupon_discount)
            else:
                print("TOTAL COUPON DISCOUNT = Rs 0")
                print("TOTAL COST = Rs" ,total_cost_after_coupon_discount)

            print("Thank you for visiting!")
            tag += 1


if __name__ == '__main__':
    main()

