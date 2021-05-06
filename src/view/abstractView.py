from abc import ABC, abstractmethod

class AbstractView(ABC):

    #dict keys as integers mean nothing to me
    def set_keys_to_attrs(self, values, attributes):
        count = 0
        for key, value in values.items():
            values[attributes[count]] = values.pop(count)
            count += 1

        return values

