# this is a python3 code snippet that can be used to diagnose the membrane mechanisms inserted in a neuron model

for sec in h.allsec():
	for seg in sec:
		for mech in seg:
			print(sec.name(), seg.x, mech.name())

shape_window = h.PlotShape()
shape_window.exec_menu('Show Diam')
