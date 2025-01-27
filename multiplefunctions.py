class overallfunctions():
    
    def subfields():
        fields="Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"
        print("subfields in ai are:",fields)
        return fields

    def oddeven():
        num=int(input("enter a number is:"))
        if(num%2==0):
              print(num,"is even number")
              message=num,"is even number"
        else: 
              print(num,"is odd number")  
              message=num,"is odd number"
        return message

    def marriage_eligibility():
        num=input("your gender:")
        num2=int(input("your age:"))
        if(num== "male" and num2>21):
            print("eligible")
            message="eligible"
        elif(num=="female"and num2>18):
            print("eligible")
            message="eligible"
        else:
            print("not eligible")
            message="not eligible"
        return message

    def find_percentage():
        num1=int(input("subject_1="))
        num2=int(input("subject_2="))
        num3=int(input("subject_3="))
        num4=int(input("subject_4="))
        num5=int(input("subject_5="))
        add = num1+num2+num3+num4+num5
        print("total:",add)
        percentage=add/500*100
        print("percentage:",percentage)
        return percentage

    def triangle():
        height=int(input("height:"))
        breadth=int(input("breadth:"))
        area=(height*breadth)/2
        print("area=",area)
        area_of_triangle=(1/2)*(breadth*height)
        print("area of triangle=",area_of_triangle)
        height1=int(input("height1:"))
        height2=int(input("height2:"))
        breadth1=int(input("breadth:"))
        perimeter= height1+height2+breadth1
        print("perimeter=",perimeter)