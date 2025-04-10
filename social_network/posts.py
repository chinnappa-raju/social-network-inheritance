from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text=text
        self.timestamp=timestamp

    def set_user(self, user):
        self.user=user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        self.text=text
        self.timestamp=timestamp.strftime("%A, %b %d, %Y")
        self.user=None

    def __str__(self):
#        dateform=self.timestamp.strftime("%A, %b %d, %Y")
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp)

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text=text
        self.image_url=image_url
        self.timestamp=timestamp.strftime("%A, %b %d, %Y")

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp)
    
class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude=latitude
        self.longitude=longitude
        self.timestamp=timestamp.strftime("%A, %b %d, %Y")
    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp)