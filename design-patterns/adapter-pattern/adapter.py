from external import Musician, Dancer

class Club:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the club {self.name}'

    def organize_event(self):
        return 'hires an artist to perform for the people'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        # Update the dictionary of the Adapter with the adapted methods
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Club('Jazz Cafe'), Musician('Roy Ayers'), Dancer('Shane Sparks')]

    for obj in objects:
        if hasattr(obj, 'play') or hasattr(obj, 'dance'):
            # If 'play' attribute exists, create an adapted_methods dictionary for the Adapter
            if hasattr(obj, 'play'):
                adapted_methods = dict(organize_event=obj.play)
            # If 'dance' attribute exists, create an adapted_methods dictionary for the Adapter
            elif hasattr(obj, 'dance'):
                adapted_methods = dict(organize_event=obj.dance)

            # Create an Adapter object with the original object and adapted methods
            obj = Adapter(obj, adapted_methods)

        print(f'{obj} {obj.organize_event()}')


if __name__ == "__main__":
    main()
