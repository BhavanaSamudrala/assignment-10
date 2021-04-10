from a10provided.a10q2_Container import Container


class Queue(Container):

    def __init__(self):
        Container.__init__(self)

    def dequeue(self):
        return Container.pop_top(self)
    def enqueue(self,value):
        return Container.add_bottom(self,value)

    def peek(self):
        return Container.peek(self)