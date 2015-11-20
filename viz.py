import scanner, classifier
from bokeh.plotting import figure, output_file, show
output_file("line.html")
p = figure(plot_width=400, plot_height=400)
p.circle(0, 0, size=20, color="navy", alpha=0.5, text="shit")
show(p)