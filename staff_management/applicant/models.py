from django.db import models
from django.utils.translation import ugettext_lazy as _
# from users.models import User
# Create your models here.
import datetime
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()


class District(models.Model):
    name = models.CharField(max_length=50,blank=True)
    admin = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class School(models.Model):
    SCHOOL_TYPE = (
        (1,'Highly accessible school'),
        (2,'Accessible Schools'),
        (5,'Highly Inaccessible Schools'),
        (4,'Inaccessible Schools'),
        )
    name = models.CharField(max_length=100,)
    code = models.CharField(max_length=50,)
    location = models.CharField(max_length=50,)
    district= models.ForeignKey(
        District, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )
    s_type = models.IntegerField(choices=SCHOOL_TYPE,blank=True) 
    # s_points = models.IntegerField(max_length=3,)
    
    def __str__(self):
        return self.name

class ApplicantUser(models.Model):
    CHRONIC_CHOICES = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )
    DIS_CHOICES = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )
    CHILD_DIS_CHOICES = (
        ('yes','YES'),
        ('no','NO'),
    )
    MARITAL_CHOICES = (
        ('married','MARRIED'),
        ('unmarried','SINGLE'),
    )
    GENDER_CHOICES = (
        ('male','MALE'),
        ('female','FEMALE'),
        )

    email = models.OneToOneField(User,on_delete=models.PROTECT,null=True,blank=True,related_name='applicant_email')
    full_name = models.CharField(max_length=50,blank=True,null=True)
    mobile = models.CharField(max_length=50,blank=True,null=True)

    aadhaar = models.CharField(max_length=50,null=True)#validators=[self.validate_length],)
    chronic_disease     = models.CharField(max_length=30, choices=CHRONIC_CHOICES,null=True)
    child_disease       = models.CharField(max_length=30, choices=CHILD_DIS_CHOICES,null=True)
    disabled            = models.CharField(max_length=30,choices=DIS_CHOICES,null=True)
    gender              = models.CharField(max_length=30,choices=GENDER_CHOICES,null=True)
    dob                 = models.DateField(_('dob'),null=True) 
    age                 = models.CharField(_('age'),max_length=15,null=True,blank=True)
    marital_status      = models.CharField(max_length=30,choices=MARITAL_CHOICES,default='single',null=True)
    district            = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    school              = models.ForeignKey(School,on_delete=models.PROTECT,null=True,blank=True,related_name="applicant_school")
    join_date           = models.DateField(_('join_date'),null=True)
    experience          = models.IntegerField(_('experience'),null=True)
    au_points           = models.IntegerField(_('points'),null=True,blank=True)
    direct_eligible     = models.BooleanField(default=False,null=True)
    
    # def age(self):
    #   return self.age
    
    # def experience(self):
        
    #   return self.experience
    # @property
    # def au_points(self,*args,**kwargs):
    #   self.au_points = self.school.s_points
    #   return self.au_points

    def save(self, *args, **kwargs):
        if self.dob:
            self.age = int((datetime.date.today() - self.dob).days / 365.25)
        if self.join_date:
            self.experience = int((datetime.date.today() - self.join_date).days/ 365.25)
        if self.school:
            self.au_points = self.school.s_type

        if self.chronic_disease=='yes' or self.child_disease =='yes':
            self.direct_eligible =True
        elif self.experience and self.experience >=8:
            self.direct_eligible=True
        else:
            self.direct_eligible =False

        if not self.direct_eligible:
            if self.marital_status=='unmarried' and self.gender=='female':
                self.au_points = self.au_points+5 
            if self.disabled == 'yes':
                self.au_points = self.au_points+10


        super(ApplicantUser, self).save(*args, **kwargs)

    # def __STR__(self):
    #   return self.email

        # if not self.id:
        #   super(ApplicantUser, self).save(*args, **kwargs)
        # else:
        #   qs = ApplicantUser.objects.filter(id=self.id)
        #   if qs.marital_status=='unmarried' and qs.gender=='female':
        #       qs.au_points = qs.au_points+5 
        #   if qs.disabled == 'yes':
        #       qs.au_points = qs.au_points + 10
        #   if (qs.chronic_disease|qs.child_disease)=='yes' 
        #       qs.direct_eligible =True

        # super(ApplicantUser, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_applicantuser(sender, instance, created, **kwargs):
    if created:
        ApplicantUser.objects.get_or_create(email=instance)

@receiver(post_save, sender=User)

def save_user_applicantuser(sender, instance, **kwargs):
    instance.applicant_email.save()