# -*- coding: utf-8 -*-
from .models import Madurez
from model_report.report import reports, ReportAdmin


class MadurezReport(ReportAdmin):
    title = ('Reporte de madurez')
    model = Madurez
    fields = [
        'grado__nombre',
        'fecha',
        'registro__control__nombre',
        'registro__resultado',
        'registro__control__dominio__nombre',
        'registro__control__dominio__metodologia__nombre',
        ]
    list_order_by = ('grado',)
    type = 'chart'
    char_type = 'pie'

reports.register('madurez-report', MadurezReport)
