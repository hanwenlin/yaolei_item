from django.db import models

# Create your models here.

class ApplicationTable(models.Model):
    productnumber = models.CharField(max_length=50,verbose_name='项目号')
    producttime = models.DateTimeField(verbose_name='生产时间',auto_now_add=True)
    editorstaff = models.CharField(max_length=20,verbose_name='编辑人')
    resinname = models.CharField(max_length=50,verbose_name='填料名称')
    cycletime = models.CharField(max_length=10,verbose_name='循环次数')
    public = models.CharField(max_length=10,verbose_name='是否专用')
    diameter = models.CharField(max_length=10,verbose_name='层析柱直径')
    height = models.CharField(max_length=10,verbose_name='柱高')
    volumn = models.CharField(max_length=10,verbose_name='填料体积')
    storage = models.CharField(max_length=10,verbose_name='保存液')
    hetp = models.CharField(max_length=10,verbose_name='柱效')
    AS = models.CharField(max_length=10,verbose_name='对称因子')
    nppeditorstaff = models.CharField(max_length=10,verbose_name='NPP编辑人')
    cat = models.CharField(max_length=10,verbose_name='填料货号')
    lot = models.CharField(max_length=10,verbose_name='填料批号')
    expire = models.CharField(max_length=10,verbose_name='填料有效期')
    resinid = models.CharField(max_length=10,verbose_name='填料编号')
    usedtime = models.CharField(max_length=10,verbose_name='填料已使用次数')
    feedbackeditor = models.CharField(max_length=10,verbose_name='反馈编辑人')
    maxpressure = models.CharField(max_length=10,verbose_name='最大压力')
    maxvictory =  models.CharField(max_length=10,verbose_name='最大力量')

