from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils.html import format_html


class personal_details(models.Model):
    f_name              = models.CharField("First name", max_length=50)
    l_name              = models.CharField("Last name",max_length=50)
    job_title           = models.CharField("job title", max_length=50)
    email               = models.EmailField("email", max_length=254)
    phone_number        = models.CharField("phone Number", max_length=50)
    birthday            = models.DateField("birthday", auto_now=False, auto_now_add=False)
    address             = models.CharField("address", max_length=50)
    education           = models.CharField("education", max_length=50)
    status              = models.CharField("work status", max_length=50)
    website             = models.URLField("your website", max_length=200)
    about_me            = models.TextField()
    image_profile       = models.ImageField("profile", upload_to=None, height_field=None, width_field=None, max_length=None)  
    def __str__(self):
        return self.l_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'personal detail'
        verbose_name_plural = 'personal details'

class set_user(models.Model):
    user    =  models.OneToOneField(personal_details, verbose_name="user", on_delete=models.CASCADE)
    def __str__(self):
        return self .user.l_name

class social_media_links(models.Model):
    """Model definition for social_media_links."""

    # TODO: Define fields here
    user            = models.OneToOneField(personal_details, verbose_name="social links", on_delete=models.CASCADE)
    instagram       = models.CharField("Instagram Link", max_length=50)
    twitter         = models.CharField("twitter Link", max_length=50)
    telegram        = models.CharField("telegram Link", max_length=50)
    linkedin        = models.CharField("linkedin Link", max_length=50)
    facebook        = models.CharField("facebook Link", max_length=50)

    class Meta:
        """Meta definition for social_media_links."""

        verbose_name = 'social_media_links'
        verbose_name_plural = 'social_media_linkss'

    def __str__(self):
        """Unicode representation of social_media_links."""
        return self.user.l_name

class resume(models.Model):
    resume_file = models.FileField("Resume Files", upload_to=None, max_length=100)
    User        = models.ForeignKey(personal_details, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.User.l_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'resume'
        verbose_name_plural = 'resumes'


class skills(models.Model):
    skill       = models.CharField("skill", max_length=50)
    percent     = models.PositiveIntegerField(
        default=10,validators=[MinValueValidator(0),MaxValueValidator(100)])
    User        = models.ForeignKey(personal_details, on_delete=models.CASCADE) 

    def __str__(self):
        return self.User.l_name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'skills'
        verbose_name_plural = 'skillss'

    def percentage_skill(self):
        if self.percent:
            percentage = round((self.percent), 2)
        else:
            percentage = 0
        return format_html(
            '''
            <progress value="{0}" max="100">{0}%</progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            percentage
        )
        