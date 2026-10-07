from PIL import Image, ImageDraw, ImageFont
import sys
F=lambda s,b=True: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
PW,PH,G=600,400,24
def fit(img,box=None):
    im=Image.open(img).convert('RGB')
    if box: im=im.crop(box)
    w,h=im.size;r=PW/PH
    if w/h>r: nw=int(h*r);im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
    else: nh=int(w/r);im=im.crop((0,(h-nh)//2,w,(h-nh)//2+nh))
    return im.resize((PW,PH),Image.LANCZOS)
def make(title,panels,out):
    W=G+len(panels)*(PW+G);H=110+PH+G
    c=Image.new('RGB',(W,H),'#f5f7fa');d=ImageDraw.Draw(c)
    d.text((G,22),title,font=F(30),fill='#173a5e')
    for i,(img,box,label,col) in enumerate(panels):
        x=G+i*(PW+G);y=86
        c.paste(fit(img,box),(x,y))
        d.rounded_rectangle((x+12,y+12,x+12+F(18).getlength(label)+24,y+46),radius=14,fill=col)
        d.text((x+24,y+17),label,font=F(18),fill='white')
        if i<len(panels)-1: d.text((x+PW+3,y+PH//2-18),'›',font=F(34),fill='#8a96a3')
    d.text((G,64),'Concept mockup — not to scale',font=F(15,False),fill='#6b7785')
    c.save(out)
make('EEE building: today vs biosolar roof',[
 ('reference-photos/eee-building.webp',(560,0,1340,500),'Photo · today','#5b6670'),
 ('s3/c_eee.png',(100,0,1180,720),'3D · biosolar roof','#2e8b57')],'s3/compare_eee.png')
make('Rooftop solar: today vs biosolar roof',[
 ('reference-photos/ntu-rooftop-solar.webp',None,'Photo · NTU rooftop today','#5b6670'),
 ('s3/c_roof.png',(100,0,1180,720),'3D · biosolar roof','#2e8b57')],'s3/compare_roof.png')
make('Campus Loop bus stop: today vs Solar Cool Stop',[
 ('reference-photos/campus-loop-bus-stop.png',(0,150,335,500),'Photo · today','#5b6670'),
 ('s3/c_stop.png',(100,0,1180,720),'3D · Solar Cool Stop','#2e8b57')],'s3/compare_busstop.png')
