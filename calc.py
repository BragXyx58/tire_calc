class TireCalculator:
    def __init__(self):
        pass

    def calculate_profile_height(self, width, profile_percentage):
        return (width * profile_percentage) / 100

    def calculate_diameter(self, width, profile_percentage, rim_diameter):
        profile_height = self.calculate_profile_height(width, profile_percentage)
        diameter = rim_diameter + 2 * profile_height / 25.4
        return diameter

    def adjust_diameter_for_rim(self, diameter, et, rim_width):
        # Это не точная формулa
        return diameter + (et * 0.05) + (rim_width * 0.1)

    def calculate_clearance_change(self, old_diameter, new_diameter):
        return (new_diameter - old_diameter) * 25.4

    def calculate_speed_difference(self, old_diameter, new_diameter, speed):
        return ((new_diameter / old_diameter) - 1) * speed
