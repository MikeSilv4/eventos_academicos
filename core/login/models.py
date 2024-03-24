from django.db import models


class events(models.Model):

    idevento = models.CharField(primary_key=True, null=False)
    txnomeevento = models.CharField(max_length=128, null=False)
    txdescricaoevento = models.CharField(max_length=512, null=True)
    dtinicialevento = models.DateField(null=False)
    dtfinalevento = models.DateField(null=False)
    hrinicialevento = models.TimeField(null=False)
    hrfinalevento = models.TimeField(null=False)
    numinimoparticipante = models.IntegerField(null=True)
    numaximoparticipante = models.IntegerField(null=True)
    nuparticipantes = models.IntegerField(null=False)
    vlinscricaoevento = models.DecimalField(max_digits=10, decimal_places=8, null=False)
    txlocalevento = models.TextField(null=False)


    class Meta:
        managed = True
        db_table = 'events'


class organizer(models.Model):

    idorganizador = models.CharField("idorganizador", primary_key=True, null=False)
    txcpforganizador = models.CharField("txcpforganizador", max_length=14, null=False)
    txnomeorganizador = models.CharField("txnomeorganizador", max_length=256, null=False)
    txsenhaorganizador = models.CharField("txsenhaorganizador", max_length=10, null=False)
    txemailorganizador = models.CharField("txemailorganizador", max_length=256, null=False)
    dtnascimentoorganizador = models.DateField("dtnascimentoorganizador", null=False)

    #foreignKeys
    eventoid = models.ForeignKey(events, on_delete=models.CASCADE, null=False)

    class Meta:
        managed = True
        db_table = 'organizer'