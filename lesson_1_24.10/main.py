# Напишите низкоуровневый алгоритм работы со статическим массивом
# (реализованы операции записи, чтения, вставки, удаления).

class StaticArray:
    def __init__(self, length):
        self.length = length
        self.st_ar = self._create_st_ar()

    def _create_st_ar(self):
        st_ar = []
        count = 0
        while count < self.length:
            st_ar += [None]
            count += 1
        return st_ar

    def add_item(self, item):
        for i in range(self.length):
            if self.st_ar[i] is None:
                self.st_ar[i] = item
                break
        return self.st_ar

    def get_item_by_index(self, num):
        assert num < self.length, 'Array has no such index.'
        return self.st_ar[num]

    def get_last_item_if_space(self):
        i = -1
        for item in self.st_ar:
            i += 1
            if item is None and i == 0:
                return 'empty'
            elif item is None and i != 0:
                return i - 1
            elif item is not None and i == self.length - 1:
                return False

    def insert_item_by_index(self, item, num):
        last_item_ind = self.get_last_item_if_space()

        assert last_item_ind, "Can't insert an item in full array."
        if last_item_ind == 'empty':
            self.st_ar[num] = item
        else:
            for i in range(last_item_ind, num - 1, -1):
                self.st_ar[i + 1] = self.st_ar[i]
            self.st_ar[num] = item

        return self.st_ar

    def delete_item_by_index(self, num):
        assert num < self.length, 'Array has no such index.'
        assert self.st_ar[num] is not None, 'There is no item by this index.'

        for i in range(num, self.length):
            if i != self.length - 1:
                self.st_ar[i] = self.st_ar[i + 1]
            else:
                self.st_ar[i] = None

        return self.st_ar

#Проверка

sm = StaticArray(5)
print(f'Add item 1 - {sm.add_item(1)}')
print(f'Add item 2 - {sm.add_item(2)}')
print(f'Add item 3 - {sm.add_item(3)}')
print(f'Add item 4 - {sm.add_item(4)}')

print(f'Read item by index 3 - {sm.get_item_by_index(3)}')
print(f'Insert 5 by index 2 - {sm.insert_item_by_index(5, 2)}')
print(f'Delete item by index 1 - {sm.delete_item_by_index(1)}')

# Напишите собственные хэш-функции. Подайте на вход разнообразные ключи,
# убедитесь, что слишком часто коллизии не возникают, иначе усовершенствуйте функцию.


def hash_item(word):
    hash_value = 0
    table_size = 1000
    for i in word:
        hash_value += ord(i)
    hash_value = (hash_value * ord(i)) % table_size

    return hash_value


print(hash_item('2'))
print(hash_item('goodbye'))
print(hash_item('a'))
