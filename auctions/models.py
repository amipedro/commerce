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
    title = models.CharField(max_length=64)
    starting_price = models.DecimalField(max_digits=12, decimal_places=2, default="0")
    current_price = models.DecimalField(max_digits=12, decimal_places=2, default="0")
    condition = models.CharField(
        max_length=14,
        choices=CONDITION_CHOICES,
        default=BRAND_NEW
    )
    description = models.TextField(max_length=1024, blank=True, null=True)
    image_url = models.CharField(max_length=256, blank=False, null=False)
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default=HG
    )
    zip_code = models.IntegerField(default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #User.objects.get(id=id)
    creation_date = models.DateTimeField(default=now, editable=False)
    is_closed = models.BooleanField(default=False)
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="highest_bidder", null=True, blank=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner", null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.current_price} by {self.owner}"

# Bid model
class Bid(models.Model):
    bidding_id = models.BigAutoField(primary_key=True)
    bidding_product = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="product")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="_Id")
    bid = models.DecimalField(max_digits=12, decimal_places=2, default="0")
    bid_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidding_id}, {self.bidder}, $ {self.bid} || {self.bidding_product} "

# Comment model
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.TextField(max_length=256)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listed_commentary")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.comment} by {self.commenter_id} on {self.listing_id} at {self.comment_date}"

# Watchtlist model

class Watchlist(models.Model):
    watched_id = models.BigAutoField(primary_key=True)
    watcher = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


# Form for listing
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'starting_price', 'condition', 'description', 'image_url', 'category', 'zip_code']


# Categories model
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=32, blank=True)
    
    def __str__(self):
        return f"{self.category}"