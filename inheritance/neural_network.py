class Layer:
    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return layer


class Input(Layer):
    """формирование входного слоя нейронной сети;"""

    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs


class Dense(Layer):
    """формирование полносвязного слоя нейронной сети."""

    def __init__(self, inputs, outputs, activation):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)
