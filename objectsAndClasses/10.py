class Movie:
    def __init__(self,moviename,hero,heroin,rating):
        self.moviename=moviename
        self.hero=hero
        self.heroin=heroin
        self.rating=rating
m=Movie("Bahubali","Prabhas","Anushka Shetty",9.5)
m1=Movie("RRR","Ram Charan","Alia Bhatt",9.0)
print("Movie Name:",m.moviename,"Hero:",m.hero,"Heroin:",m.heroin,"Rating:",m.rating)
print("Movie Name:",m1.moviename,"Hero:",m1.hero,"Heroin:",m1.heroin,"Rating:",m1.rating)