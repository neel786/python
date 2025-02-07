class employee:
  __id=0
  __name=""
  __gender=""
  __age=""

  def __init__(self,empid,name,gender,age):  #initialize object with the value
      self.__id=empid
      self.__name=name
      self.__gender=gender
      self.__age=age

  def showEmplInfo(self):
      print("Employee ID \t:", self.__id)
      print("Employee name \t:", self.__name)
      print("Employee gender \t:", self.__gender)
      print("Employee age \t:", self.__age)

#create object for the particular class
emp1=employee('12345',"Oliver","male","45")
emp1.showEmplInfo()
