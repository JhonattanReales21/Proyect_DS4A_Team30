from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from scripts import tabs, call_maps
from data_fetch import get_views, get_s3_data
import requests, json
from dash.exceptions import PreventUpdate

def return_callbacks(app):

	@app.callback(
		Output("app-content", "children"),
		[
			Input("tabs","value")
		]
	)
	def get_current_content(selected_tab):
		return tabs.create_content_tab(selected_tab)

 ##################################### cluster
	@app.callback(
		Output('cluster-dpdn', 'options'),
		Input('ciudades-dpdn', 'value')
		)

	def set_cities_options(chosen_state):
		clean2=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
		dff=clean2[clean2['ciudad_tienda']==chosen_state]
		return [{'label': c, 'value': c} for c in sorted(dff['cluster_id'].unique())]
########################Callbacks diagrama de torta
# Connect the Plotly graphs with Dash Components
	@app.callback(
		Output(component_id='fig1', component_property='figure'),
		Input(component_id='ciudades-dpdn', component_property='value'),
		Input(component_id='cluster-dpdn', component_property='value')
		)
	def update_graph(selected_ciudad,selected_cluster):
		clean=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
		df=clean[clean['ciudad_tienda']==selected_ciudad]
		df10=df['cluster_id'].unique()
		if selected_cluster is None :
			df2=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
			dff =df2[(df2['ciudad_tienda']==selected_ciudad)]
			fig = px.sunburst(dff, path=['canal','edad','tipo_articulo'], values='volumen_pesos', color='canal',title="Total sales  for the city of: {}".format(selected_ciudad))
			fig.update_traces(textinfo='label+percent entry')
			fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
		else:
			if selected_cluster in list(df10):
				df2=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
				dff =df2[(df2['ciudad_tienda']==selected_ciudad) & df2['cluster_id'].isin([selected_cluster])]
				fig = px.sunburst(dff, path=['canal','edad','tipo_articulo'], values='volumen_pesos', color='canal',title="Total sales  for the city of: {}".format(selected_ciudad))
				fig.update_traces(textinfo='label+percent entry')
				fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
			else:
				df2=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
				dff =df2[(df2['ciudad_tienda']==selected_ciudad)]
				fig = px.sunburst(dff, path=['canal','edad','tipo_articulo'], values='volumen_pesos', color='canal',title="Total sales  for the city of: {}".format(selected_ciudad))
				fig.update_traces(textinfo='label+percent entry')
				fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
		return fig
############################################################# parallel plot######
	@app.callback(
	Output('fig2', 'figure'),
	Input('cluster-dpdn', 'value'),
	Input('ciudades-dpdn', 'value'),
	Input('check','value')
	)
	def paral(selected_cluster, selected_ciudad,choose):
		clean=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
		df=clean[clean['ciudad_tienda']==selected_ciudad]
		df10=df['cluster_id'].unique()
		if selected_cluster is None :
			dff=get_views.get_view_by_name('paralell_plot_cluster')
			grupos=dff[(dff['ciudad_tienda']==selected_ciudad)]
			fig2 = px.parallel_categories(grupos, dimensions=choose,color="valor_neto", color_continuous_scale=px.colors.sequential.Inferno,title='Parallel Categories Sales Category Diagram')
		else:
			if selected_cluster in list(df10):
				dff=get_views.get_view_by_name('paralell_plot_cluster')
				grupos=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
				fig2 = px.parallel_categories(grupos, dimensions=choose,color="valor_neto", color_continuous_scale=px.colors.sequential.Inferno,title='Parallel Categories Sales Category Diagram')
			else:
				dff=get_views.get_view_by_name('paralell_plot_cluster')
				grupos=dff[(dff['ciudad_tienda']==selected_ciudad)]
				fig2 = px.parallel_categories(grupos, dimensions=choose,color="valor_neto", color_continuous_scale=px.colors.sequential.Inferno,title='Parallel Categories Sales Category Diagram')
		return fig2
