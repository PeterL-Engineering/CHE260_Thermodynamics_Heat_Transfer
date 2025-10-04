import os

def parse_data_file(filename):
    # Check if file exists first
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return None, None, None, None, None, None
    
    # Initialize empty lists for each data column
    time = []
    T1 = []
    T2 = []
    P1 = []
    P2 = []
    mass_flowrate = []
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                line = line.strip()
                
                # Skip empty lines and header lines
                if not line or line.startswith('Ambient') or line.startswith('Time(s)'):
                    continue
                
                # Parse data rows (check if line starts with a number)
                elif line[0].isdigit() or (line[0] == '-' and line[1].isdigit()):
                    try:
                        # Split by whitespace (tabs or spaces)
                        values = line.split()
                        
                        # Convert all values to float
                        time_val = float(values[0])
                        T1_val = float(values[1])
                        T2_val = float(values[2])
                        P1_val = float(values[3])
                        P2_val = float(values[4])
                        mass_flow_val = float(values[5])
                        
                        # Only keep data points at 0.2 second intervals
                        if abs(time_val % 0.2) < 0.001:
                            time.append(time_val)
                            T1.append(T1_val)
                            T2.append(T2_val)
                            P1.append(P1_val)
                            P2.append(P2_val)
                            mass_flowrate.append(mass_flow_val)
                        
                    except (ValueError, IndexError) as e:
                        print(f"Warning: Could not parse data line: {line}")
                        continue
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, None, None, None, None
    
    return time, T1, T2, P1, P2, mass_flowrate

# Main execution
if __name__ == "__main__":
    # Replace final directory to desired file
    full_path = r"C:\Users\Peter\Documents\GitHub\CHE260_Thermodynamics_Heat_Transfer\Labs\Ideal Gas\Data_Files\lab1-part2a.txt"
    
    # Parse the data file
    time, T1, T2, P1, P2, mass_flowrate = parse_data_file(full_path)
    
    if time is not None:
        print(f"Successfully parsed {len(time)} data points at 0.5s intervals")
        print("\nFirst 10 data points:")
        print("Time(s)\tT1(°C)\tT2(°C)\tP1(PSI)\tP2(PSI)\tMass Flow(g/min)")
        for i in range(min(10, len(time))):
            print(f"{time[i]:.1f}\t{T1[i]:.2f}\t{T2[i]:.2f}\t{P1[i]:.2f}\t{P2[i]:.2f}\t{mass_flowrate[i]:.2f}")
    else:
        print("Failed to parse the data file.")