# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from .services import integerToRoman


def index(request):
    return HttpResponse(integerToRoman(1))
