from wand.image import Image as wi
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


ImageSequence = 1

for i in range(35,40):
    PROFILE=wi(filename='EP'+str(i)+'.pdf',resolution=400)
    Images=PROFILE.convert('jpg')


    for img in PROFILE.sequence:

        Imm=wi(image=img)
        Imm.save(filename='Image'+str(i)+'_' +str(ImageSequence)+'.jpg')
        pic=Image.open('Image'+str(i)+'_'+str(ImageSequence)+'.jpg')
        text=pytesseract.image_to_string(pic)
        txt_file=open('my_txt'+str(i)+'_'+str(ImageSequence)+'.txt','w')
        ImageSequence +=1
        TXT = open('EP_TXT' + str(i) + '.txt', 'a+')
        TXT.write(text)
