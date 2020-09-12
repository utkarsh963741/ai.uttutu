from PIL import Image

for i in range(91):
    image = Image.open('./background/'+str(i)+'.jpg')
    new_image = image.resize((1080, 608))
    new_image.save(str(i+85)+'.jpg')
    print(i)