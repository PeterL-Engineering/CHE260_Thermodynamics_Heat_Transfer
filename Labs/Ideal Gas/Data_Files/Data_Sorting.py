def parse_data_file(filename):
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
                        
                        # Only keep data points at 0.5 second intervals
                        # Using tolerance for floating-point precision
                        if abs(time_val % 0.5) < 0.001 or abs(time_val % 0.5 - 0.5) < 0.001:
                            time.append(time_val)
                            T1.append(T1_val)
                            T2.append(T2_val)
                            P1.append(P1_val)
                            P2.append(P2_val)
                            mass_flowrate.append(mass_flow_val)
                        
                    except (ValueError, IndexError) as e:
                        print(f"Warning: Could not parse data line: {line}")
                        print(f"Error: {e}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None, None, None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, None, None, None, None
    
    return time, T1, T2, P1, P2, mass_flowrate

def print_summary(time, T1, T2, P1, P2, mass_flowrate):
    """Print a summary of the parsed data"""
    print("Data Summary (0.5 second intervals):")
    print(f"Number of data points: {len(time)}")
    print(f"Time range: {min(time) if time else 'N/A'} to {max(time) if time else 'N/A'} s")
    print(f"T1 range: {min(T1) if T1 else 'N/A'} to {max(T1) if T1 else 'N/A'} °C")
    print(f"T2 range: {min(T2) if T2 else 'N/A'} to {max(T2) if T2 else 'N/A'} °C")
    print(f"P1 range: {min(P1) if P1 else 'N/A'} to {max(P1) if P1 else 'N/A'} PSI")
    print(f"P2 range: {min(P2) if P2 else 'N/A'} to {max(P2) if P2 else 'N/A'} PSI")
    print(f"Mass Flowrate range: {min(mass_flowrate) if mass_flowrate else 'N/A'} to {max(mass_flowrate) if mass_flowrate else 'N/A'} g/min")

# Example usage
if __name__ == "__main__":
    filename = "lab1-part2a.txt"  # Replace with your actual file name
    
    # Parse the data file
    time, T1, T2, P1, P2, mass_flowrate = parse_data_file(filename)
    
    # if time is not None:
    #     # Print summary
    #     print_summary(time, T1, T2, P1, P2, mass_flowrate)
        
    #     # Print all values to verify
    #     print("\nAll data points (0.5 second intervals):")
    #     print("Time(s)\tT1(°C)\tT2(°C)\tP1(PSI)\tP2(PSI)\tMass Flow(g/min)")
    #     for i in range(len(time)):
    #         print(f"{time[i]:.1f}\t{T1[i]:.2f}\t{T2[i]:.2f}\t{P1[i]:.2f}\t{P2[i]:.2f}\t{mass_flowrate[i]:.2f}")
        
    #     # # You can now use the arrays for further processing
    #     # print(f"\nArrays created:")
    #     # print(f"time array length: {len(time)}")
    #     # print(f"T1 array length: {len(T1)}")
    #     # print(f"T2 array length: {len(T2)}")
    #     # print(f"P1 array length: {len(P1)}")
    #     # print(f"P2 array length: {len(P2)}")
    #     # print(f"mass_flowrate array length: {len(mass_flowrate)}")
        
    # else:
    #     print("Failed to parse the data file.")

    import os

    # List all files in the current directory to see what's actually there
    print("Files in current directory:")
    for file in os.listdir('.'):
        if file.endswith('.txt'):
            print(f"  {file}")

    # # Then use the exact filename
    # filename = "your_exact_filename.txt"  # Replace with the actual name