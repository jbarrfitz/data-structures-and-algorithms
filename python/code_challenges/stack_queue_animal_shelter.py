class Animal:
    def __init__(self, next=None):
        self.next = next


class Cat(Animal):
    def __init__(self, species="cat", name=""):
        super().__init__(None)
        self.species = species
        self.name = name


class Dog(Animal):
    def __init__(self, species="dog", name=""):
        super().__init__(None)
        self.species = species
        self.name = name


class AnimalShelter:
    def __init__(self, front=None, tail=None):
        self.front = front
        self.tail = tail

    def enqueue(self, animal):
        if not self.front:
            self.front = self.tail = animal
        else:
            self.tail.next = animal
            self.tail = self.tail.next

    def dequeue(self, pref=""):
        if not self.front:
            return None
        if not pref:
            dequeued = self.front
            self.front = self.front.next
            return dequeued
        if pref.lower() != "dog" and pref.lower() != "cat":
            return None
        queue = []
        curr_animal = self.front
        dequeued = None
        while curr_animal:
            if pref.lower() == curr_animal.species and dequeued is None:
                dequeued = curr_animal
                self.front = self.front.next
                break
            else:
                queue.append(curr_animal)
                curr_animal = curr_animal.next
                self.front = self.front.next
        return dequeued
