#! /usr/bin/python
# encoding:utf-8

# Create your tasks here

from __future__ import absolute_import,unicode_literals
from celery import shared_task

@shared_task
def add(x,y):
    return x+y


