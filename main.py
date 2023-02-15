from PIL import Image
def bilde():
   datne = Image.open("pantheon--rome--italy-870287362-5a87671b6bf06900375c06f2.jpg")
   rotate_build = datne.rotate(90)
   rotate_build.save("b.jpg", rotate_build.format)
   rotate_build.show
bilde()

def bilde2():
  bilde2= Image.open("b.jpg")
  bilde2_resize = ((40,40))
  bilde2_resize.save("fg.jpg", bilde2.format)
  bilde2.show
bilde2()
    