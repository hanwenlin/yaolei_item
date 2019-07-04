from django.db import models
from django.forms import Form,ModelForm

# Create your models here.
#
# class MeterialsForm(ModelForm):
#     meterialName = models.CharField(max_length=20)      # 填料名称
#     meterialType = models.CharField(max_length=20)      # 填料类型
#     brand = models.CharField(max_length=20)             # 厂家
#     matrix = models.CharField(max_length=40)            # 基质
#     ligand = models.CharField(max_length=10)            # 功能基团
#     diameter = models.CharField(max_length=10)          # 直径
#     tolePressure = models.CharField(max_length=10,blank=True)      # 耐受压力类型
#     phRange = models.CharField(max_length=10,blank=True)           # PH范围
#     storeMethod = models.CharField(max_length=20,blank=True)       # 保存方法
#     comFactor = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)                     # 压缩因子
#     dbc = models.CharField(max_length=10,blank=True)               # DBC(mg/ml)
#     capacityRange = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)             # 项目生产载量范围
#     velocityPressure = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)          # 装柱最大流速压力
#     validtyPeriod = models.CharField(max_length=20,blank=True)         #有效期
#     packingMethod = models.CharField(max_length=5,blank=True)         #装柱方法   ABCDE
#     packingdetail = models.CharField(max_length=100,blank=True)