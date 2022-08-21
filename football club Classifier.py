from PIL import Image
import glob
import ntpath as nt

def detect(im):
    b = 0
    r = 0 
    w = im.size[0]
    h = im.size[1]
    pix = im.load()
    for i in range(w):
        for j in range(h):
            r += pix[i,j][0]
            b += pix[i,j][2]
    if r > b : 
        return 0 
    else :
        return 1 
def confusion(man,chel):
    tp = 0 
    fp = 0 
    fn = 0 
    tn = 0
    for i in chel:
        if i == 'c': 
            tp += 1 
        else:
            fp += 1
    for i in man:
        if i == 'm':
            tn += 1 
        else:
            fn += 1 
    return [tp,fp,fn,tn]
def recall(tp,fn):
    return tp/(tp+fn)
def percision(tp,fp):
    return tp/(tp+fp)
def accuracy(tp,tn,fp,fn):
    return (tp+tn)/(tp+tn+fp+fn)
def extract(adr1):
    for adr in glob.glob(adr1):
        im = Image.open(adr) 
        print(detect(im))
        if detect(im) == 1: 
            chel.append(nt.basename(adr))
        else: 
            man.append(nt.basename(adr))
    for i in range(len(chel)):
        chel[i]=chel[i][0]
    for i in range(len(man)):
        man[i]=man[i][0]

adr1 = "C:\\Users\\Navid\\Desktop\\codmod\\Images\\*.jpg"
chel = []
man = []
extract(adr1)
conf = confusion(man,chel)

print('tp=',conf[0],'fp=',conf[1],'fn=',conf[2],'tn=',conf[3])
print('recall=',recall(conf[0],conf[2]))
print('percision',percision(conf[0],conf[1]))
print('accuracy',accuracy(conf[0],conf[3],conf[1],conf[2]))

