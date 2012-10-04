from django.db import models

class Guest(models.Model):
    
    CATEGORIES = (
        ('WP', 'Wedding Party'),
        ('F', 'Family'),
        ('W', 'Work'),
        ('FR', 'Friends'),
    )
    
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    category        = models.CharField(max_length=255, choices=CATEGORIES)
    maybe           = models.BooleanField()
    under_21        = models.BooleanField()
    sent_save_the_date  = models.BooleanField(verbose_name="Sent 'Save the Date'")
    sent_invite         = models.BooleanField(verbose_name="Sent Invite")
    sent_bridal_shower_invite         = models.BooleanField(verbose_name="Sent Bridal Shower Invite")
    notes           = models.TextField(blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return u'%s %s' %(self.first_name, self.last_name)

class RSVP(models.Model):
    NUMBER_GUESTS = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    ATTENDING = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    MEALS = (
        ('P', 'Black Angus Prime Rib'),
        ('C', 'Stuffed Chicken Breast'),
        ('S', 'Stuffed Haddock'),
        ('A', 'Penne in Pomodoro'),
        ('K', 'Kids Chicken Fingers'),
    )

    attending = models.CharField(choices=ATTENDING, verbose_name='Will you be attending?', max_length=255)
    number_of_guests = models.IntegerField(choices=NUMBER_GUESTS, null=True, blank=True)
    
    guest_1_first_name = models.CharField(max_length=255)
    guest_1_last_name = models.CharField(max_length=255)
    guest_1_meal = models.CharField(choices=MEALS, max_length=255, blank=True, null=True)
    guest_1_over_21 = models.BooleanField()
    guest_1_table = models.IntegerField(blank=True, null=True)

    guest_2_first_name = models.CharField(max_length=255, blank=True, null=True)
    guest_2_last_name = models.CharField(max_length=255, blank=True, null=True)
    guest_2_meal = models.CharField(choices=MEALS, max_length=255, blank=True, null=True)
    guest_2_over_21 = models.BooleanField()
    guest_2_table = models.IntegerField(blank=True, null=True)

    guest_3_first_name = models.CharField(max_length=255, blank=True, null=True)
    guest_3_last_name = models.CharField(max_length=255, blank=True, null=True)
    guest_3_meal = models.CharField(choices=MEALS, max_length=255, blank=True, null=True)
    guest_3_over_21 = models.BooleanField()
    guest_3_table = models.IntegerField(blank=True, null=True)

    guest_4_first_name = models.CharField(max_length=255, blank=True, null=True)
    guest_4_last_name = models.CharField(max_length=255, blank=True, null=True)
    guest_4_meal = models.CharField(choices=MEALS, max_length=255, blank=True, null=True)
    guest_4_over_21 = models.BooleanField()
    guest_4_table = models.IntegerField(blank=True, null=True)

    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%d for %s %s' % (self.number_of_guests, self.guest_1_first_name, self.guest_1_last_name)

    class Meta:
        verbose_name = 'RSVP'
