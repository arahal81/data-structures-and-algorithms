from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter
import pytest


@pytest.fixture
def animal_shelter():
    animal_shelter = AnimalShelter()

    return animal_shelter


def test_animal_shelter_enqueue_cat(animal_shelter):

    assert animal_shelter.enqueue(
        "cat") == "The cat has been successfully added to the shelter"


def test_animal_shelter_enqueue_dog(animal_shelter):

    assert animal_shelter.enqueue(
        "dog") == "The dog has been successfully added to the shelter"


def test_animal_shelter_enqueue_rabbit(animal_shelter):

    assert animal_shelter.enqueue(
        "rabbit") == "this shelter for dogs and cats only"


def test_animal_shelter_dequeue_cat(animal_shelter):
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    assert animal_shelter.dequeue(
        "cat") == "cat"


def test_animal_shelter_dequeue_dog(animal_shelter):
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    assert animal_shelter.dequeue(
        "dog") == "dog"


def test_animal_shelter_dequeue_rabbit(animal_shelter):
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    assert animal_shelter.dequeue(
        "rabbit") == None


def test_animal_shelter_dequeue_dog_not_exist(animal_shelter):
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("cat")
    assert animal_shelter.dequeue(
        "dog") == "there is no dogs in your shelter"


def test_animal_shelter_dequeue_can_not_exist(animal_shelter):
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("dog")
    assert animal_shelter.dequeue(
        "cat") == "there is no cats in your shelter"


def test_animal_shelter_dequeue_from_empty_shelter(animal_shelter):
    with pytest.raises(Exception, match="Your shelter is empty"):
        animal_shelter.dequeue("cat")
