from google_images_search import GoogleImagesSearch
import zipfile
import os

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch(
    'AIzaSyBpIAcN5IIIcmfLwGq3j6fAV5QkW6vn4N0', '2e5dded9ae895e14b', validate_images=True)


# define search params:
def search(keyword, imageNumber):
    _search_params = {
        'q': keyword,
        'num': imageNumber,
        # 'safe': 'medium',
        # 'fileType': 'jpg',
        # 'imgType': 'photo',
        # 'imgSize': 'MEDIUM',
        # 'imgDominantColor': 'brown',
        # 'rights': 'cc_publicdomain'
    }
    gis.search(search_params=_search_params, path_to_dir='./images/')

    handle = zipfile.ZipFile('images.zip', 'w')

    os.chdir('./images/')

    for x in os.listdir():
        handle.write(x, compress_type=zipfile.ZIP_DEFLATED)
        os.remove(x)

    handle.close()
    os.chdir("../")

    os.rmdir("./images/")

    # for files in os.walk('./'):
    #     for imagefile in files:
    #         return imagefile.endswith('.zip')
