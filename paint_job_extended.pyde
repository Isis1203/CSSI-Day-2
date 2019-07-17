canvas_x = 600 
canvas_y = 600
rectangle_count = 6 
rectangle_height = 70
rectangle_width = canvas_x / rectangle_count 
print(rectangle_width)

def setup(): #runs once
    size (600, 600) 
    background(255, 255, 255)
    rect(0, 0, rectangle_width, rectangle_height)#clear button 
    fill(52, 132, 240) #blue
    rect(rectangle_width, 0, rectangle_width, rectangle_height)
    fill(255, 0, 255) #purple 
    rect(2 * rectangle_width, 0, rectangle_width, rectangle_height)
    fill( 234, 234, 234)#gray
    rect(3 * rectangle_width, 0, rectangle_width, rectangle_height)
    fill(78, 48, 67)#maroon 
    rect(4 * rectangle_width, 0, rectangle_width, rectangle_height)
    fill(255, 255, 255) #eraser 
    rect(5 * rectangle_width, 0, rectangle_width, rectangle_height)
    noStroke()


def draw () :
    if keyPressed and key == "c": 
        fill(255, 255, 255) 
        rect(0, 71, canvas_x, canvas_y) 
        
    if mousePressed and mouseY > 75:
        ellipse(mouseX, mouseY, 5, 5)
        
    if mouseX > rectangle_width and mouseX < rectangle_width*2 and mouseY < rectangle_height:
        print("in box 2")
        fill(52, 132, 240)
    else:
        print("")
        
    if mouseX > rectangle_width*2 and mouseX < rectangle_width*3 and mouseY < rectangle_height:
        print("in box 3")
        fill(255, 0, 255) 
    else:
        print("")
        
    if mouseX > rectangle_width*3 and mouseX < rectangle_width*4 and mouseY < rectangle_height:
        print("in box 4") 
        fill( 234, 234, 234)
    else:
        print("")
        
    if mouseX > rectangle_width*4 and mouseX < rectangle_width*5 and mouseY < rectangle_height:
        print("in box 5") 
        fill(78, 48, 67)
    else:
        print("")
    
    if mouseX > rectangle_width*5 and mouseX < rectangle_width*6 and mouseY < rectangle_height:
        print("in box 6") 
        fill(255, 255, 255) 
    else:
        print("")
    
#Purple box (box 2) is at TL: 200, 0 TR: 400, 0 BL: 200, 70 BR:400, 70
#200-400 in X
#0-70 in Y 
