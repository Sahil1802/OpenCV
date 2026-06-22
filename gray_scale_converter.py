import cv2 as cv

# to convert and save normal image into gray image. 
def Converter():
    img = cv.imread(image)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Image converted successfully!", gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

    res = input("Do you want to save the changes?(Y/N)")
    if res == "y" or res == "Y":
        name = input("Enter the name of the photo")
        cv.imwrite(name,gray)
        print("Image saved successfully")
    else:
        print("exiting...")
    
#taking image path input. 
image = input("Please write the path of the image: ")

if image is not None:
    while True:
        print("1.Show the Image.")
        print("2.Convert the image in grayscale image.")
        ans = input("Choose any option: ")    
        if ans == "1":
            img = cv.imread(image)
            cv.imshow("Showing you the Image..", img)
            cv.waitKey(0)
            cv.destroyAllWindows()
            break

        elif ans == "2":
            Converter()
            break

        else:
            print("Wrong Input please try again")

else:
    print("No Image Found :(")







