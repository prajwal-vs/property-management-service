from flask_restful import Resource

from services.propertyManagement import PropertyService


class RoomList(Resource):
    def __init__(self):
        self.service = PropertyService()

    def get(self, building_id):
        """Room List."""

        query = {"building_id": building_id}
        result = self.service.get_list_room("rooms", querydata=query)

        return result
