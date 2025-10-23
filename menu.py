menu ={
    "americano": {
        "small" :10, 
        "medium":12,
        "large":14  
    },
"iced_americano": {
    "small":12 ,
    "medium":14 ,
    "large":16 
}
}
print("welcome to RIRI's coffee shop!n")
print("avaliable drinks:americano /iced_americano")
print("sizes:small / medium /large\n")

drink=input("what would you like to order?").lower()
size=input("choose a size (small/medium/large):").lower()

if drink in menu and size in menu[drink]:
    price = menu[drink][size]

    is_employee = input("are you an employee? (yes/no):").lower()
    if is_employee=="yes":
        discount =price * 0.3
        finale_price =price - discount
        print(f"\nyou get a 30% discount\nfinal price sar {final_price}.2f")
    else:
        print(f"\nfinal price : sar {price:.2f}")
else:
    print("\nsorry,we do not have that option.")

