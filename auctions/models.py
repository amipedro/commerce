from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.timezone import now
from django.conf import settings


from django.forms import ModelForm


# User Model
class User(AbstractUser):
    id = models.AutoField(primary_key=True)


# Listing model with all required database fields
class Listing(models.Model):
    BRAND_NEW = 'Brand new'
    LIKE_NEW = 'Like new'
    USED = 'Used'
    REFURBISHED = 'Refurbished'
    REMANUFACTURED = 'Remanufactured'
    FOR_PARTS = 'For parts'

    CONDITION_CHOICES = [
    (BRAND_NEW, 'Brand new'), (LIKE_NEW, 'Like new'), (USED, 'Used'),
    (REFURBISHED, 'Refurbished'), (REMANUFACTURED, 'Remanufactured'), (FOR_PARTS, 'For parts')
    ]

    BO = "Books"
    BI = "Business & Industrial"
    CA = "Clothing, Shoes & Accessories"
    CO = "Collectibles"
    CE = "Consumer Electronics"
    CR = "Crafts"
    DB = "Dolls & Bears"
    HG = "Home & Garden"
    MO = "Motors"
    PS = "Pet Supplies"
    SG = "Sporting Goods"
    SM = "Sports Mem, Cards & Fan Shop"
    TH = "Toys & Hobbies"
    AT = "Antiques"
    CN = "Computers/Tablets & Networking"

    CATEGORY_CHOICES = [
    (BO, "Books"), (BI, "Business & Industrial"), (CA, "Clothing, Shoes & Accessories"), (CO, "Collectibles"),
    (CE, "Consumer Electronics"), (CR, "Crafts"), (DB, "Dolls & Bears"), (HG, "Home & Garden"), (MO, "Motors"), (PS, "Pet Supplies"),
    (SG, "Sporting Goods"), (SM, "Sports Mem, Cards & Fan Shop"), (TH, "Toys & Hobbies"), (AT, "Antiques"), (CN, "Computers/Tablets & Networking")
    ]

    listing_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64)
    starting_price = models.DecimalField(max_digits=12, decimal_places=2, default="0")
    current_price = models.DecimalField(max_digits=12, decimal_places=2, default="0")
    condition = models.CharField(
        max_length=14,
        choices=CONDITION_CHOICES,
        default=BRAND_NEW
    )
    description = models.CharField(max_length=1024, blank=True, null=True)
    image_url = models.CharField(max_length=256, blank=False, null=False)
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default=HG
    )
    zip_code = models.IntegerField(default="00000")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #User.objects.get(id=id)
    creation_date = models.DateTimeField(default=now, editable=False)
    is_closed = models.BooleanField(default=False)
    winner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.current_price} by {self.owner}"

# Bid model
class Bid(models.Model):
    bidding_id = models.AutoField(primary_key=True)
    bidding_product = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="product")
    highest_bidder_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="_Id")
    highest_bid = models.DecimalField(max_digits=12, decimal_places=2, default="0")

    def __str__(self):
        return f"{self.bidding_id}, {self.highest_bidder_id}, {self.highest_bid}"

# Comment model
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    commenter_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.CharField(max_length=128)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listed_commentary")
    
    def __str__(self):
        return f"{self.comment} by {self.commenter_id} on {self.listing_id}"

'''
# Image model. A single image will be saved at time.
class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listed_image")
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return f"{self.image_id}"


# Form for image
class ImagesForm(ModelForm):
    class Meta:
        model = Images
        fields = ['image']
'''

# Form for listing
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'starting_price', 'condition', 'description', 'image_url', 'category', 'zip_code']