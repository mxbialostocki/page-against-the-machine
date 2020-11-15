from django.db import models
from model_author import Author
from model_imprint import Imprint
from model_book import Publisher
from model_supplier import Supplier
# from model_primary_category import Primary_Category
# from model_subcategory import Subcategory
# from model_tag import Tag
# from model_illustrator import Illustrator
# from model_series import Series

"""
Plan to split this into primary title data and secondary title data for speed - particularly line 83 - line 91
"""

class Book(models.Model):
    """
    structural selection options here
    """
    format_choices = [
        (PB, 'Paperback'),
        (HB, 'Hardback'),
        (TP, 'Trade Paperback'),
        (BX, 'Boxed Set'),
        (MC, 'Miscellaneous'),
        (CA, 'Card')
    ]
    status_choices = [
        (ACT, 'Active'),
        (OP, 'Out of Print'),
        (SHT, 'It\'s Shit'),
        (JAN, 'Due January'),
        (FEB, 'Due February'),
        (MAR, 'Due March'),
        (APR, 'Due April'),
        (MAY, 'Due May'),
        (JUN, 'Due June'),
        (JUL, 'Due July'),
        (AUG, 'Due August'),
        (SEP, 'Due September'),
        (OCT, 'Due October'),
        (NOV, 'Due November'),
        (DEC, 'Due December'),
        (POD, 'Print on Demand'),
        (CAN, 'Cancelled')
    ]
    """
    individual data pointshere
    """
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField(Author)
    imprint = models.ForeignKey(Imprint)
    publisher = models.ForeignKey(Publisher)
    supplier = models.ForeignKey(Supplier)
    publication_date = models.DateField()
    date_created = models.DateTimeField('date created')
    # primary_department = models.ForeignKey(Primary_Department)
    # subcategory = models.ManyToManyField(Subcategory)
    # tags = models.ManyToManyField(Tag)
    # example https://hackernoon.com/how-to-add-tags-to-your-models-in-django-django-packages-series-1-4y1b32sf
    firm_sale = models.BooleanField(**options)
    no_discounting = models.BooleanField(**options)
    no_special_orders = models.BooleanField(**options)
    generic_item = models.BooleanField(**options)
    # stock management fields
    available = models.SmallIntegerField(default=0)
    on_hand = models.SmallIntegerField(default=0)
    draft = models.SmallIntegerField(default=0)
    holds = models.SmallIntegerField(default=0)
    special_orders = models.SmallIntegerField(default=0)
    approval = models.SmallIntegerField(default=0)
    on_order = models.SmallIntegerField(default=0)
    layby = models.SmallIntegerField(default=0)
    backorder = models.SmallIntegerField(default=0)
    minimum_number = models.SmallIntegerField(default=0)
    maximum_number = models.SmallIntegerField(default=0)
    # fiscal fields - to be converted to https://django-money.readthedocs.io/en/stable/ when possible
    retail_value = models.DecimalField(max_digits=8, decimal_places=2)
    sell_value = models.DecimalField(max_digits=8, decimal_places=2)
    cost_including_gst_value = models.DecimalField(max_digits=8, decimal_places=2)
    cost_excluding_gst_value = models.DecimalField(max_digits=8, decimal_places=2)
    margin = models.DecimalField(max_digits=8, decimal_places=2)
    # extraneous fields
    notes = models.TextField(**options)
    dewey_decimal_class = models.DecimalField(max_digits=16, decimal_plces=6)
    language = models.CharField(max_length=80)
    number_of_pages = models.SmallIntegerField(default=0)
    height_in_millimetres = models.DecimalField(max_digits=5, decimal_places=2)
    width_in_millimetres = models.DecimalField(max_digits=5, decimal_places=2)
    image_path_local = models.CharField(max_length=150)
    image_path_remote = models.URLField(max_length=250)

    book_format = models.CharField(
        max_length=2,
        choices=format_choices,
        default=PB
    )
    book_status = models.CharField(
        max_length=3,
        choices=status_choices,
        default=ACT
    )
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        db_table = 'books'
        app_label = 'patm'