from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import psycopg2


def paint(request):
    if request.method == 'GET':
        return render(request, 'paint.html')
    if request.method == 'POST':
        filename = request.POST['fname']
        data = request.POST['data']
        '''conn = psycopg2.connect(database="djangopaint", user="nidhin")
        cur = conn.cursor()
        cur.execute("INSERT INTO files(name, image) VALUES(%s, %s)", [filename, data])
        conn.commit()
        conn.close()
        '''
        return HttpResponseRedirect('/')


