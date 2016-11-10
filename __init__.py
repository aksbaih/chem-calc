from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path= '/static', template_folder='templates')

@app.route('/home', methods=['GET', 'POST'])
def home():
	method = request.method
	form = request.form
	if(method=='POST'):
		# Input
		f={"s": form['name1'], "n": int(form['num1'])}
		s={"s": form['name2'], "n": int(form['num2'])}

		# Validation
		if(f["n"] == 0 or s["n"] == 0):
			return render_template('home.html', formula='', message=1, form=form)
		if((f['n'] < 0 and s['n'] < 0)or(f['n'] > 0 and s['n'] > 0)):
			return render_template('home.html', formula='', message=2, form=form)
		
		# Swap
		n = f
		if(s['n'] > 0):
			f, s = s, n

		# Absolution
		s['n'] = s['n'] * -1

		# Minimization
		for i in range(2, f['n'] + 1):
			if(f['n'] % i == 0 and s['n'] % i == 0):
				f['n'], s['n'] = f['n'] / i, s['n'] / i
				i = 2

		# Parantheses
		if(f['s'].lower().capitalize() != f['s'] and s['n'] != 1):
			f['s'] = '(' + f['s'] + ')'
		if(s['s'].lower().capitalize() != s['s'] and f['n'] != 1):
			s['s'] = '(' + s['s'] + ')'

		return render_template('home.html', formula=f['s']+str(s['n'])+s['s']+str(f['n']) , message='', form=form)
	else:
		return render_template('home.html', formula='', message='', form=form)

@app.route('/')
def redi():
	return redirect('/home')

if __name__ == "__main__":
    app.debug = True
    app.run(port=3000)