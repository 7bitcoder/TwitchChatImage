from PIL import Image, ImageFilter
#Read image
im = Image.open( 'input9.png' )
#Display image
im = im.convert('RGB')
im.show()

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.FIND_EDGES).show()
#Saving the filtered image to a new file
im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

#Viewing EXIF data embedded in image