
# Python comes with built in text alignment methods
#       ljust(width, padchar)
#       rjust(width, padchar)
#       center(width, padchar)


thickness = int(input())
c = 'H'

#Top Cone. Since we making a triangle, it looks like /|\. So rjust first then ljust
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars. Center align the thicknesses so we have pillar in middle of cone
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt. Center align on this one
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))