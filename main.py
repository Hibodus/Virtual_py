# class prog:
#     a = 10
# Obj1 = prog()
# print(Obj1.a)
# Obj1.a = 100
# print(Obj1.a)
# Obj2 = prog()
#
# class prog1:
#     a = 10
#     b = 3.14159
#     c = 'Python'
# Obj3 = prog1()
# print(Obj3.a, Obj3.b)
#
# class prog2:
#     a = 10
#     def f(self):
#         print('a =', self.a)
# if __name__ == '__main__':
#     x = prog2()
#     x.f()
#
# class prog3:
#     a = 10
#     b = 3.14159
#     c = 23
#     def g(self):
#         print(self.a + self.b + self.c)
# if __name__ == '__main__':
#     x = prog3()
#     x.g()

# class MyClass:
#     x = 10 #атрибут класса
#     def __init__(self):
#         self.y = 20 #атрибут экземпляра класса
#
# print(MyClass.x)
# print(MyClass.y) #error
# obj1 = MyClass()
# print(obj1.x)
# print(obj1.y)

# class MyC:
#     def __init__(self):
#         print('вызов конструктора')
#     def __del__(self):
#         print('вызов диструктора')
# obj = MyC
# del obj
#
# class Tr_Class:
#     def __init__(self, x, y, z):
#         self.a = x
#         self.b = y
#         self.c = z
#     def P_Tr(self):
#         P = self.a + self.b + self.c
#         return P
#     def S_Tr(self):
#         P = 0.5 * self.P_Tr()
#         S = (P *(P - self.a) * (P - self.b) * (P - self.c)) ** 0.5
#         return S
# if __name__ == '__main__':
#     Tr1 = Tr_Class(3,4,5)
#     print('p =', Tr1.P_Tr())
#     print('s =', Tr1.S_Tr())
#     Tr2 = Tr_Class(11,12,13)
#     print('p =', Tr2.P_Tr())
#     print('s =', Tr2.S_Tr())
#
# class c1:
#     def f_c1(self):
#         print('f_c1')
# class c2(c1):
#     def f_c2(self):
#         print('f_c2')
# ob1 = c2()
# ob1.f_c1()
# ob1.f_c2()
#
# class D2_Cl:
#     x = 1
#     y = 1
#     def D2(self):
#         d = (self.x ** 2 + self.y ** 2) ** 0.5
#         print('D=', d)
# class D3_Cl(D2_Cl):
#     z = 1
#     def D3(self):
#         d = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
#         print('D=', d)
# x2 = D2_Cl()
# x2.D2()
# X3 = D3_Cl()
# x3.D3()
# x3.D2()
#

# class D2_Cl:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def D2(self):
#         d = (self.x ** 2 + self.y ** 2) ** 0.5
# class D3_Cl(D2_Cl):
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#     def D3(self):
#         x2 = D2_Cl(2,3)
#         x2.D2()


# class TClass:
#     x = 10
#     y = 20
# class TD(TClass):
#     z = 80
# A = TD()
# print(A.x, A.y, A.z)
#
#
# class A:
#     x = 10
# class B:
#     y = 20
# class C(A,B):
#     z = 30
# C_obj = C()
# print(C_obj.x, C_obj.y, C_obj.z)


# class S2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def P_S(self):
#         return 2*(self.x + self.y)
#
# class S3(S2):
#     def __init__(self, x, y, z):
#         super().__init__(x,y)
#         self.z = z
#     def P_S(self):
#         return 4*(self.x + self.y + self.z)
# P2d = S2(10,15)
# print('P =', P2d.P_S())
# P3d = S3(4,12,158)
# print('P =', P3d.P_S())

# class TCLPrn:
#     def P_prn(self, p):
#         print('p =', p)
# class Sq(TCLPrn):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def P(self):
#         p = 2*(self.a + self.b)
#         self.P_prn(p)


# class MyClass:
#     __x = 10
#     def set_x(self, x):
#         self.__x = x
#     def get_x(self):
#         return self.__x
# c = MyClass()
# print(c.get_x())
# c.set_x(100)
# print(c.get_x())
# print(c.__Myclass__x)

# class TClass:
#     @staticmethod
#     def demostatic(self):
#         print('статический метод')
#     def psn(self):
#         print('обычный метод')
#
# TClass.demostatic()



#
# MainWin = tk.Tk()
# MainWin.title('Glavnoe okno')
# # MainWin.geometry("600x320+200+100") #600-w,320-h,200-x,100-y
# W = 640
# H = 320
# X = 300
# Y = 200
# MainWin.geometry('%dx%d+%d+%d' % (W,H,X,Y))
# MainWin.mainloop()
import tkinter as tk
from random import random
class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Glavnoe okno')
        self.geometry('640x320')
        self.resizable(width=False, height=False)
        self.Lb = tk.Label(self, text = 'Это метка(LABLE)')
        self.Lb.pack()
        self.Btn = tk.Button(self, text='Нажми', command= self.Btn_click)
        self.Btn.pack()
    def Btn_click(self):
        Color = '#%02x%02x%02x' % (int(random()*255), int(random()*225), int(random()*255))
        self['bg'] = Color
if __name__ == '__main__':
    MainWin = Aplication()
    MainWin.mainloop()
