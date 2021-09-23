import pandas as pd
import gdown
import shutil
from PIL import Image

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

block_template = """
<figure class="photo" style="display:inline-block;margin:20px;">
    <img src="{}" alt="{}" style="vertical-align:top;width:120px;" />
    <figcaption style="text-align:center;">
        <a href="{}">{}</a>
    </figcaption>
</figure>
"""

df = pd.read_csv('scripts/data/profile.csv')
df.columns = ["Timestamp", "name", "position", "web", "photo"]
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df[df.Timestamp >= pd.to_datetime("2021-09-16 17:10:41")]

# clean photo url and only leave photo id
df.photo = df.photo.apply(lambda x: x[33:])
df['name_p'] =  df.name.apply(lambda x: x.replace(' ', '_'))

# download photos
url = 'https://drive.google.com/uc?id='
photo_dir = "static/"
photo_path = []
for name_p, photo_id in zip(df.name_p, df.photo):
    name_from_url = gdown.download(url+photo_id, quiet=False)
    print(name_from_url)
    dot_index = name_from_url.find('.')
    file_type = name_from_url[dot_index:]
    print(file_type)
    rename = name_p + file_type
    shutil.move(name_from_url, photo_dir + rename)

    # cropped center
    im = Image.open(photo_dir + rename)
    short_side = min(im.size)
    im_cropped = crop_center(im, short_side, short_side)
    im_cropped.save(photo_dir + rename, quality=95)

    photo_path.append(rename)

df['photo_path'] = photo_path

positions = ['Postdoc', 'PhD', 'Master', 'Undergrad']

for p in positions:
    print(f"=== {p} ===")    
    tmp_df = df[df.position == p]
    for _, row in tmp_df.iterrows():
        # print(row)
        print(
            block_template.format(
                row.photo_path,
                row.name_p,
                row.web,
                row['name'],
            )
        )
