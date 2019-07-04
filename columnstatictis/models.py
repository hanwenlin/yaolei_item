from django.db import models
from material.models import ResinLabel

# Create your models here.

class PressureandVelocity(models.Model):
    resin = models.ForeignKey(ResinLabel,related_name='materisesin',on_delete=models.CASCADE,verbose_name='填料id')
    packingproject = models.CharField(max_length=20,verbose_name='装柱项目',blank=True)  #整型 3，4
    columnid = models.CharField(max_length=50,verbose_name='层析柱编号',blank=True)
    resinid = models.CharField(max_length=50,verbose_name='填料编号',blank=True)
    minipackingvelocity = models.CharField(max_length=20,verbose_name='最低装柱流速',blank=True)  # 整型或者NA
    maxpackingvelocity = models.CharField(max_length=20,verbose_name='最高装柱流速',blank=True)  # 整型或者NA
    packingpressure = models.CharField(max_length=20,verbose_name='装柱压力',blank=True)  #浮点数 2位
    productionvelocity = models.CharField(max_length=20,verbose_name='生产流速',blank=True)  #整型 或者NA
    columnheight = models.CharField(max_length=20,verbose_name='柱高',blank=True)       #浮点数或者NA
    columndimeter = models.CharField(max_length=20,verbose_name='层析柱直径',blank=True) #浮点数或者na
    symmetry = models.CharField(max_length=20,verbose_name='对称性',blank=True)   #浮点数或na
    hetp = models.CharField(max_length=20,verbose_name='HETP',blank=True)  #浮点数3位
    comment = models.CharField(max_length=1000,verbose_name='备注',blank=True)

