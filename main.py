from medical_data_visualizer import draw_cat_plot, draw_heat_map

# Generate and save cat plot
cat_fig = draw_cat_plot()
cat_fig.savefig('catplot.png')

# Generate and save heat map
heat_fig = draw_heat_map()
heat_fig.savefig('heatmap.png')