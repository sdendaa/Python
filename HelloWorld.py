from string import Template
print("Hello World")
class Parent:
    value1 = "This is value one"
    value2 ="This is value two"

class Child(Parent):
    pass

myParent = Parent()
myChild = Child()
print(myChild.value1);
print(myChild.value2);

class CalcSum:
        def addItem(self):
            cart =[]
            cart.append(dict(item ="cake",price =8, qty = 2))
            cart.append(dict(item="cake", price=12, qty=1))
            cart.append(dict(item="fish", price=8, qty=5))

        def sum(self):
            t =Template("$qty * $item = $price")
            total = 0
            myList =[]
            myList = addItem()

            print("Cart:")
            for data in myList:
                print(t.substitute(data))
                total+=data("price")
            print("Total:"+str(total))

mySum = CalcSum()
print(mySum.sum())