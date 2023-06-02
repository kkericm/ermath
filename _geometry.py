# 
# circle
# Trapeze
# Triangle
from _othernum import deg
from _alias import Arrest
from _excepts import ImpossibleRectangle
from _bsc import raiz

"""# if (type(width) and type(height)) is (int or float):
        #     self.__y__ = abs(height)
        #     self.__x__ = abs(width)

        
        # elif (type(diagonal) and (type(alfa_angle) or type(beta_angle))) is (int or float):
        #     if type(alfa_angle) and type(beta_angle):
        #         if alfa_angle + beta_angle == 90:
        #             self.__a__ = alfa_angle
        #             self.__b__ = beta_angle
        #         else:
        #             raise ImpossibleRectangle("The sum of the angles must be 90 degrees, neither more nor less.")
        #     elif type(beta_angle) is (int or float):
        #         self.__b__ = abs(beta_angle)
        #         self.__a__ = 90 - self.__b__
        #     else:
        #         self.__a__ = abs(alfa_angle)
        #         self.__b__ = 90 - self.__a__
        #     self.__d__ = diagonal


        # elif (type(diagonal) and (type(width) or type(height))) is (int or float):
        #     if type(height) is (int or float):
        #         self.__l__ = abs(height)
        #     else:
        #         self.__l__ = abs(width)
        #     if abs(diagonal) > self.__l__:
        #         diagonal = abs(diagonal)
        #     else:
        #         raise ImpossibleRectangle("It is impossible for a rectangle to have the shorter diagonal and one of the sides.")
        
        # elif ((type(width) or type(height)) and (type(alfa_angle) or type(beta_angle))) is (int or float):
        #     if type(alfa_angle) and type(beta_angle) is (int or float):
        #         if alfa_angle + beta_angle == 90:
        #             self.__a__ = alfa_angle
        #             self.__b__ = beta_angle
        #         else:
        #             raise ImpossibleRectangle("The sum of the angles must be 90 degrees, neither more nor less.")
        #     elif type(beta_angle) is (int or float):
        #         self.__b__ = abs(beta_angle)
        #         self.__a__ = 90 - self.__b__
        #     else:
        #         self.__a__ = abs(alfa_angle)
        #         self.__b__ = 90 - self.__a__

        #     if type(height) is (int or float):
        #         self.__l__ = abs(height)
        #     else:
        #         self.__l__ = abs(width)
        
        # else:"""
        
class Rectangle():
    def __init__(self,
            height: (int or float) = None,
            width: (int or float) = None,
            diagonal: (int or float) = None,
            alfa_angle: (int or float) = None,
            beta_angle: (int or float) = None
        ) -> None:
        self.__y__ = height
        self.__x__ = width
        self.__d__ = diagonal
        self.__a__ = alfa_angle
        self.__b__ = beta_angle
        
        if self.__y__ == None:
            self.__l__ = self.__x__
        else:
            self.__l__ = self.__y__
        
        if (type(self.__a__)  is (int or float)) and (type(self.__b__) is (int or float)):
            if alfa_angle + beta_angle != 90:
                raise ImpossibleRectangle("The sum of the angles must be 90 degrees, neither more nor less.")
        elif type(self.__b__) is (int or float):
            self.__a__ = 90 - self.__b__
        elif type(self.__a__) is (int or float):
            self.__b__ = 90 - self.__a__
        
        if (type(self.__d__) and (self.__y__ or self.__x__)) is (int or float): 
            if self.__d__ < (self.__y__ or self.__x__):
                raise ImpossibleRectangle("It is impossible for a rectangle to have the shorter diagonal and one of the sides.")
        # area
        # center
        # perimeter
        self.__ar__ = None
        self.__pr__ = None
        
    def degrees(self, Arrest: Arrest):
        pass
    
    @property
    def area(self):
        if self.__ar__ == None: 
            
            """# if (type(self.__x__) and type(self.__y__)) is (int or float):
            #     print(type(self.__x__))
            #     print(type(self.__y__))
            #     self.__ar__ = self.__x__ * self.__y__
                
                
            # elif (type(self.__d__) and (type(self.__a__) or type(self.__b__))) is (int or float):
            #     if type(self.__a__) is (int or float):
            #         self.__ar__ = (self.__d__ ** 2) * (deg(self.__a__).sin * deg(self.__a__).cos)
            #     else:
            #         self.__ar__ = (self.__d__ ** 2) * (deg(self.__b__).sin * deg(self.__b__).cos)
                    
                    
            # elif (type(self.__d__) and (type(self.__x__) or type(self.__y__))) is (int or float):
            #     if type(self.__y__) is (int or float):
            #         self.__ar__ = raiz((self.__d__ ** 2) - (self.__y__ ** 2))
            #     else:
            #         self.__ar__ = raiz((self.__d__ ** 2) - (self.__y__ ** 2))
                    
                    
            # elif ((type(self.__a__) or type(self.__b__)) and (type(self.__x__) or type(self.__y__))) is (int or float):
            #     if type(self.__a__) is (int or float):
            #         w = self.__a__
            #     else: w = self.__b__
                
            #     if type(self.__x__) is (int or float):
            #         y = self.__x__ * deg(w).tan
            #         self.__ar__ = self.__x__ * y
            #     else: 
            #         x = self.__y__ * deg(w).tan
            #         self.__ar__ = self.__y__ * x"""
        
            try:
                self.__ar__ = self.__ar_1__(self.__x__, self.__y__)
            except:
                try:
                    self.__ar__ = self.__ar_2__(self.__l__, self.__d__)
                except:
                    try:
                        if self.__a__ != None:
                            self.__ar__ = self.__ar_3__(self.__l__, self.__a__)
                        else:
                            self.__ar__ = self.__ar_3__(self.__l__, self.__b__)
                    except:
                        if self.__a__ != None:
                            self.__ar__ = self.__ar_4__(self.__d__, self.__a__)
                        else:
                            self.__ar__ = self.__ar_4__(self.__d__, self.__b__)
                                            
        
        return self.__ar__ # [self.__b__, self.__x__, self.__y__, self.__a__, self.__b__]

    def __ar_1__(self, w, h):
        return w * h
    def __ar_2__(self, l, d):
        return raiz((d**2) - (l**2))
    def __ar_3__(self, l, t):
        return l * (l * deg(t).tan)
    def __ar_4__(self, d, t):
        return (d ** 2) * (deg(t).sin * deg(t).cos) 
    
# print(Rectangle(3, 4).area)                        # 12
# print(Rectangle(3, alfa_angle=60).area)            # 17.05239
# print(Rectangle(3, beta_angle=60).area)            # 5.21136
# print(Rectangle(3, diagonal=10).area)              # 91
# print(Rectangle(diagonal=10, alfa_angle=60).area)  # 38.64471931
# print(Rectangle(diagonal=10, beta_angle=60).area)  # 43.11802331