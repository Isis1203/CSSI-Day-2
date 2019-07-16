def setup(): # runs once
    size(512, 512)
    noStroke()
      
def draw(): # run multiple times
    if mousePressed:
        fill (52, 132, 240) 
        ellipse(mouseX, mouseY, 20, 20) 
    if keyPressed and key == 'c' or key == 'C': 
             background (200, 200, 200)
             

    # if mouseY > 256: 
    #     if mouseX > 256: 
    #         fill (255, 0, 0) #red
    #     else: 
    #         fill (255, 0, 255) #purple 
    # else:
    #     if mouseX > 256:
    #             fill (0, 0, 255)#blue
    #     else: 
    #         fill (0, 255, 255) #teal 
    
    
     # else:
    #     fill (117, 117, 117)
    
    
    #alternative solution: rect(mouseX, mouseY, 100, 100)
    #translate (-50, -50)
        
