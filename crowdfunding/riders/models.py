from django.db import models
from django.db.models import Sum
from django.db.models import OuterRef, Subquery
from django.contrib.auth import get_user_model



class Rider(models.Model):

    class KmsToDollar(models.IntegerChoices):
        KM_1 = 1, '1km'
        KM_2 = 2, '2km'
        KM_5 = 5, '5km'
    
    rider_owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user')
    team = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)
    avatar_image = models.URLField()
    background_image = models.URLField()
    is_active = models.BooleanField()
    date_created = models.DateTimeField()
    rate = models.PositiveIntegerField(choices=KmsToDollar.choices, default=KmsToDollar.KM_1, help_text="How may kms would you like to ride for each $ donated?")
    kms_ceiling = models.IntegerField()
   
    # @property
    # def calc_kms_ridden(self):
    #     total_kms_ridden = RiderUpdates.objects.aggregate(s=Sum('kms_ridden'))["s"]
    #     return(total_kms_ridden)

    @property
    def kms_ridden(self):
        return self.updates.all().aggregate(total=Sum('kms_ridden'))['total']
    
    # @property
    # def calc_amount_raised(self):
    #     donations = Donation.objects.select_related('rider')
    #     total_raised = donations.aggregate(s=Sum('amount'))["s"]
    #     return(total_raised)

    @property
    def amount_donated(self):
        return self.donations.aggregate(total=Sum('amount'))['total']
    
    # @property
    # def calc_kms_to_ride(self):
    #     donations = Donation.objects.select_related('rider')
    #     donation_kms = donations.aggregate(s=Sum('amount'))["s"]
    #     print(Rider.objects.get().rate)
    #     rate = Rider.objects.get().rate
    #     kms_to_ride = rate * donation_kms
    #     return(kms_to_ride)

    @property
    def kms_to_ride(self):
        return self.rate * self.amount_donated


class RiderUpdates(models.Model):
    rider_posting = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='updates')
    kms_ridden = models.IntegerField(null=True)
    description = models.CharField(max_length=300)
    image = models.URLField()


class Donation(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    rider = models.ForeignKey(Rider,
                              on_delete=models.CASCADE,
                              related_name='donations')
    donor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='donor')

