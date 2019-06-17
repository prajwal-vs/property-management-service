import json

from flask import request
from flask_restful import Resource

from services.propertyManagement import PropertyService


class RoomAddition(Resource):

    def __init__(self):
        self.service = PropertyService()

    def post(self, building_id):
        """Add Rooms."""
        data = json.loads(request.data)

        output = self.service.add_room_details(data, building_id)
        return output
