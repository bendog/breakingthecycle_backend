from rest_framework import serializers
from django.apps import apps


class DonationSerializer(serializers.ModelSerializer):
    
    donor = serializers.ReadOnlyField(source='donor.id')
    
    class Meta:
        model = apps.get_model('riders.Donation')
        fields = '__all__'


class RiderUpdateSerializer(serializers.ModelSerializer):

    rider_posting = serializers.ReadOnlyField(source='updates.rider_posting')
    
    class Meta:
        model = apps.get_model('riders.RiderUpdates')
        fields = "__all__"


class RiderSerializer(serializers.ModelSerializer):

    rider_owner = serializers.ReadOnlyField(source='rider_owner.id')

    class Meta:
        model = apps.get_model('riders.Rider')
        fields = '__all__'
        

class RiderDeSerializer(serializers.ModelSerializer):  

    rider = serializers.ReadOnlyField(source='id')
    # kms_ridden = serializers.SerializerMethodField()
    # kms_to_ride = serializers.SerializerMethodField()
    # amount_donated = serializers.SerializerMethodField()

    class Meta:
        model = apps.get_model('riders.Rider')      
        fields = ('rider', 'rider_owner', 'team', 'bio', 'avatar_image', 'background_image', 'is_active', 'date_created', 'rate', 'kms_ceiling', 'kms_ridden', 'kms_to_ride', 'amount_donated')

    # def get_kms_ridden(self, obj):
    #     rider_updates = apps.get_model('riders.RiderUpdates')
    #     updates_to_sum = rider_updates.objects.filter(
    #         rider_posting_id=obj.rider_owner_id
    #         )
    #     kms_ridden = 0
    #     for update in updates_to_sum:
    #         kms_ridden += update.kms_ridden
    #
    #     return(kms_ridden)
    #
    # def get_kms_to_ride(self, obj):
    #     rider_donations = apps.get_model('riders.Donation')
    #     rate = obj.rate
    #     donations_to_sum = rider_donations.objects.filter(
    #         rider_id=obj.rider_owner_id
    #     )
    #     donation_sum = 0
    #     for donation in donations_to_sum:
    #         donation_sum += donation.amount
    #
    #     kms_to_ride = rate * donation_sum
    #
    #     return(kms_to_ride)
    #
    # def get_amount_donated(self, obj):
    #     rider_donations = apps.get_model('riders.Donation')
    #     donations_to_sum = rider_donations.objects.filter(
    #         rider_id=obj.rider_owner_id
    #     )
    #     donation_sum = 0
    #     for donation in donations_to_sum:
    #         donation_sum += donation.amount
    #     return(donation_sum)
    

class RiderDetailSerializer(RiderSerializer):
    donations = DonationSerializer(many=True, read_only=True)
    rider_updates = RiderUpdateSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.team = validated_data.get('team', instance.team)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar_image = validated_data.get('avatar_image', instance.avatar_image)
        instance.background_image = validated_data.get('background_image', instance.background_image)
        instance.is_active = validated_data.get('is_active', instance.background_image)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.kms_goal = validated_data.get('kms_goal', instance.kms_goal)
        instance.rider_owner = validated_data.get('rider_owner', instance.rider_owner)
        instance.save()
        return instance
    
    class Meta:
        model = apps.get_model('riders.Rider')
        fields = '__all__'
    
