
class Animal:
    def __init__(self, value=""):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class AnimalShelter:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if value == "cat" or value == "dog":
            print("hi")
            animal = Animal(value)
            if not self.front and not self.rear:
                self.front = self.rear = animal
            else:
                temp = self.rear
                self.rear = animal
                temp.next = self.rear
            return f"The {value} has been successfully added to the shelter"
        else:
            return "this shelter for dogs and cats only"

    def dequeue(self, pref=None):
        dequeuedValue = None
        if pref == "cat" or pref == "dog":
            if not self.front and not self.rear:
                raise Exception("Your shelter is empty")
            if self.front.value == pref:
                dequeuedValue = self.front.value
                self.front = self.front.next

            else:
                temp_pre = self.front
                temp_current = self.front.next
                while temp_current:
                    if temp_current.value == pref:
                        temp_pre.next = temp_current.next
                        dequeuedValue = temp_current.value
                        break
                    else:
                        temp_pre = temp_current
                        temp_current = temp_current.next

            if self.front:
                self.rear = None
            if dequeuedValue:
                return dequeuedValue
            else:
                return f"there is no {pref}s in your shelter"
        else:
            return None


if __name__ == "__main__":
    ansh = AnimalShelter()
    print(ansh.enqueue("dog"))
