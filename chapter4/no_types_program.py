from collections import namedtuple

Item=namedtuple("Item","name,value")

running_max=None

def counter(items):
    global running_max
    total=0


    for i in items:
        total+=i.value

    if not running_max or total>running_max:
        running_max=total



    return total

def main():
    print("Let's create some items")

    dinner_items=[Item('Pizza',20),Item('Beer',9),Item('Beer',9)]
    breakfast_items=[Item('Pancakes',11),Item('Bacon',4),Item('Coffee',3),Item('Coffee',3)]

    dinner_total=counter(dinner_items)
    print(f"Dinner was ${dinner_total:,.02f}")

    breakfast_total=counter(breakfast_items)
    print(f"Breakfast was ${breakfast_total:,.02f}")

if __name__ == '__main__':
    main()
