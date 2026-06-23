import cv2 as cv
path = input("Enter image path: ")
image = cv.imread(path)

#Save the file
def save_image(img):
    ans = input("Do you want to save the changes? (Y/N): ")
    if ans.strip().lower() == "y":
        name = input("Enter file name with extension: ")
        file = cv.imwrite(name, img)
        if file:
            print("Image saved successfully :)")
        else:
            print("Failed to save the image :(")

#Resize the image
def resize():
    width = int(input("Enter Width: "))
    height = int(input("Enter Height:"))
    resize = cv.resize(image,(width,height))
    cv.imshow("original image",image)
    cv.imshow("resized image",resize)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save_image(resize)

#Grayscale conversion
def converter():
    img = image.copy()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Original Image",img)
    cv.imshow("Updated Image", gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save_image(gray)

# Rotate or flip
def rotate_flip():

    do = input("Write 'f' for flip, 'r' for rotate : ")

    if do == "f":
        print("Flip along\n 1. x-axis\n 2. y-axix\n 3. both")
        a = input("Choose one: ")
        flipv = cv.flip(image, 0)
        fliph = cv.flip(image, 1)
        flipb = cv.flip(image, -1)

        if a == "1":
            cv.imshow("original",image)
            cv.imshow("vertical flip",flipv)
            cv.waitKey(0)
            cv.destroyAllWindows()
            save_image(flipv)
        
        elif a == "2":
            cv.imshow("original",image)
            cv.imshow("vertical flip",fliph)
            cv.waitKey(0)
            cv.destroyAllWindows()
            save_image(fliph)

        elif a == "3":
            cv.imshow("original",image)
            cv.imshow("vertical flip",flipb)
            cv.waitKey(0)
            cv.destroyAllWindows()
            save_image(flipb)

        else:
            print("Wrong input")
    
    elif do == "r":
        deg = float(input("Enter the degree of rotation(use - sign for clockwise rotation): "))
        h,w = image.shape[:2]
        center = (w//2,h//2)
        R = cv.getRotationMatrix2D(center, deg, 1.0)
        rotated = cv.warpAffine(image, R, (w,h))
        cv.imshow("Original image",image)
        cv.imshow("Rotated image",rotated)
        cv.waitKey(0)
        cv.destroyAllWindows()

        save_image(rotated)
    

#Draw any image or figure
def shapes():
    print("What do you want to draw: ")
    print("1. Line")
    print("2. Rectangle")
    print("3. Circle")

    response = input("Enter your choice: ")

    if response == "1":
        x = int(input("Enter X coordinate of starting point: "))
        y = int(input("Enter y coordinate of starting point: "))
        x1 = int(input("Enter X coordinate of end point: "))
        y1 = int(input("Enter y coordinate of end point: "))

        a = (x,y)
        b = (x1,y1)
        color = (200,255,255)
        thickness = 3

        shape = image.copy()
        cv.line(shape, a, b, color, thickness)
        cv.imshow("Line drawn", shape)
        cv.waitKey(0)
        cv.destroyAllWindows()
        save_image(shape)
    
    elif response == "2":
        x = int(input("Enter X coordinate of starting point: "))
        y = int(input("Enter y coordinate of starting point: "))
        x1 = int(input("Enter X coordinate of end point: "))
        y1 = int(input("Enter y coordinate of end point: "))

        a = (x,y)
        b = (x1,y1)
        color = (200,255,255)
        thickness = 3

        shape = image.copy()
        cv.rectangle(shape, a, b, color, thickness)
        cv.imshow("Rectangle Drawn", shape)
        cv.waitKey(0)
        cv.destroyAllWindows()
        save_image(shape)

    elif response == "3":
        x = int(input("Enter X coordinate: "))
        y = int(input("Enter y coordinate: "))
        c = (x,y)
        r = int(input("Enter the radius of the circle: ") )
        color = (255,255,255)
        thickness = 3

        shape = image.copy()
        cv.circle(shape, c, r, color, thickness)
        cv.imshow("Circle Drawn", shape)
        cv.waitKey(0)
        cv.destroyAllWindows()
        save_image(shape)

#Edit the text
def text():
    img = image.copy()
    font = cv.FONT_HERSHEY_DUPLEX
    font_scale = 1.3
    thickness = 2

    
    txt = input("Enter the text you want to be displayed on the image: ")

    (text_width, text_height), _ = cv.getTextSize(
        txt,
        font,
        font_scale,
        thickness
        )
    h, w = img.shape[:2]
    x = (w - text_width) // 2
    y = h - 20

    cv.putText(img, txt , (x,y), 
               cv.FONT_HERSHEY_DUPLEX, font_scale, (255,255,255), thickness)
    cv.imshow("Edited photo",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    save_image(img)

if image is None:
    print("Invalid image path.\nExiting.....")
    exit()

else:

    while True:
        print("Choose any option from the following: ")
        print("1. Convert the photo in black and white.")
        print("2. Resize the image.")
        print("3. Rotate or flip the image.")
        print("4. Draw any shape on the image(line, rectangle, circle)")
        print("5. Add text in the image.")
        print("6. Exit...")

        res = input("Enter any option: ")

        if res == "1":
            converter()

        elif res == "2":
           resize()

        elif res == "3":
            rotate_flip()

        elif res == "4":
            shapes()

        elif res == "5":
            text()
        
        elif res == "6":
            break

        else:
            print("Wrong input please try again.")



        
