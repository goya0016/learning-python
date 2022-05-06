def main():
    cSpeed = 299792458
    mass = float(input("Enter Mass in Kg: "))
    energy = mass*cSpeed**2  #(m*c) * (m*c)
    print("E = %d kg*(m/s)2" % energy) # Check Energy units 
main()