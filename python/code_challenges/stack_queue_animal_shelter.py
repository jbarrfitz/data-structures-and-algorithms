from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self, front=None, tail=None):
        self.front = front
        self.tail = tail

    def enqueue(self, animal):
        if not animal:
            return
        if animal.lower() == "dog":
            new_animal = Dog()
        elif animal.lower() == "cat":
            new_animal = Cat()
        else:
            return
        if not self.tail:
            self.tail = self.front = new_animal
        else:
            self.tail.next = new_animal
            self.tail = new_animal

    def dequeue(self, pref=None):
        if not self.front:
            return
        if pref == "dog":
            match_class = "Dog"
        elif pref == "cat":
            match_class = "Cat"
        else:
            return
        curr_animal = self.front.value
        while True:
            if isinstance(curr_animal, match_class):
                dequeued = curr_animal

        self.front = self.front.next
        return dequeued

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        return self.front.value

    def is_empty(self):
        return not self.front


class Dog:
    def __init__(self, name="", next=None):
        self.name = name
        self.next = next


class Cat:
    def __init__(self, name="", next=None):
        self.name = name
        self.next = next
