from dash.dependencies import Input, Output, State

from scripts import tabs

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

    		fig = px.sunburst(dff, path=['canal','edad','tipo_articulo'], values='volumen_pesos', color='canal')

    		return fig
###################################################################lineplot##########
	@app.callback(
    	Output(component_id='fig3', component_property='figure'),
    	Input(component_id='slct_year3', component_property='value')
		)

		def update(choose):
    		if (choose=='edad'):
				df_line=get_views.get_view_by_name('edad_count_avg')
			else:
				df_line=get_views.get_view_by_name('count_avg')


    		fig2 = px.line(df_line, x="fecha_compra", y='ventas_promedio', color=choose,hover_data=['cantidad_compras'])

    		return fig2

############################################################# parallel plot######

	@app.callback(
    	Output(component_id='par', component_property='figure'),
    	Input(component_id='check', component_property='value')
		)

		def paral(choose):
    		grupos=get_views.get_view_by_name('parallel_plot')
    		fig3 = px.parallel_categories(grupos, dimensions=choose,color="valor_neto", color_continuous_scale=px.colors.sequential.Inferno)

    		return fig3


################################################################
