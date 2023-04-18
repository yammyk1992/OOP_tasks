# class SoftList(list):
#     def __init__(self, lst):
#         super().__init__()
#         self.lst = [",".join(i) for i in lst]
#         print(self.lst)
#
#     def __getitem__(self, item):
#         try:
#             if item <= len(self.lst):
#                 return self.lst[item]
#         except IndexError:
#             return False
#
#     def __setitem__(self, key, value):
#         if key <= len(self.lst):
#             self.lst[key] = value
#         return False

class SoftList(list):
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return False


sl = SoftList("python")

print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
