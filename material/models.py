from django.db import models

# Create your models here.

class ResinLabel(models.Model):
    resinName = models.CharField(max_length=50,verbose_name='填料名称')      # 填料名称     # resinName
    resinaType = models.CharField(max_length=50,verbose_name='填料类型')      # 填料类型      # resinaType
    brand = models.CharField(max_length=50,verbose_name='厂家')             # 厂家
    matrix = models.CharField(max_length=50,verbose_name='基质')            # 基质
    ligand = models.CharField(max_length=50,verbose_name='功能基团')            # 功能基团
    diameter = models.CharField(max_length=10,verbose_name='粒径(um)')          # 直径(粒径)  int整型
    Pmax = models.CharField(max_length=10,blank=True,verbose_name='耐受压力')      # 耐受压力  #Pmax 浮点数 2位小数点
    phRange = models.CharField(max_length=10,blank=True,verbose_name='PH范围')           # PH范围  #phRange
    storageMethod = models.CharField(max_length=100,blank=True,verbose_name='保存方法')       # 保存方法  #storageMethod
    #comFactor = models.DecimalField(max_digits=5, decimal_places=2,blank=True)                     # 压缩因子 null=True不能要，否则空的时候不是这个类型了
    compactFactor = models.CharField(max_length=10,blank=True,verbose_name='压缩因子')   #compactFactor  浮点数 两位小数点
    dbc = models.CharField(max_length=10,blank=True,verbose_name='DBC(mg/ml)')               # DBC(mg/ml)  # 整型
   # capacityRange = models.DecimalField(max_digits=5, decimal_places=2,blank=True)             # 项目生产载量范围
    LoadingRangeinProject = models.CharField(max_length=10,blank=True,verbose_name='项目生产载量范围')   # LoadingRangeinProject  #浮点数 2位小数位
    #velocityPressure = models.DecimalField(max_digits=5, decimal_places=2,blank=True)          # 装柱最大流速压力
    PackingVmaxandPmax = models.CharField(max_length=50,blank=True,verbose_name='装柱最大流速压力')   #PackingVmaxandPmax  字符串
    expiry = models.CharField(max_length=50,blank=True,verbose_name='有效期')         #有效期  expiry
    TypeofColomuPackingMethod = models.CharField(max_length=5,blank=True,verbose_name='装柱方法类型')         #装柱方法  TypeofColomuPackingMethod   ABCDE
    ColomuPackingMethod = models.CharField(max_length=1000,blank=True,verbose_name='装柱方法')        #装柱方法详细  ColomuPackingMethod  TextField
