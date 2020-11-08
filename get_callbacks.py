from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from scripts import tabs
from data_fetch import get_views

def return_callbacks(app):

	@app.callback(
		Output("app-content", "children"),
		[
			Input("tabs","value")
		]
	)
	def get_current_content(selected_tab):
		return tabs.create_content_tab(selected_tab)


########################Callbacks diagrama de torta
# Connect the Plotly graphs with Dash Components
	@app.callback(
    	Output(component_id='pie_chart1', component_property='figure'),
    	Input(component_id='slct_year', component_property='value')
		)
	def update_graph(option_slctd):
		clean2=get_views.get_view_by_name('canal_edad_tipo_ciudad')
		dff = clean2[clean2['ciudad_tienda'] == option_slctd]
		fig = px.sunburst(dff, path=['canal','edad','tipo_articulo'], values='volumen_pesos', color='canal',title="Total sales  for the city of: {}".format(option_slctd))
		return fig
###################################################################lineplot##########
	@app.callback(
    	Output(component_id='fig3', component_property='figure'),
    	Input(component_id='slct_year3', component_property='value')
	)

	def update(choose):
		if (choose=='edad'):
			df_line=get_views.get_view_by_name('edad_count_avg')
			fig2 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color='edad',hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		else:
			df_line=get_views.get_view_by_name('count_avg')
			fig2 = px.scatter(df_line, x="fecha_compra", y='ventas_promedio', color='canal',hover_data=['cantidad_compras'],title="Trend of sales according to the annual course of : {}".format(choose))
		return fig2

############################################################# parallel plot######

	@app.callback(
    	Output(component_id='par', component_property='figure'),
    	Input(component_id='check', component_property='value')
	)
	def paral(choose):
		grupos=get_views.get_view_by_name('parallel_plot')
		fig3 = px.parallel_categories(grupos, dimensions=choose,color="valor_neto", color_continuous_scale=px.colors.sequential.Inferno,title='Parallel Categories Sales Category Diagram')
		return fig3


################################################################ barplot #######
	@app.callback(
		Output(component_id='fig4', component_property='figure'),
		Input(component_id='xaxis_raditem', component_property='value')
	)
	def barp(select):
		if (select=='canal'):
			df_bar=get_views.get_view_by_name('ciudad_tienda_canal')
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5 = px.bar(df_bar, y='canal', x="volumen_pesos", color='canal', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (select=='sublinea'):
			df_bar=get_views.get_view_by_name('ciudad_tienda_sublinea')
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='sublinea', x="volumen_pesos", color='sublinea', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (select=='saldo'):
			df_bar=get_views.get_view_by_name('ciudad_tienda_saldo')
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='saldo', x="volumen_pesos", color='saldo', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (select=='tipo_tejido'):
			df_bar=get_views.get_view_by_name('ciudad_tienda_tipo_tejido')
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='tipo_tejido', x="volumen_pesos", color='tipo_tejido', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (select=='mes_venta'):
			df_bar=get_views.get_view_by_name('ciudad_tienda_mes_venta')
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False)
			fig5=px.bar(df_bar, y='mes_venta', x="volumen_pesos", color='mes_venta', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		elif (select=='tipo_articulo'):
			df_bar=get_views.get_view_by_name('ciudad_tienda_tipo_articulo')
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False).head(50)
			fig5=px.bar(df_bar, y='tipo_articulo', x="volumen_pesos", color='tipo_articulo', orientation="h", hover_name="ciudad_tienda",title="Sales generated according to: {}".format(select))
		else:
			df_bar=get_views.get_view_by_name('ciudad_tienda_grupo_articulo')
			df_bar=df_bar.sort_values('volumen_pesos',ascending=False).head(50)
			fig5=px.bar(df_bar, y='grupo_articulo', x="volumen_pesos", color='grupo_articulo', orientation="h", hover_name="ciudad_tienda" ,title="Sales generated according to: {}".format(select))
		return fig5
