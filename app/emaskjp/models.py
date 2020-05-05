from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class PrefectureMaster(models.Model):
    # Prefecture Master
    name = models.CharField('Prefecture', max_length=50)


class Entity(models.Model):
    # Legan Entity
    entity_name = models.CharField(
        verbose_name='医療機関名', max_length=200,
        blank=False,
        validators=[MinLengthValidator(2)]
    )
    zip_code = models.CharField(
        verbose_name='zip_code',  # this is displayed in html form
        max_length=8,
        blank=True,
    )
    prefecture = models.CharField(
        verbose_name='都道府県', max_length=40,
        blank=False,
        validators=[MinLengthValidator(3)]
    )
    address1 = models.CharField(
        verbose_name='市区町村番地', max_length=40,
        blank=False,
    )
    address2 = models.CharField(
        verbose_name='建物名', max_length=40,
        blank=True,
    )

    def __str__(self):
        return self.entity_name


class Demand(models.Model):
    entity = models.ForeignKey(
        Entity,
        on_delete=models.CASCADE,)
    begin_date = models.DateField(
        blank=False,
        null=False
    )
    begin_date_display = models.CharField(
        verbose_name='年/月', max_length=40, null=True, blank=True)
    demand_qty = models.DecimalField(max_digits=16, decimal_places=6)

    class Meta:
        unique_together = (('entity', 'begin_date'),)

    def __str__(self):
        return self.begin_date


class Supplier(models.Model):
    name = models.CharField(max_length=200, blank=False,
                            validators=[MinLengthValidator(2)])
    zip_code = models.CharField(
        verbose_name='zip_code',  # this is displayed in html form
        max_length=8,
        blank=True,
    )
    prefecture = models.CharField(
        blank=True, max_length=40, verbose_name='都道府県', )
    address1 = models.CharField(verbose_name='市区町村番地', max_length=40,
                                blank=False,)
    address2 = models.CharField(verbose_name='建物名', max_length=40,
                                blank=True,)


class SupplierContact(models.Model):
    supplier = models.ForeignKey(
        Supplier, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True,)
    email = models.EmailField(max_length=200, blank=False)
    phone = PhoneNumberField(blank=True)


class Supply(models.Model):
    destination_entity = models.ForeignKey(
        Entity, on_delete=models.DO_NOTHING,)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING,)
    begin_date = models.DateField(blank=False, null=False)
    supply_qty = models.DecimalField(max_digits=16, decimal_places=6)

    class Meta:
        unique_together = (('destination_entity', 'supplier', 'begin_date'),)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # update of create
        Request, created = Request.objects.update_or_create(
            entity=destination_entity,
            begin_date=begin_date,
        )
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def __str__(self):
        return self.begin_date


class SupplyRequest(models.Model):
    entity = models.ForeignKey(
        Entity, on_delete=models.CASCADE)
    begin_date = models.DateField(blank=False, null=False)
    request_qty = models.DecimalField(max_digits=16, decimal_places=6)
    last_update = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    last_calculated = models.DateTimeField(
        blank=True, null=True, default=(timezone.datetime.now() - timezone.timedelta(days=1)))
    # When supply created, request created or updated last_update.
    # Every 1 minutes, if last_update > last_calculated or last_update is null,
    # run update().

    class Meta:
        unique_together = (('entity', 'begin_date'),)
