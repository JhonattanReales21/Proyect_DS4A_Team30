from flask import Flask
from flask import jsonify
from flask import request
import json
from data_fetch import get_s3_data
import pandas as pd

recoms = {
	'TUNJA': get_s3_data.get_s3_matrix('TUNJA'),
	'BARRANQUILLA': get_s3_data.get_s3_matrix('BARRANQUILLA'),
	'AGUACHICA': get_s3_data.get_s3_matrix('AGUACHICA')
}

user_groups = {key: recoms[key]['cliente'].unique() for key in recoms}


def recom_sys(city, user):
	if user is not None:
		if city is not None:
			users_list = []
			if city in recoms:
				users_list = user_groups[city]
				df_recoms = recoms[city]
			options = [{'label': int(i), 'value': int(i)} for i in sorted(users_list)]
			if user in users_list:
				resu = pd.DataFrame()
				resu['Recommended Articles'] = df_recoms[df_recoms['cliente'] == user]['recomendados']
				items_to_recommend_to_user = resu
			else:
				items_to_recommend_to_user = pd.DataFrame()
				items_to_recommend_to_user['Recommended Articles'] = ['None', 'None', 'None', 'None', 'None']
				#return items_to_recommend_to_user.to_dict('records'), options
			return items_to_recommend_to_user.to_dict('records'), options
		else:
			options = [{'label': "", 'value': ""}]
			resu = pd.DataFrame()
			resu['Recommended Articles'] = ['None', 'None', 'None', 'None', 'None']
			return resu.to_dict('records'), options
	else:
		if city is not None:
			users_list = []
			if city in recoms:
				users_list = user_groups[city]
			options = [{'label': int(i), 'value': int(i)} for i in sorted(users_list)]
			resu = pd.DataFrame()
			resu['Recommended Articles'] = ['None', 'None', 'None', 'None', 'None']
			return resu.to_dict('records'), options
		else:
			options = [{'label': "", 'value': ""}]
			resu = pd.DataFrame()
			resu['Recommended Articles'] = ['None', 'None', 'None', 'None', 'None']
			return resu.to_dict('records'), options


def create_app():
	the_app = Flask(__name__)
	return the_app


app = create_app()


@app.route('/api/v1/suggest/', methods=['POST'])
def get_suggestion():
	form = json.loads(request.data)
	r, o = [], []
	response = {}
	if not('city' in form):
		form['city'] = None
		response['Response'] = 'No city was given in POST request.'
		r, o = recom_sys(city=None, user=None)
		response['Recommended Articles'] = r
		response['Options'] = o
	elif not('user' in form):
		form['user'] = None
		response['Response'] = 'No user was given in POST request.'
		r, o = recom_sys(city=form['city'], user=None)
		response['Recommended Articles'] = r
		response['Options'] = o
	else:
		res = ''
		r, o = [], []
		try:
			r, o = recom_sys(city=form['city'], user=int(form['user']))
			res = 'Successful Request'
			response['Recommended Articles'] = r
			response['Options'] = o
		except Exception as e:
			res = '{}'.format(e)
			r = ['None', 'None', 'None', 'None', 'None']
			o = [{'label': "", 'value': ""}]
		finally:
			response['Response'] = res
			response['Recommended Articles'] = r
			response['Options'] = o
	return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)