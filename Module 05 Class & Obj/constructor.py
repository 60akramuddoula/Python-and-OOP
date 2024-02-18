class pen_construct:

    def __init__(self, brand_Name,priceofHolesale, priceoftotalsale,inkkcolor):
        self.brand_Name= brand_Name
        self.priceofHolesale= priceofHolesale
        self.priceoftotalsale= priceoftotalsale
        self.inkkcolor= inkkcolor


my_pen= pen_construct()
print(my_pen.brand_Name('Samsung'))
print(my_pen.priceofHolesale(15000))
