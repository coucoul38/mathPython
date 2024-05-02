
import numpy as np
import matplotlib.pyplot as plt

# Constantes
g = 9.81  # Accélération due à la gravité (m/s²)
rho_water = 1000  # Densité de l'eau (kg/m³)
Cd = 0.47  # Coefficient de traînée
A = 10  # Section transversale du sous-marin (m²)
mass = 5000  # Masse du sous-marin (kg)
volume = 5  # Volume du sous-marin (m³)
engine_force = 2000  # Force de poussée des moteurs (N)
dive_force = 1500  # Force de plongée vers le bas (N)

# Conditions initiales
initial_position = np.array([0.0, 0.0])  # Position initiale [x, y]
initial_velocity = np.array([2.0, -1.0])  # Vitesse initiale [vx, vy] avec mouvement vers le bas
initial_time = 0  # Temps initial
time_final = 10  # Temps final
time_step = 0.01  # Pas de temps

# Fonction pour calculer les forces
def calculate_forces(position, velocity):
    # Poids
    weight = np.array([0, -mass * g])

    # Poussée d'Archimède
    buoyancy = np.array([0, rho_water * volume * g])

    # Frottements avec l'eau (résistance)
    drag = -0.5 * Cd * rho_water * A * velocity

    # Poussée des moteurs (vers l'avant)
    engine = np.array([engine_force, 0])

    # Force de plongée (vers le bas)
    dive = np.array([0, -dive_force])

    # Somme des forces
    net_force = weight + buoyancy + drag + engine + dive

    return net_force

# Fonction pour calculer le mouvement
def simulate_motion(initial_position, initial_velocity, initial_time, time_final, time_step):
    # Conditions initiales
    position = initial_position.copy()
    velocity = initial_velocity.copy()
    time = initial_time
    
    # Liste pour stocker la trajectoire
    trajectory = []
    
    # Simulation
    while time <= time_final:
        trajectory.append(position.copy())
        
        # Calcul des forces
        net_force = calculate_forces(position, velocity)
        
        # Calcul de l'accélération
        acceleration = net_force / mass
        
        # Mise à jour de la vitesse
        velocity += acceleration * time_step
        
        # Mise à jour de la position
        position += velocity * time_step
        
        # Mise à jour du temps
        time += time_step
    
    return np.array(trajectory)

# Simuler le mouvement
trajectory = simulate_motion(initial_position, initial_velocity, initial_time, time_final, time_step)



# Tracer la trajectoire
plt.plot(trajectory[:, 0], trajectory[:, 1], label="Trajectoire du sous-marin")
plt.xlabel("Position X (m)")
plt.ylabel("Position Y (m)")
plt.title("Trajectoire du Nautilus en train de plonger")
plt.axhline(0, color='blue', linestyle='--', label="Surface de l'eau")
plt.legend()
plt.grid(True)
plt.show()