from flask import Flask, request, render_template
import random, psycopg2

app=Flask(__name__)

@app.route('/')
def base():
	conn=psycopg2.connect(user='shaftr01', host='localhost', port=2345, dbname='world')
	curs=conn.cursor()
	curs.execute("select distinct governmentform from country")
	govform = [item[0] for item in curs.fetchall()]
	return render_template('index.html', govform=govform)

@app.route('/page1')
def page1():
	minpop=request.args.get('minpop')
	maxpop=request.args.get('maxpop')
	conn=psycopg2.connect(user='shaftr01', host='localhost', port=2345, dbname='world')
	curs=conn.cursor()
	curs.execute("select name, population from country where Population > "+ minpop + " and Population < "+ maxpop+" order by population asc")
	name = [item[0] for item in curs.fetchall()]
	curs.execute("select name, population from country where Population > "+ minpop + " and Population < "+ maxpop+" order by population asc")
	pop=[item[1] for item in curs.fetchall()]
	namepop={}
	for i in range(len(name)):
		namepop[name[i]]=pop[i]
	return render_template('page1.html', name=name, pop=pop, namepop=namepop, minpop=minpop, maxpop=maxpop)

@app.route('/page2')
def page2():
	govform=request.args.get('govform')
	conn=psycopg2.connect(user='shaftr01', host='localhost', port=2345, dbname='world')
	curs=conn.cursor()
	curs.execute("select name, lifeexpectancy from country where governmentform='"+govform+"'"+" order by lifeexpectancy asc")
	res = [item[0] for item in curs.fetchall()]
	curs.execute("select name, lifeexpectancy from country where governmentform='"+govform+"'"+" order by lifeexpectancy asc")
	life=[item[1] for item in curs.fetchall()]
	lifeexp={}
	for i in range(len(res)):
		lifeexp[res[i]]=life[i]
	return render_template('page2.html', res=res, govform=govform, lifeexp=lifeexp)

if __name__=='__main__':
	app.run(debug=True)