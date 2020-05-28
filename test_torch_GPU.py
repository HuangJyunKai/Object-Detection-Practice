#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:17:24 2019

@author: aaron-lab
"""
import torch
print(torch.__version__)
print("torch GPU :",torch.cuda.is_available())
print("torch.cuda.current_device()",torch.cuda.current_device())
print("torch.cuda.get_device_name(0)",torch.cuda.get_device_name(0))
print("torch.cuda.device_count()",torch.cuda.device_count())