######################################
	@app.callback(
	Output(component_id='fig3', component_property='figure'),
	Input('cluster-dpdn', 'value'),
	Input('ciudades-dpdn', 'value'),
	Input(component_id="slct_year3", component_property='value')
	)
	def update(selected_cluster, selected_ciudad,choose):
		clean=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
		df=clean[clean['ciudad_tienda']==selected_ciudad]
		df10=df['cluster_id'].unique()
		if selected_cluster is None and choose=='edad':
			dff=get_views.get_view_by_name('edad_count_avg_cluster')
			df_line=dff[(dff['ciudad_tienda']==selected_ciudad)]
			fig3 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color=choose,hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		elif selected_cluster is None and choose=='canal':
			dff=get_views.get_view_by_name('count_avg_cluster')
			df_line=dff[(dff['ciudad_tienda']==selected_ciudad)]
			fig3 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color=choose,hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		elif selected_cluster in list(df10) and choose=='edad':
			dff=get_views.get_view_by_name('edad_count_avg_cluster')
			df_line=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			fig3 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color=choose,hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		elif selected_cluster in list(df10) and choose=='canal':
			dff=get_views.get_view_by_name('count_avg_cluster')
			df_line=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			fig3 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color=choose,hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		elif selected_cluster not in list(df10) and choose=='canal':
			dff=get_views.get_view_by_name('count_avg_cluster')
			df_line=dff[(dff['ciudad_tienda']==selected_ciudad)]
			fig3 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color=choose,hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		else:
			dff=get_views.get_view_by_name('edad_count_avg_cluster')
			df_line=dff[(dff['ciudad_tienda']==selected_ciudad)]
			fig3 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color=choose,hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		return fig3
