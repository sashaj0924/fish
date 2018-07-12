def setup():
    size(400, 400)
    background(43, 169, 237)
    fish(255, 255, 0, 30, 30, 40 )
    fish( 70, 200, 80, 300, 300, 70)
    fish( 300, 85, 65, 200, 200, 50)
    
def fish(r, b, g, x, y, s):
    noStroke()
    fill(r,b,g)
    ellipse(x, y, s, s)
    noStroke()
    triangle(x+5, y, x+s, y-s/2, x+s, y+s/2)
    fill (10, 10, 9)
    ellipse( x-5, y, 5, 5)
    
    
