from django.db import models

class social_media_links(models.Model):
    """Model definition for social_media_links."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for social_media_links."""

        verbose_name = 'social_media_links'
        verbose_name_plural = 'social_media_linkss'

    def __str__(self):
        """Unicode representation of social_media_links."""
        pass

    def save(self):
        """Save method for social_media_links."""
        pass

    def get_absolute_url(self):
        """Return absolute url for social_media_links."""
        return ('')

    # TODO: Define custom methods here


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
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'personal detail'
        verbose_name_plural = 'personal details'