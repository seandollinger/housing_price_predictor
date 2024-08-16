class House:
    def __init__(self, house_id, neighborhood, house_style, overall_condition, year_built, roof_type, roof_material, foundation_material, heating, central_air, electrical, fireplace_num, garage_area, date_sold):
        self.house_id = house_id
        self.neighborhood = neighborhood
        self.house_style = house_style
        self.overall_condition = overall_condition
        self.year_built = year_built
        self.roof_type = roof_type
        self.roof_material = roof_material
        self.foundation_material = foundation_material
        self.heating = heating
        self.central_air = central_air
        self.electrical = electrical
        self.fireplace_num = fireplace_num
        self.garage_area = garage_area
        self.date_sold = date_sold

    def to_dict(self):
        """Returns the house details as a dictionary."""
        return self.__dict__

class HouseDataset:
    def __init__(self):
        self.houses = {}  # Dictionary to store House instances with house_id as key

    def add_house(self, house: House) -> None:
        """Adds a new house to the dataset."""
        self.houses[house.house_id] = house

    def get_house_by_id(self, house_id: int) -> House:
        """Returns a house by its ID."""
        return self.houses.get(house_id)

    def update_house_by_id(self, house_id: int, updated_fields: dict) -> None:
        """Updates house fields by house ID."""
        house = self.get_house_by_id(house_id)
        if house:
            for key, value in updated_fields.items():
                setattr(house, key, value)

    def delete_house_by_id(self, house_id: int) -> None:
        """Deletes a house by its ID."""
        if house_id in self.houses:
            del self.houses[house_id]

    def get_houses_by_filters(self, filters: dict) -> list:
        """Returns a list of houses filtered by specific criteria."""
        result = []
        for house in self.houses.values():
            match = True
            for key, value in filters.items():
                if getattr(house, key) != value:
                    match = False
                    break
            if match:
                result.append(house)
        return result
