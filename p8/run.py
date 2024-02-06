from function1.dimensions import ShapeDimensions
from function2.volume import calculate_volume
from function3.surface_area import calculate_surface_area

def main():
    # setting dimensions
    shape = ShapeDimensions(5, 3, 2)
    print ("Dimensions:", shape.get_dimesions())

    # calculate volume
    volume = calculate_volume(*shape.get_dimesions())
    print("Volume:", volume)

    # calculate surface area
    surface_area =calculate_surface_area(*shape.get_dimesions())
    print("Surface Area:", surface_area)


if __name__=='__main__':
    main()