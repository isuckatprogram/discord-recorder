from PIL import Image, ImageDraw, ImageFont
import urllib.request
import video



def construct_images(author, message, author_profile, photoID=0,
                     deleted=False):
    global id

    img = Image.new('RGB', (531, 78), color='#333')

    fnt = ImageFont.truetype('fonts/font.otf', 20)
    fnt2 = ImageFont.truetype('fonts/font.otf', 10)

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(author_profile, "assets/temporary.png")

    profile_picture = Image.open('assets/temporary.png', 'r')

    profile_picture = profile_picture.resize((50, 50))

    img_w, img_h = profile_picture.size
    bg_w, bg_h = img.size

    offset = (9, 10)

    name = ImageDraw.Draw(img)

    if deleted:
        name.text((70, 10),
                  f'{author} (DELETED)',
                  font=fnt,
                  fill=(255, 255, 0))
    else:
        name.text((70, 10), author, font=fnt, fill=(255, 255, 0))

    name.text((70, 37), message, font=fnt2, fill=(218, 219, 220, 1))

    img.paste(profile_picture, offset)


    img.save(f'assets/generated_images/frame-{photoID}.png')

    video.generate_video()