##################################
	@app.callback(
	Output(component_id='fig4', component_property='figure'),
	Input('cluster-dpdn', 'value'),
	Input('ciudades-dpdn', 'value'),
	Input(component_id='xaxis_raditem', component_property='value')
	)
	def barp(selected_cluster, selected_ciudad,select):
		clean=get_views.get_view_by_name('canal_edad_tipo_ciudad_cluster')
		df=clean[clean['ciudad_tienda']==selected_ciudad]
		df10=df['cluster_id'].unique()
		if (selected_cluster is None and select=='grupo_articulo') or (selected_cluster not in list(df10) and select=='grupo_articulo'):
			dff=get_views.get_view_by_name('ciudad_tienda_grupo_articulo_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad)]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False).head(10)
			fig5=px.bar(df_bar, y='grupo_articulo', x="volumen_pesos", color='grupo_articulo', orientation="h", hover_name="ciudad_tienda" ,title="Sales generated according to: {}".format(select))
		elif (selected_cluster is None and select=='canal') or (selected_cluster not in list(df10) and select=='canal'):
			dff=get_views.get_view_by_name('ciudad_tienda_canal_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad)]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='canal', x="volumen_pesos", color='canal', orientation="h", hover_name="ciudad_tienda" ,title="Sales generated according to: {}".format(select))
		elif (selected_cluster is None and select=='sublinea') or (selected_cluster not in list(df10) and select=='sublinea'):
			dff=get_views.get_view_by_name('ciudad_tienda_sublinea_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad)]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='sublinea', x="volumen_pesos", color='sublinea', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster is None and select=='saldo') or (selected_cluster not in list(df10) and select=='saldo'):
			dff=get_views.get_view_by_name('ciudad_tienda_saldo_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad)]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='saldo', x="volumen_pesos", color='saldo', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster is None and select=='tipo_tejido') or (selected_cluster not in list(df10) and select=='tipo_tejido'):
			dff=get_views.get_view_by_name('ciudad_tienda_tipo_tejido_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad)]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='tipo_tejido', x="volumen_pesos", color='tipo_tejido', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster is None and select=='tipo_articulo') or (selected_cluster not in list(df10) and select=='tipo_articulo'):
			dff=get_views.get_view_by_name('ciudad_tienda_tipo_articulo_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad)]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False).head(10)
			fig5=px.bar(df_bar, y='tipo_articulo', x="volumen_pesos", color='tipo_articulo', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster is None and select=='mes_venta') or (selected_cluster not in list(df10) and select=='mes_venta'):
			dff=get_views.get_view_by_name('ciudad_tienda_mes_venta_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad)]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='mes_venta', x="volumen_pesos", color='mes_venta', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster in list(df10) and select=='grupo_articulo'):
			dff=get_views.get_view_by_name('ciudad_tienda_grupo_articulo_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False).head(10)
			fig5=px.bar(df_bar, y='grupo_articulo', x="volumen_pesos", color='grupo_articulo', orientation="h", hover_name="ciudad_tienda" ,title="Sales generated according to: {}".format(select))
		elif (selected_cluster in list(df10) and select=='canal'):
			dff=get_views.get_view_by_name('ciudad_tienda_canal_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5 = px.bar(df_bar, y='canal', x="volumen_pesos", color='canal', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster in list(df10) and  select=='sublinea'):
			dff=get_views.get_view_by_name('ciudad_tienda_sublinea_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='sublinea', x="volumen_pesos", color='sublinea', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster in list(df10) and select=='saldo'):
			dff=get_views.get_view_by_name('ciudad_tienda_saldo_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='saldo', x="volumen_pesos", color='saldo', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster in list(df10) and  select=='tipo_tejido'):
			dff=get_views.get_view_by_name('ciudad_tienda_tipo_tejido_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='tipo_tejido', x="volumen_pesos", color='tipo_tejido', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster in list(df10) and  select=='mes_venta'):
			dff=get_views.get_view_by_name('ciudad_tienda_mes_venta_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='mes_venta', x="volumen_pesos", color='mes_venta', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (selected_cluster in list(df10) and  select=='tipo_articulo'):
			dff=get_views.get_view_by_name('ciudad_tienda_tipo_articulo_cluster')
			df_bar=dff[(dff['ciudad_tienda']==selected_ciudad) & dff['cluster_id'].isin([selected_cluster])]
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False).head(10)
			fig5=px.bar(df_bar, y='tipo_articulo', x="volumen_pesos", color='tipo_articulo', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		else:
			print('no found')
		return fig5
			################################################################ cities map #######

	@app.callback(
		[Output(component_id='call_cities_map', component_property='srcDoc'),
		Output(component_id='line_plot_cities', component_property='figure')],
		Input(component_id='slct_ciudad_map', component_property='value')
		)

	def map_cities(ciudad):
		line_df = get_views.get_view_by_name('ventas_diarias_ciudad')
		line_df["ciudad_tienda"]=line_df["ciudad_tienda"].apply(lambda x: x.capitalize())
		line_df=line_df[line_df["ciudad_tienda"]==ciudad]
		fig6 = px.line(line_df,x = 'fecha_compra',y = 'volumen_ventas',hover_data=['promedio_ventas'])

		return open('maps/'+ciudad+'_map.html','r').read(), fig6


	@app.callback(
		[Output('table','data'),
		Output('user','options')],
		[Input('ciudad_dropdown','value'),
		Input('user','value')]
	)
	def recom_sys(city, user):
		payload = {}
		ip = '127.0.0.1'
		port = 5000
		url = 'http://{0}:{1}/api/v1/suggest/'.format(ip, port)
		if city is not None:
			payload['city'] = city
		if user is not None:
			payload['user'] = user
		r = requests.post(url=url, data=json.dumps(payload))
		response = r.json()
		resu = pd.DataFrame()
		resu['Recommended Articles'] = response['Recommended Articles']
		options = response['Options']
		return resu.to_dict('records'), options
