from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

#parameters:
p = 4

x1 = -1.6
x2 = 1.6
y1 = -1
y2 = 1

width = 960
height = 600

max_iter = 3
epsilon = 1e-4

def f(z):
	return 1./p*((p-1)*z+1./(z**(p-1)))
	
roots = [complex(1, 0), complex(0, 1), complex(-1, 0), complex(0, -1)]
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

image = np.zeros((height, width, 3))



def get_color(index, intensity):
	ret = colors[index]
	
	
	
def draw(n):

	max_iter = n
	
	percent = 0
	
	for w in range(width):
		
		if (int(float(w)/width*100) > percent+10):
			percent = int(float(w)/width*100)
			#try:
			misc.imsave("fractal1.tif", image)
			#except:
			#	pass
			#print(str(percent) + "%")
		
		
		
		for h in range(height):
		
			current_x = x1 + (float(w)/width)*(x2-x1)
			current_y = y1 + (float(h)/height)*(y2-y1)
			
			current_point = complex(current_x, current_y)
			has_converged = False
			root_index = -1
			pixel = None
			
			try:
				for i in range(max_iter):
					next_point = f(current_point)
					if (abs(current_point - next_point) < epsilon):
						has_converged = True
						current_point = next_point
						break
					current_point = next_point
					
			except ZeroDivisionError:
				has_converged = False
			
			if has_converged:
				saturation = 1.-float(i)/max_iter
				r=b=g=255.0*saturation
				if (abs(current_point-roots[0]) < epsilon): r *= 4
				if (abs(current_point-roots[1]) < epsilon): g *= 4
				if (abs(current_point-roots[2]) < epsilon): b *= 4
				if (abs(current_point-roots[3]) < epsilon): 
					r *= 4
					g *= 4
				
				pixel = (int(r), int(g), int(b))
					
			else:
				pixel = (0,0,0)
			
			image[h, w, :] = pixel
		
		
		
	misc.imsave("fractal_" + str(n) + ".tif", image)
	
	
def main():
	for i in range(2, 32, 1):
		print("Drawing for i=" + str(i))
		draw(i)
		print("Finished for i=" + str(i))
	
	
main()
