import math

def main():
	hubLength=2.69
	raisedFace=0.0625
	flangeThinckness=0.81
	hubD=3.31
	pipeOD=2.38

	r=0.12

	x_right = hubLength+raisedFace-(pipeOD/2-0.03)*math.tan(math.radians(40))

	for alpha in range(19, 45):
		theta = 90-alpha
		x = flangeThinckness+raisedFace
		y = hubD/2

		print(theta)

		A = x+r*(1-math.cos(math.radians(theta)))
		B = y-r*math.sin(math.radians(theta))

		m = - A/B
		b = B-m*A

		y2 = pipeOD/2
		x2 = (y2-b)/m

		if x_right-x2 >= 0.25:
			print("It works")
			break


	print("alpha:", alpha)
	print("A:", A)
	print("B:", B)
	print("x_Right:", x_right)
	print("x2:", x2)
	print("y2:", y2)

if __name__ == "__main__":
    main()