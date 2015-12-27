from django.shortcuts import render
import datetime

def home_page(reques):
	return render(reques, 'home_page.html', {})