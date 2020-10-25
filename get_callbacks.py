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