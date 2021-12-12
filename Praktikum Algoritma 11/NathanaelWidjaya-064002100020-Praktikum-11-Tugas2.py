
class Criteria:
     def __init__(self):
          self._age = 0
      
     @property
     def age(self):
         print("~~~~~getter method called~~~~~")
         return self._age
       
     @age.setter
     def age(self, a):
         if(a < 18):
            raise ValueError("Maaf umur anda dibawah kriteria.")
         print("~~~~~setter method called~~~~~")
         self._age = a
  
x = Criteria()
  
x.age = int(input("Masukan umur: "))
  
print("\nUmur anda sesuai dengan kriteria ",x.age)
