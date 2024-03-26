from django.db import models


class events(models.Model):

    idevento = models.AutoField("idevento", primary_key=True, null=False)
    txnomeevento = models.CharField("txnomeevento", max_length=128, null=False)
    txdescricaoevento = models.CharField("txdescricaoevento", max_length=512, null=True)
    dtinicialevento = models.DateField("dtinicialevento", null=False)
    dtfinalevento = models.DateField("dtfinalevento", null=False)
    hrinicialevento = models.TimeField("hrinicialevento", null=False)
    hrfinalevento = models.TimeField("hrfinalevento", null=False)
    numinimoparticipante = models.IntegerField("numinimoparticipante", null=True)
    numaximoparticipante = models.IntegerField("numaximoparticipante", null=True)
    nuparticipantes = models.IntegerField("nuparticipantes", null=False)
    vlinscricaoevento = models.DecimalField("vlinscricaoevento", max_digits=10, decimal_places=2, null=False)
    txlocalevento = models.TextField("txlocalevento", null=False)

    class Meta:
        managed = True
        db_table = 'events'


class organizer(models.Model):

    idorganizador = models.AutoField("idorganizador", primary_key=True, null=False)
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


class participant(models.Model):

    idparticipante = models.AutoField("idparticipante", primary_key=True, null=False)
    txcpfparticipante = models.CharField("txcpfparticipante", max_length=14, null=False)
    txnomeparticipante = models.CharField("txnomeparticipante", max_length=256, null=False)
    txsenhaparticipante = models.CharField("txsenhaparticipante", max_length=10, null=False)
    txemailparticipante = models.CharField("txemailparticipante", max_length=256, null=False)
    dtnascparticipante = models.DateField("dtnascparticipante", null=False)

    class Meta:
        managed = True
        db_table = 'participant'


class participants_events(models.Model):

    idpresenca = models.AutoField("idpresenca", primary_key=True, null=False)
    presenca = models.BooleanField("presenca", null=False)
    
    #foreignKeys
    participanteid = models.ForeignKey(participant, on_delete=models.DO_NOTHING, null=False)
    eventoid = models.ForeignKey(events, on_delete=models.DO_NOTHING, null=False)


    class Meta:
        managed = True
        db_table = 'participants_events'