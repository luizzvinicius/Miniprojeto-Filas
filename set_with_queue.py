class FilaArray:
    def __init__(self, queue=None):
        if queue is None:
            queue = [None] * 8
            self._added = 0
        else:
            added = 0
            for i in queue:
                if i is not None:
                    added += 1
            self._added = added

        self._first = 0
        self.queue = queue

    def __len__(self):
        return self._added

    def is_empty(self):
        return self._added == 0

    def enqueue(self, element):
        self._increase_size()

        disponivel = (self._first + self._added) % len(self.queue)
        self.queue[disponivel] = element
        self._added += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue()

        excluded = self.queue[self._first]
        self.queue[self._first] = None
        self._first = (self._first + 1) % len(self.queue)
        self._added -= 1
        return excluded

    def _increase_size(self):
        if self._added == len(self.queue):
            old_queue = self.queue
            self.queue = [None] * 2 * len(self.queue)

            i = self._first
            for j in range(self._added):
                self.queue[j] = old_queue[i]
                i = (i + 1) % len(old_queue)

            self._first = 0


class EmptyQueue(Exception):
    def __init__(self, mensagem="Fila está vazia"):
        super().__init__(mensagem)


class ElementNotFound(ValueError):
    def __init__(self, mensagem="Element not found"):
        super().__init__(mensagem)


class SetWithQueue(FilaArray):

    def size(self):
        return self._added

    def add(self, element):
        if self.contains(element):
            return

        super().enqueue(element)

    def remove(self, element):
        if self.is_empty():
            raise EmptyQueue()

        old_queue = self.queue
        self.queue = [None] * len(self.queue)

        i = self._first
        for j in range(self._added):
            self.queue[j] = old_queue[i]
            i = (i + 1) % len(old_queue)
        self._first = 0  # reorganiza a fila
        index = self._index_of(element)

        if index == -1:
            raise ElementNotFound

        for i in range(index, self._added - 1):
            self.queue[i] = self.queue[i + 1]

        self._added -= 1
        self.queue[self._added] = None
        self._first = 0

    def _index_of(self, element):
        for i in range(len(self.queue)):
            j = (self._first + i) % len(self.queue)

            if self.queue[j] == element:
                return i

        return -1

    def contains(self, element):
        return self._index_of(element) > -1

    def list(self):
        return [
            self.queue[(self._first + i) % len(self.queue)] for i in range(self._added)
        ]


lista = SetWithQueue()
lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)
lista.remove(1)
lista.add(5)
lista.remove(5)
print(lista.list())
print(lista.contains(5))
