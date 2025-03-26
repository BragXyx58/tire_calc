class TireCalculator:
    def __init__(self):
        pass

    def calc_profile_height(self, width, profile_percentage):
        return (width * profile_percentage) / 100

    def calc_diameter(self, width, profile_percentage, rim_diameter):
        profile_height = self.calc_profile_height(width, profile_percentage)
        return rim_diameter + 2 * profile_height / 25.4

    def calc_clearance_change(self, old_diameter, new_diameter):
        return (new_diameter - old_diameter) * 25.4

    def calc_speed_difference(self, old_diameter, new_diameter, speed):
        return (new_diameter / old_diameter - 1) * speed
