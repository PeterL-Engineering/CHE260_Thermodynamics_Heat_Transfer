from Data_Sorting import parse_data_file
import matplotlib.pyplot as plt

def plot_mass_flow_rate(time, flow_rate):
    """
    Function Description:
        - Plots the mass flow rate as a function of time

    Parameters:
        - time (array_like): array of time points
        - flow_rate (array_like): array of mass flow rate that correspond to time array

    Returns:
        - none
    """

    # Plot results
    plt.figure(figsize=(12, 10))

    # Plot mass flow rate
    plt.plot(time, flow_rate, 'b-', linewidth=2)
    plt.title('Mass Flow Rate vs. Time', fontsize=14)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Mass Flow Rate (g/min)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_pressure_temperature(time, T1, T2, P1, P2):
    """
    Function Description:
        - Plots temperature and pressure for two tanks as functions of time
        - Creates two subplots: one for Tank 1 and one for Tank 2
        - Each subplot displays both temperature and pressure on the same axes

    Parameters:
        - time (array_like): Array of time points
        - T1 (array_like): Temperature values for Tank 1 corresponding to time array
        - T2 (array_like): Temperature values for Tank 2 corresponding to time array  
        - P1 (array_like): Pressure values for Tank 1 corresponding to time array
        - P2 (array_like): Pressure values for Tank 2 corresponding to time array

    Returns:
        - none
    """
    plt.figure(figsize=(12, 8))

    # Plot 1: Tank 1 temperature and pressure
    plt.subplot(2, 1, 1)
    ax1 = plt.gca()
    ax2 = ax1.twinx()

    ax1.plot(time, T1, 'r-', linewidth=2, label='Tank 1 Temperature')
    ax2.plot(time, P1, 'b-', linewidth=2, label='Tank 1 Pressure')
    plt.title('Tank 1: Temperature and Pressure', fontsize=14)
    ax1.set_ylabel('Temperature (°C)', fontsize=12, color='red')
    ax2.set_ylabel('Pressure (psi)', fontsize=12, color='blue')
    ax1.grid(True, alpha=0.3)

    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower right')

    # Plot 2: Tank 2 temperature and pressure
    plt.subplot(2, 1, 2)
    ax3 = plt.gca()
    ax4 = ax3.twinx()

    ax3.plot(time, T2, 'r-', linewidth=2, label='Tank 2 Temperature')
    ax4.plot(time, P2, 'b-', linewidth=2, label='Tank 2 Pressure')
    plt.title('Tank 2: Temperature and Pressure', fontsize=14)
    ax3.set_xlabel('Time', fontsize=12)
    ax3.set_ylabel('Temperature (°C)', fontsize=12, color='red')
    ax4.set_ylabel('Pressure (psi)', fontsize=12, color='blue')
    ax3.grid(True, alpha=0.3)

    # Combine legends
    lines3, labels3 = ax3.get_legend_handles_labels()
    lines4, labels4 = ax4.get_legend_handles_labels()
    ax3.legend(lines3 + lines4, labels3 + labels4, loc='lower right')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Part 1a data
    full_path = r"C:\Users\Peter\Documents\GitHub\CHE260_Thermodynamics_Heat_Transfer\Labs\Ideal Gas\Data_Files\lab1-part1a.txt"
    time_1a, T1_1a, T2_1a, P1_1a, P2_1a, mass_flowrate_1a = parse_data_file(full_path)

    # # Slice mass flow from start to time = 200 seconds
    # mass_flowrate_1a_sliced = mass_flowrate_1a[:150]
    # time_1a_sliced = time_1a[:150]

    # plot_mass_flow_rate(time_1a_sliced, mass_flowrate_1a_sliced)
    # plot_pressure_temperature(time_1a, T1_1a, T2_1a, P1_1a, P2_1a)

    # Part 1b data
    full_path = r"C:\Users\Peter\Documents\GitHub\CHE260_Thermodynamics_Heat_Transfer\Labs\Ideal Gas\Data_Files\lab1-part1b.txt"
    time_1b, T1_1b, T2_1b, P1_1b, P2_1b, mass_flowrate_1b = parse_data_file(full_path)

    # Slice mass flow from start to time = 140 seconds
    mass_flowrate_1b_sliced = mass_flowrate_1b[:100]
    time_1b_sliced = time_1b[:100]

    plot_mass_flow_rate(time_1b_sliced, mass_flowrate_1b_sliced)
    plot_pressure_temperature(time_1b, T1_1b, T2_1b, P1_1b, P2_1b)

    # Part 2a data
    full_path = r"C:\Users\Peter\Documents\GitHub\CHE260_Thermodynamics_Heat_Transfer\Labs\Ideal Gas\Data_Files\lab1-part2a.txt"
    time_2a, T1_2a, T2_2a, P1_2a, P2_2a, mass_flowrate_2a = parse_data_file(full_path)

    # # Slice mass flow from start to time = 60 seconds
    # mass_flowrate_2a_sliced = mass_flowrate_2a[:120]
    # time_2a_sliced = time_2a[:120]

    # plot_mass_flow_rate(time_2a_sliced, mass_flowrate_2a_sliced)
    # plot_pressure_temperature(time_2a, T1_2a, T2_2a, P1_2a, P2_2a)
