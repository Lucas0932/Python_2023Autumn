class Car:
    def __init__(self, color):
        self.color = color
        self.next = None
head = Car("red")
second = Car("blue")
head.next = second
second.next=head
def traverse(head):
    ptr = head
    while True:
        print("The color of the car is {}.". format(ptr.color))
        if ptr.next == head:
            break
        ptr = ptr.next 
    print("Finish traverse!")

# traverse(head)
#------------------------------------------------------
new = Car("black")
new.next = head
ptr = head
while ptr.next != head:
    ptr = ptr.next
ptr.next = new
head = new
#traverse(head)
#------------------------------------------------------
pink = Car("pink")
red = head.next
pink.next = second
red.next = pink
# red = Car("red")
# head.next = red
# red.next = pink
traverse(head)